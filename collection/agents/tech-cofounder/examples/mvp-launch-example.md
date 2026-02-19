# Tech Co-Founder Agent - MVP Launch Example

## User Request

```
我需要快速构建一个 MVP 产品：AI 写作助手。

目标用户：内容创作者、自媒体、小团队
核心功能：
1. AI 文本生成（文章、社媒文案）
2. 文本优化（改写、扩写、缩写）
3. SEO 优化建议
4. 多平台发布（微信公众号、小红书、抖音）

技术约束：
- 快速上线（2周内）
- 低成本
- 易于迭代

请帮我：
1. 设计产品架构
2. 选择技术栈
3. 实现 MVP 功能
4. 部署上线
```

## Agent Response

### Phase A - Plan-to-Build Brief

**Scope:**
- AI 写作助手 MVP
- 核心：文本生成、优化、SEO
- 平台：Web 应用 + 浏览器扩展
- 部署：Serverless (降低成本)

**Assumptions:**
- 使用 Claude API (高质量文本生成)
- 数据库：PostgreSQL (Supabase)
- 前端：Next.js (快速开发)
- 认证：Supabase Auth
- 支付：微信支付 + Stripe

**Timeline:**
- Week 1: 核心功能开发
- Week 2: 集成测试 + 上线

**Build Checklist:**
1. 项目初始化
2. 数据库设计
3. API 集成（Claude）
4. 核心功能实现
5. UI/UX 设计
6. 部署配置

### Phase B - Implement

#### Stage 1: 项目结构

```
ai-writer/
├── apps/
│   ├── web/                    # Next.js Web 应用
│   │   ├── app/
│   │   │   ├── (auth)/         # 认证页面
│   │   │   ├── dashboard/      # 仪表板
│   │   │   ├── write/          # 写作界面
│   │   │   └── api/            # API Routes
│   │   ├── components/
│   │   │   ├── ui/             # UI 组件
│   │   │   ├── editor/         # 编辑器组件
│   │   │   └── templates/      # 模板组件
│   │   └── lib/
│   │       ├── supabase.ts     # Supabase 客户端
│   │       ├── claude.ts       # Claude API
│   │       └── utils.ts
│   │
│   └── extension/              # 浏览器扩展
│       ├── popup/
│       ├── content/
│       └── background/
│
├── packages/
│   ├── shared/                 # 共享代码
│   │   ├── types/
│   │   └── utils/
│   └── config/                 # 配置
│
├── supabase/
│   ├── migrations/
│   └── functions/
│
└── docker-compose.yml
```

#### Stage 2: 数据库设计

**Supabase Schema:**

```sql
-- 用户表（Supabase Auth 扩展）
create table public.profiles (
  id uuid references auth.users not null primary key,
  email text,
  full_name text,
  avatar_url text,
  plan text default 'free',  -- free, pro, team
  credits_remaining integer default 100,
  created_at timestamp with time zone default timezone('utc'::text, now())
);

-- 文档表
create table public.documents (
  id uuid default uuid_generate_v4() primary key,
  user_id uuid references public.profiles(id) not null,
  title text not null,
  content text,
  type text default 'article',  -- article, social, email, etc.
  status text default 'draft',  -- draft, published, archived
  word_count integer default 0,
  seo_score jsonb,
  created_at timestamp with time zone default timezone('utc'::text, now()),
  updated_at timestamp with time zone default timezone('utc'::text, now())
);

-- 模板表
create table public.templates (
  id uuid default uuid_generate_v4() primary key,
  name text not null,
  description text,
  category text,
  prompt_template text not null,
  variables jsonb,
  is_public boolean default true,
  created_by uuid references public.profiles(id),
  usage_count integer default 0
);

-- 生成历史
create table public.generations (
  id uuid default uuid_generate_v4() primary key,
  user_id uuid references public.profiles(id) not null,
  document_id uuid references public.documents(id),
  prompt text,
  response text,
  model text default 'claude-3-5-sonnet',
  tokens_used integer,
  cost decimal(10, 4),
  created_at timestamp with time zone default timezone('utc'::text, now())
);

-- RLS 策略
alter table public.profiles enable row level security;
alter table public.documents enable row level security;

create policy "Users can view own profile" on public.profiles
  for select using (auth.uid() = id);

create policy "Users can update own profile" on public.profiles
  for update using (auth.uid() = id);

create policy "Users can view own documents" on public.documents
  for select using (auth.uid() = user_id);

create policy "Users can insert own documents" on public.documents
  for insert with check (auth.uid() = user_id);

create policy "Users can update own documents" on public.documents
  for update using (auth.uid() = user_id);

-- 索引
create index idx_documents_user_id on public.documents(user_id);
create index idx_documents_status on public.documents(status);
create index idx_generations_user_id on public.generations(user_id);
```

#### Stage 3: API 实现

**Claude API 集成:**

