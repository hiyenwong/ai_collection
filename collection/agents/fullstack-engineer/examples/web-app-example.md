# Fullstack Engineer Agent - Web Application Example

## User Request

```
我需要构建一个 SaaS 产品：一个团队协作的任务管理系统。

核心功能：
- 用户注册和登录
- 创建项目和团队
- 任务看板（类似 Trello）
- 实时协作
- 通知系统

技术栈偏好：
- 前端：React + TypeScript
- 后端：Node.js + Express
- 数据库：PostgreSQL
- 实时：Socket.io
```

## Agent Response

### Phase 1: Architecture Planning

**Tech Stack Selection:**

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | React 18 + TypeScript + Vite | Modern, fast, type-safe |
| State | Zustand + React Query | Simple state, efficient server state |
| UI | TailwindCSS + shadcn/ui | Beautiful, customizable |
| Backend | Node.js + Express + TypeScript | Consistent language with frontend |
| Database | PostgreSQL + Prisma ORM | Type-safe queries, migrations |
| Auth | JWT + bcrypt | Standard, secure |
| Real-time | Socket.io | Well-established WebSocket library |
| Deployment | Docker + Docker Compose | Easy deployment and scaling |

**Project Structure:**
```
taskflow/
├── apps/
│   ├── web/                    # React frontend
│   │   ├── src/
│   │   │   ├── components/     # Reusable UI components
│   │   │   ├── features/       # Feature-based modules
│   │   │   │   ├── auth/
│   │   │   │   ├── projects/
│   │   │   │   ├── tasks/
│   │   │   │   └── notifications/
│   │   │   ├── hooks/          # Custom React hooks
│   │   │   ├── lib/            # Utilities
│   │   │   └── types/          # TypeScript types
│   │   └── package.json
│   │
│   └── api/                    # Express backend
│       ├── src/
│       │   ├── routes/         # API routes
│       │   ├── controllers/    # Request handlers
│       │   ├── services/       # Business logic
│       │   ├── models/         # Prisma models
│       │   ├── middleware/     # Express middleware
│       │   └── socket/         # Socket.io handlers
│       └── package.json
│
├── packages/
│   ├── shared/                 # Shared TypeScript types
│   └── config/                 # Shared configuration
│
├── docker-compose.yml
├── Dockerfile.web
├── Dockerfile.api
└── package.json
```

### Phase 2: Database Schema

**Prisma Schema:**
```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id            String    @id @default(cuid())
  email         String    @unique
  passwordHash  String
  name          String?
  avatar        String?
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt

  // Relations
  ownedProjects Project[]  @relation("ProjectOwner")
  members       ProjectMember[]
  assignedTasks Task[]     @relation("TaskAssignee")
  createdTasks  Task[]     @relation("TaskCreator")
  notifications Notification[]
}

model Project {
  id          String    @id @default(cuid())
  name        String
  description String?
  ownerId     String
  createdAt   DateTime  @default(now())
  updatedAt   DateTime  @updatedAt

  // Relations
  owner   User            @relation("ProjectOwner", fields: [ownerId], references: [id])
  members ProjectMember[]
  columns Column[]

  @@index([ownerId])
}

model ProjectMember {
  id        String   @id @default(cuid())
  projectId String
  userId    String
  role      MemberRole @default(MEMBER)
  joinedAt  DateTime @default(now())

  // Relations
  project Project @relation(fields: [projectId], references: [id], onDelete: Cascade)
  user    User    @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([projectId, userId])
  @@index([projectId])
  @@index([userId])
}

enum MemberRole {
  OWNER
  ADMIN
  MEMBER
  VIEWER
}

model Column {
  id        String   @id @default(cuid())
  projectId String
  name      String
  position  Int
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  // Relations
  project Project @relation(fields: [projectId], references: [id], onDelete: Cascade)
  tasks   Task[]

  @@index([projectId])
}

model Task {
  id          String     @id @default(cuid())
  title       String
  description String?
  columnId    String
  projectId   String
  assigneeId  String?
  creatorId   String
  priority    Priority   @default(MEDIUM)
  dueDate     DateTime?
  position    Int
  createdAt   DateTime   @default(now())
  updatedAt   DateTime   @updatedAt

  // Relations
  column    Column @relation(fields: [columnId], references: [id], onDelete: Cascade)
  assignee  User?  @relation("TaskAssignee", fields: [assigneeId], references: [id])
  creator   User   @relation("TaskCreator", fields: [creatorId], references: [id])
  comments  Comment[]
  tags      TaskTag[]

  @@index([columnId])
  @@index([projectId])
  @@index([assigneeId])
}

enum Priority {
  LOW
  MEDIUM
  HIGH
  URGENT
}

model Comment {
  id        String   @id @default(cuid())
  content   String
  taskId    String
  userId    String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  // Relations
  task Task @relation(fields: [taskId], references: [id], onDelete: Cascade)
  user User @relation(fields: [userId], references: [id])

  @@index([taskId])
}

model Tag {
  id    String @id @default(cuid())
  name  String @unique
  color String

  // Relations
  tasks TaskTag[]
}

model TaskTag {
  taskId String
  tagId  String

  // Relations
  task Task @relation(fields: [taskId], references: [id], onDelete: Cascade)
  tag  Tag  @relation(fields: [tagId], references: [id], onDelete: Cascade)

  @@id([taskId, tagId])
  @@index([taskId])
  @@index([tagId])
}

model Notification {
  id        String           @id @default(cuid())
  userId    String
  type      NotificationType
  title     String
  message   String
  read      Boolean          @default(false)
  createdAt DateTime         @default(now())

  // Relations
  user User @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@index([userId])
  @@index([read])
}

enum NotificationType {
  TASK_ASSIGNED
  TASK_MOVED
  COMMENT_ADDED
  PROJECT_INVITE
}
```

