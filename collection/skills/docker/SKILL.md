---
name: docker
description: "Docker container management skill. Build, run, manage containers, images, networks, and volumes. Use for containerization, Docker Compose, multi-container apps, and DevOps tasks. Keywords: docker, container, docker-compose, image, volume, network, containerization."
---

# Docker

Docker container management for building, running, and managing containers.

## Activation Keywords

- docker
- container
- docker-compose
- docker compose
- containerization
- 容器
- 镜像
- docker build
- docker run

## Tools Used

- `exec` - Execute Docker CLI commands
- `read` - Read Dockerfiles, compose files
- `write` - Create Dockerfiles, compose files
- `edit` - Modify Docker configurations

## Workflow Decision Tree

```
User Request → Identify Task Type
├── Build Image → docker build workflow
├── Run Container → docker run workflow
├── Manage Containers → docker ps/stop/rm workflow
├── Compose Multi-Container → docker compose workflow
├── Network Management → docker network workflow
├── Volume Management → docker volume workflow
└── Debug Issues → docker logs/exec workflow
```

## Core Commands Reference

### Container Management

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Run container
docker run -d --name <name> -p <host:container> <image>

# Run with environment variables
docker run -d --name <name> -e KEY=VALUE <image>

# Run with volume mount
docker run -d --name <name> -v /host/path:/container/path <image>

# Stop container
docker stop <container>

# Remove container
docker rm <container>

# Force remove running container
docker rm -f <container>

# Execute command in container
docker exec -it <container> <command>

# View logs
docker logs <container>
docker logs -f <container>  # follow mode
docker logs --tail 100 <container>  # last 100 lines
```

### Image Management

```bash
# List images
docker images

# Build image from Dockerfile
docker build -t <name>:<tag> <path>
docker build -t <name>:<tag> -f <dockerfile> <path>

# Pull image
docker pull <image>:<tag>

# Push image
docker push <image>:<tag>

# Remove image
docker rmi <image>

# Remove dangling images
docker image prune

# Tag image
docker tag <source> <target>
```

### Docker Compose

```bash
# Start services
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs
docker compose logs -f <service>

# Restart services
docker compose restart

# Build services
docker compose build

# Execute in service
docker compose exec <service> <command>

# Scale services
docker compose up -d --scale <service>=<count>
```

### Network Management

```bash
# List networks
docker network ls

# Create network
docker network create <name>

# Create network with driver
docker network create -d bridge <name>

# Connect container to network
docker network connect <network> <container>

# Disconnect container
docker network disconnect <network> <container>

# Remove network
docker network rm <network>
```

### Volume Management

```bash
# List volumes
docker volume ls

# Create volume
docker volume create <name>

# Remove volume
docker volume rm <name>

# Remove unused volumes
docker volume prune
```

### System Cleanup

```bash
# Show disk usage
docker system df

# Remove unused data
docker system prune

# Remove all unused data (images, containers, volumes)
docker system prune -a --volumes
```

## Common Patterns

### Dockerfile Template

```dockerfile
# Use official base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Run command
CMD ["python", "main.py"]
```

### Docker Compose Template

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/dbname
    volumes:
      - ./data:/app/data
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Best Practices

### Dockerfile

1. **Use specific image tags** - Avoid `latest` in production
2. **Minimize layers** - Combine RUN commands with `&&`
3. **Use multi-stage builds** - Reduce final image size
4. **Leverage build cache** - Order commands from least to most frequent changes
5. **Use .dockerignore** - Exclude unnecessary files

### Security

1. **Don't run as root** - Add `USER` instruction
2. **Scan images** - Use `docker scout` or third-party tools
3. **Use secrets management** - Don't hardcode credentials
4. **Limit resources** - Use `--cpus`, `--memory`

### Performance

1. **Use alpine images** - Smaller footprint
2. **Optimize COPY order** - Leverage layer caching
3. **Use health checks** - Add `HEALTHCHECK` instruction

## Troubleshooting

### Common Issues

1. **Container won't start**
   ```bash
   # Check logs
   docker logs <container>
   
   # Check exit code
   docker inspect <container> --format='{{.State.ExitCode}}'
   ```

2. **Port already in use**
   ```bash
   # Find process using port
   lsof -i :<port>
   
   # Use different host port
   docker run -p <different_port>:<container_port> <image>
   ```

3. **Disk space issues**
   ```bash
   # Check disk usage
   docker system df
   
   # Clean up
   docker system prune -a --volumes
   ```

4. **Permission denied**
   ```bash
   # Run with user namespace
   docker run --user $(id -u):$(id -g) <image>
   
   # Or fix volume permissions
   sudo chown -R $(id -u):$(id -g) /host/path
   ```

## Examples

### Run MySQL Container

```bash
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=mydb \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  mysql:8.0
```

### Run Redis Container

```bash
docker run -d \
  --name redis \
  -p 6379:6379 \
  -v redis_data:/data \
  redis:7-alpine
```

### Run Nginx Reverse Proxy

```bash
docker run -d \
  --name nginx \
  -p 80:80 \
  -p 443:443 \
  -v ./nginx.conf:/etc/nginx/nginx.conf:ro \
  -v ./ssl:/etc/nginx/ssl:ro \
  nginx:alpine
```

## Resources

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose Specification](https://github.com/compose-spec/compose-spec)
- [Best Practices Guide](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)