```typescript
// apps/web/lib/claude.ts
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

export interface GenerationOptions {
  prompt: string;
  maxTokens?: number;
  temperature?: number;
  model?: string;
}

export interface GenerationResult {
  text: string;
  tokensUsed: number;
  cost: number;
}

export async function generateText(
  options: GenerationOptions
): Promise<GenerationResult> {
  const {
    prompt,
    maxTokens = 4096,
    temperature = 0.7,
    model = 'claude-3-5-sonnet-20241022',
  } = options;

  const message = await anthropic.messages.create({
    model,
    max_tokens: maxTokens,
    temperature,
    system: `你是一个专业的写作助手，擅长创作各种类型的内容。

写作风格：
- 简洁明了，易于阅读
- 符合中文表达习惯
- 适当使用修辞手法增强表达
- 考虑 SEO 优化

请根据用户需求生成高质量内容。`,
    messages: [
      {
        role: 'user',
        content: prompt,
      },
    ],
  });

  const text = message.content[0].type === 'text' ? message.content[0].text : '';
  const tokensUsed = message.usage.input_tokens + message.usage.output_tokens;

  // Claude Sonnet 定价
  const inputCost = (tokensUsed / 1000) * 0.003;
  const outputCost = (message.usage.output_tokens / 1000) * 0.015;
  const cost = inputCost + outputCost;

  return { text, tokensUsed, cost };
}

// 专门的功能函数
export async function generateArticle(params: {
  topic: string;
  keywords: string[];
  length?: 'short' | 'medium' | 'long';
  tone?: 'professional' | 'casual' | 'friendly';
}) {
  const { topic, keywords, length = 'medium', tone = 'professional' } = params;

  const prompt = `请写一篇关于"${topic}"的文章。

要求：
- 长度：${length === 'short' ? '500-800字' : length === 'long' ? '2000-3000字' : '1000-1500字'}
- 语气：${tone === 'professional' ? '专业正式' : tone === 'casual' ? '轻松随意' : '友好亲切'}
- 融入关键词：${keywords.join('、')}
- 结构清晰，有引言、正文、结论
- 适合 SEO 优化`;

  return generateText({ prompt, maxTokens: length === 'long' ? 4096 : 2048 });
}

export async function optimizeText(params: {
  text: string;
  goal: 'rewrite' | 'expand' | 'shorten' | 'seo';
}) {
  const { text, goal } = params;

  const prompts = {
    rewrite: `请改写以下文本，保持原意但用不同的表达方式：\n\n${text}`,
    expand: `请扩写以下文本，增加更多细节和例子：\n\n${text}`,
    shorten: `请精简以下文本，保留核心信息：\n\n${text}`,
    seo: `请优化以下文本，使其更符合 SEO 要求，提高搜索排名：\n\n${text}`,
  };

  return generateText({ prompt: prompts[goal] });
}

export async function generateSocialMedia(params: {
  content: string;
  platforms: ('wechat' | 'xiaohongshu' | 'douyin')[];
}) {
  const { content, platforms } = params;

  const platformSpecs = {
    wechat: {
      name: '微信公众号',
      style: '正式、深度、排版精美',
      length: '800-2000字',
      emoji: '适当使用',
    },
    xiaohongshu: {
      name: '小红书',
      style: '轻松、种草、带表情',
      length: '300-800字',
      emoji: '大量使用',
    },
    douyin: {
      name: '抖音',
      style: '口语化、有冲击力',
      length: '100-300字（口播稿）',
      emoji: '适度使用',
    },
  };

  const prompt = `请根据以下内容，为 ${platforms.map(p => platformSpecs[p].name).join('、')} 生成适配的文案：

原文内容：
${content}

要求：
${platforms.map(p => `
${platformSpecs[p].name}：
- 风格：${platformSpecs[p].style}
- 长度：${platformSpecs[p].length}
- 表情：${platformSpecs[p].emoji}
`).join('\n')}`;

  return generateText({ prompt });
}

export async function analyzeSEO(text: string) {
  const prompt = `请分析以下文本的 SEO 情况，给出优化建议：

文本内容：
${text}

请分析：
1. 关键词密度和使用情况
2. 标题和结构
3. 可读性
4. 内链建议
5. 元标签建议

以 JSON 格式返回分析结果。`;

  return generateText({ prompt });
}
```

#### Stage 4: UI 组件

**写作界面:**