### Phase 3: API Design

**REST Endpoints:**

```
# Authentication
POST   /api/auth/register
POST   /api/auth/login
POST   /api/auth/refresh
POST   /api/auth/logout

# Projects
GET    /api/projects
POST   /api/projects
GET    /api/projects/:id
PUT    /api/projects/:id
DELETE /api/projects/:id

# Project Members
GET    /api/projects/:id/members
POST   /api/projects/:id/members
DELETE /api/projects/:id/members/:userId

# Columns
GET    /api/projects/:id/columns
POST   /api/projects/:id/columns
PUT    /api/columns/:id
DELETE /api/columns/:id

# Tasks
GET    /api/projects/:id/tasks
POST   /api/projects/:id/tasks
GET    /api/tasks/:id
PUT    /api/tasks/:id
DELETE /api/tasks/:id
PATCH  /api/tasks/:id/move

# Comments
GET    /api/tasks/:id/comments
POST   /api/tasks/:id/comments

# Notifications
GET    /api/notifications
PATCH  /api/notifications/:id/read
```

**Socket.io Events:**

```
# Client → Server
task:move          { taskId, columnId, position }
task:update        { taskId, updates }
comment:create     { taskId, content }
project:join       { projectId }
project:leave      { projectId }

# Server → Client
task:moved         { task, sourceColumn, targetColumn }
task:updated       { task }
comment:created    { comment }
notification:new   { notification }
user:joined       { user, project }
user:left          { userId, project }
```

### Phase 4: Authentication Flow

**JWT-based Authentication:**

```typescript
// api/src/middleware/auth.ts
import jwt from 'jsonwebtoken';

export interface TokenPayload {
  userId: string;
  email: string;
}

export function authMiddleware(req: Request, res: Response, next: NextFn) {
  const token = req.headers.authorization?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET) as TokenPayload;
    req.user = payload;
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

**Token Refresh:**
```typescript
// api/src/routes/auth.ts
router.post('/refresh', async (req, res) => {
  const { refreshToken } = req.body;

  // Verify refresh token
  const payload = jwt.verify(refreshToken, REFRESH_SECRET);

  // Generate new access token
  const accessToken = jwt.sign(
    { userId: payload.userId },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );

  res.json({ accessToken });
});
```

### Phase 5: Real-time Updates

**Socket.io Integration:**

```typescript
// api/src/socket/taskHandler.ts
import { Server as SocketServer } from 'socket.io';

