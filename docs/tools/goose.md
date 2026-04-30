---
title: Goose
description: "Block 出品的开源 AI Agent：不只是代码补全，而是能在你的机器上自主完成安装、执行、编辑和测试全流程的智能助手。"
category: '👨‍💻 开发者工具'
date: '2026-04-28T22:46:02+08:00'
---
# Goose：你的本地原生开源 AI Agent

![Goose OpenGraph Image](https://opengraph.githubassets.com/1/aaif-goose/goose)

**Goose** 是由 Block（Square 母公司）开发、现已捐赠给 Linux 基金会旗下 **Agentic AI Foundation (AAIF)** 的开源 AI Agent。与仅提供代码补全的传统 AI 工具不同，Goose 是一个真正运行在你本地机器上的**通用 AI 执行代理**——它可以安装软件、执行脚本、修改文件、运行测试，并自主完成复杂的多步骤任务。

* **GitHub Repo**: [aaif-goose/goose](https://github.com/aaif-goose/goose)
* **Star 数**: ⭐ 43,500+
* **官方主页**: [https://goose-docs.ai](https://goose-docs.ai)
* **核心语言**: Rust (49%) / TypeScript (45%)
* **开源协议**: Apache License 2.0

---

## ✨ 核心特性

### 1. 超越代码建议——真正的任务执行
Goose 不是 Copilot 式的代码补全工具。它拥有**完整的本地操作权限**：
- 🔧 安装依赖包和开发工具
- 📝 创建、编辑和重构代码文件
- 🧪 自动运行测试并根据结果迭代修复
- 🔍 搜索文档、分析 issue、浏览网页
- 📊 处理数据分析、写作、研究等非编程任务

### 2. 支持 15+ 大模型提供商
Goose 是真正的模型无关 Agent，内置支持：
- **主流商业模型**: Anthropic Claude、OpenAI GPT、Google Gemini
- **自托管模型**: Ollama（本地离线运行）
- **云服务**: OpenRouter、Azure OpenAI、AWS Bedrock
- **ACP 协议**: 复用已有的 Claude、ChatGPT 或 Gemini 订阅

无需绑定单一厂商，随时切换最适合当前任务的模型。

### 3. 70+ 扩展（MCP 生态）
Goose 通过 **Model Context Protocol (MCP)** 连接外部工具，内置 70+ 扩展，包括：
- 浏览器自动化（Playwright/Puppeteer）
- 数据库查询（SQLite、PostgreSQL）
- GitHub / GitLab 操作
- Slack、Notion、Google Workspace 集成
- 自定义扩展（任何人都可以为 Goose 开发插件）

### 4. 三种交互形式
| 形式 | 适用场景 |
|------|----------|
| **桌面 App** | macOS/Linux/Windows 图形界面，类 Claude.ai 体验 |
| **CLI** | 终端工作流、脚本集成、服务器环境 |
| **API** | 嵌入自有应用、自动化流水线 |

### 5. Recipes（可复用工作流）
Goose 支持将常用任务封装为 **Recipe**（YAML 配置文件），团队可以共享和复用标准化的 AI 工作流，大幅提升组织效率。

---

## 🚀 快速安装

```bash
# macOS / Linux（一键安装 CLI）
curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash

# 桌面 App（含 GUI 界面）
# 访问：https://goose-docs.ai/docs/getting-started/installation
# 支持 macOS、Linux、Windows
```

---

## 💻 使用示例

```bash
# 启动交互式 CLI 会话
goose session

# 让 Goose 帮你 debug 一个项目
goose run "分析 ./src 目录下的代码，找出可能导致内存泄漏的地方并修复"

# 执行 Recipe 工作流
goose run --recipe code-review.yaml

# 指定使用特定模型
goose session --provider anthropic --model claude-opus-4
```

---

## 🔌 与其他 AI 工具的对比

| 特性 | Goose | GitHub Copilot | Cursor |
|------|-------|----------------|--------|
| 本地任务执行 | ✅ 完整支持 | ❌ 仅建议 | 部分 |
| 多模型支持 | ✅ 15+ 提供商 | ❌ 仅 OpenAI | 部分 |
| MCP 扩展生态 | ✅ 70+ | ❌ | 有限 |
| 开源 | ✅ Apache 2.0 | ❌ | ❌ |
| 本地/离线运行 | ✅（配合 Ollama）| ❌ | ❌ |
| 非编程任务 | ✅ 通用 Agent | ❌ 仅编程 | 仅编程 |

---

## 🏛️ 项目背景

Goose 最初由 Block（Jack Dorsey 创立的金融科技公司）内部团队构建用于工程师日常开发提效。2025 年，Block 将该项目捐赠给 **Linux 基金会**旗下的 Agentic AI Foundation，成为首批加入该基金会的核心项目之一，彰显了开源社区对通用 AI Agent 标准化的重视。

---

## 💡 适用场景与总结

Goose 最适合希望将 AI 真正融入工程工作流的开发者。它不只是一个"聊天助手"，而是一个可以**自主完成端到端任务**的本地代理——从读 issue 到写代码、跑测试、提 PR，整个链路都可以交给 Goose 自动完成。对于想要 Cursor/Copilot 之外更强大自主性的工程师来说，Goose 是目前开源生态中最值得关注的选项。