```typescript
// apps/web/components/editor/WriterEditor.tsx
'use client';

import { useState, useReducer } from 'react';
import { generateText, optimizeText, generateSocialMedia } from '@/lib/claude';
import { createClient } from '@/lib/supabase';

interface WriterEditorProps {
  documentId?: string;
}

type GenerationState =
  | { status: 'idle' }
  | { status: 'generating'; progress?: number }
  | { status: 'success'; result: string }
  | { status: 'error'; error: string };

export function WriterEditor({ documentId }: WriterEditorProps) {
  const [content, setContent] = useState('');
  const [generated, setGenerated] = useState('');
  const [state, dispatch] = useReducer(
    (state: GenerationState, action: GenerationState) => action,
    { status: 'idle' }
  );

  const supabase = createClient();

  const handleGenerate = async (prompt: string, options?: GenerationOptions) => {
    dispatch({ status: 'generating' });

    try {
      const result = await generateText({
        prompt,
        ...options,
      });

      setGenerated(result.text);
      dispatch({ status: 'success', result: result.text });

      // 保存到数据库
      await supabase.from('generations').insert({
        prompt,
        response: result.text,
        tokens_used: result.tokensUsed,
        cost: result.cost,
      });
    } catch (error) {
      dispatch({ status: 'error', error: (error as Error).message });
    }
  };

  const handleOptimize = async (goal: 'rewrite' | 'expand' | 'shorten' | 'seo') => {
    if (!generated) return;

    dispatch({ status: 'generating' });

    try {
      const result = await optimizeText({
        text: generated,
        goal,
      });

      setGenerated(result.text);
      dispatch({ status: 'success', result: result.text });
    } catch (error) {
      dispatch({ status: 'error', error: (error as Error).message });
    }
  };

  return (
    <div className="flex h-full">
      {/* 左侧：输入区域 */}
      <div className="w-1/2 p-4 border-r">
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="输入你的写作要求或原始内容..."
          className="w-full h-full resize-none focus:outline-none"
        />

        {/* 操作按钮 */}
        <div className="mt-4 flex gap-2">
          <button
            onClick={() => handleGenerate(content)}
            disabled={state.status === 'generating'}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50"
          >
            {state.status === 'generating' ? '生成中...' : '生成内容'}
          </button>

          <select
            onChange={(e) => {
              if (generated) {
                handleOptimize(e.target.value as any);
              }
            }}
            disabled={!generated || state.status === 'generating'}
            className="px-4 py-2 border rounded disabled:opacity-50"
          >
            <option value="">优化选项...</option>
            <option value="rewrite">改写</option>
            <option value="expand">扩写</option>
            <option value="shorten">缩写</option>
            <option value="seo">SEO 优化</option>
          </select>
        </div>
      </div>

      {/* 右侧：输出区域 */}
      <div className="w-1/2 p-4">
        {state.status === 'generating' && (
          <div className="flex items-center justify-center h-full">
            <div className="text-center">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4" />
              <p>AI 正在创作中...</p>
            </div>
          </div>
        )}

        {state.status === 'success' && (
          <div className="h-full">
            <textarea
              value={generated}
              onChange={(e) => setGenerated(e.target.value)}
              className="w-full h-full resize-none focus:outline-none"
            />
            <div className="mt-2 text-sm text-gray-500">
              字数：{generated.length} | 约 {Math.ceil(generated.length / 400)} 分钟阅读
            </div>
          </div>
        )}

        {state.status === 'error' && (
          <div className="flex items-center justify-center h-full">
            <div className="text-center text-red-500">
              <p>生成失败：{(state as any).error}</p>
              <button
                onClick={() => dispatch({ status: 'idle' })}
                className="mt-4 px-4 py-2 border rounded"
              >
                重试
              </button>
            </div>
          </div>
        )}

        {state.status === 'idle' && (
          <div className="flex items-center justify-center h-full text-gray-400">
            <p>生成的内容将显示在这里</p>
          </div>
        )}
      </div>
    </div>
  );
}
```

#### Stage 5: 部署配置

**Vercel 部署:**

```bash
# vercel.json
{
  "buildCommand": "turbo run build",
  "outputDirectory": "apps/web/.next",
  "installCommand": "pnpm install",
  "framework": "nextjs",
  "regions": ["hkg1"],
  "env": {
    "NEXT_PUBLIC_SUPABASE_URL": "@supabase-url",
    "NEXT_PUBLIC_SUPABASE_ANON_KEY": "@supabase-anon-key",
    "ANTHROPIC_API_KEY": "@anthropic-api-key"
  }
}
```

**Supabase 配置:**

```bash
# 设置环境变量
supabase secrets set ANTHROPIC_API_KEY=your-key-here

# 推送迁移
supabase db push

# 部署边缘函数
supabase functions deploy
```

---

## Deliverables

1. ✅ 完整的项目结构
2. ✅ 数据库设计和迁移
3. ✅ Claude API 集成
4. ✅ 核心功能实现
5. ✅ UI 组件
6. ✅ 部署配置

## Launch Checklist

- [ ] Supabase 项目创建
- [ ] 环境变量配置
- [ ] 数据库迁移执行
- [ ] Vercel 部署
- [ ] 域名配置
- [ ] 支付集成（微信支付 + Stripe）
- [ ] 监控设置（Sentry）
- [ ] 分析工具（Google Analytics）

## Next Steps

1. **Week 1:**
   - 完成核心功能开发
   - 内部测试

2. **Week 2:**
   - Beta 测试
   - Bug 修复
   - 正式上线

## V2 Features

- AI 图片生成（配图）
- 多人协作
- 版本历史
- 更多平台支持
- API 开放平台