export function setupTaskHandlers(io: SocketServer) {
  io.on('connection', (socket) => {
    socket.on('task:move', async (data) => {
      const { taskId, columnId, position } = data;

      // Update in database
      const updatedTask = await moveTask(taskId, columnId, position);

      // Broadcast to project members
      socket.to(`project:${task.projectId}`).emit('task:moved', {
        task: updatedTask,
        movedBy: socket.data.user.id
      });
    });

    socket.on('project:join', async (projectId) => {
      // Verify user is member
      const isMember = await checkProjectMembership(socket.data.user.id, projectId);

      if (isMember) {
        socket.join(`project:${projectId}`);
        socket.emit('project:joined', { projectId });
      }
    });
  });
}
```

### Phase 6: Frontend State Management

**Zustand Store:**

```typescript
// web/src/stores/projectStore.ts
import create from 'zustand';
import { api } from '@/lib/api';

interface ProjectStore {
  projects: Project[];
  currentProject: Project | null;
  loading: boolean;

  fetchProjects: () => Promise<void>;
  setCurrentProject: (id: string) => void;
  createProject: (data: CreateProjectDto) => Promise<void>;
}

export const useProjectStore = create<ProjectStore>((set, get) => ({
  projects: [],
  currentProject: null,
  loading: false,

  fetchProjects: async () => {
    set({ loading: true });
    const projects = await api.projects.list();
    set({ projects, loading: false });
  },

  setCurrentProject: (id) => {
    const project = get().projects.find(p => p.id === id);
    set({ currentProject: project || null });
  },

  createProject: async (data) => {
    const project = await api.projects.create(data);
    set(state => ({ projects: [...state.projects, project] }));
  },
}));
```

**React Query for Server State:**

```typescript
// web/src/hooks/useTasks.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/lib/api';

export function useTasks(projectId: string) {
  return useQuery({
    queryKey: ['tasks', projectId],
    queryFn: () => api.tasks.list(projectId),
  });
}

export function useMoveTask() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ taskId, columnId, position }) =>
      api.tasks.move(taskId, { columnId, position }),

    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
    },
  });
}
```

### Phase 7: Deployment

**docker-compose.yml:**

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: taskflow
      POSTGRES_USER: taskflow
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  api:
    build:
      context: .
      dockerfile: Dockerfile.api
    environment:
      DATABASE_URL: postgresql://taskflow:${DB_PASSWORD}@postgres:5432/taskflow
      JWT_SECRET: ${JWT_SECRET}
    ports:
      - "3001:3001"
    depends_on:
      - postgres

  web:
    build:
      context: .
      dockerfile: Dockerfile.web
    ports:
      - "3000:80"
    depends_on:
      - api

volumes:
  postgres_data:
```

### Phase 8: Testing Strategy

```typescript
// Example test using Vitest
describe('Task API', () => {
  it('should create a task', async () => {
    const response = await app.request('/api/tasks', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
      json: {
        title: 'Test Task',
        columnId: testColumn.id,
      },
    });

    expect(response.status).toBe(201);
    expect(response.json.title).toBe('Test Task');
  });

  it('should move a task between columns', async () => {
    const response = await app.request(`/api/tasks/${task.id}/move`, {
      method: 'PATCH',
      headers: { Authorization: `Bearer ${token}` },
      json: { columnId: otherColumn.id, position: 0 },
    });

    expect(response.status).toBe(200);
    expect(response.json.columnId).toBe(otherColumn.id);
  });
});
```

---

## Deliverables Summary

1. ✅ **Architecture Design** - Complete tech stack selection
2. ✅ **Database Schema** - Prisma models with relations
3. ✅ **API Design** - REST endpoints + Socket.io events
4. ✅ **Authentication** - JWT-based auth flow
5. ✅ **Real-time Updates** - Socket.io integration
6. ✅ **State Management** - Zustand + React Query
7. ✅ **Deployment** - Docker Compose setup
8. ✅ **Testing Strategy** - Vitest examples

## Next Steps

1. Run: `npm install` && `npm run dev`
2. Access: http://localhost:3000
3. API Docs: http://localhost:3001/docs
4. Run tests: `npm test`

## V2 Suggestions

- Add file attachments to tasks
- Implement task dependencies (Gantt chart)
- Add time tracking feature
- Email notifications
- Mobile app (React Native)
