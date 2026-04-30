---
title: Penpot
description: "开源设计协作平台：专为设计师与开发者团队打造，彻底替代 Figma 的自托管设计工具。"
category: '👨‍💻 开发者工具'
date: '2026-04-28T22:45:40+08:00'
---
# Penpot：设计与代码协同的开源平台

![Penpot OpenGraph Image](https://opengraph.githubassets.com/1/penpot/penpot)

**Penpot** 是面向专业团队的开源设计与原型平台，由西班牙公司 Kaleidos 开发。凭借对 SVG、CSS、HTML 和 JSON 等开放标准的原生支持，Penpot 打破了设计与开发之间的信息壁垒——设计稿本身就是代码可读的结构，让产品真正实现所见即所得的交付。

* **GitHub Repo**: [penpot/penpot](https://github.com/penpot/penpot)
* **Star 数**: ⭐ 47,000+
* **官方主页**: [https://penpot.app](https://penpot.app)
* **核心语言**: Clojure (75%) / JavaScript / Rust
* **开源协议**: Mozilla Public License 2.0

---

## ✨ 核心特性

### 1. 以代码为核心的设计理念
Penpot 的最大差异点：**设计即代码**。所有设计元素基于 SVG 标准构建，开发者可在 Inspect 模式下直接获取 SVG、CSS 和 HTML 代码，无需任何格式转换，大幅缩短设计到上线的周期。

### 2. 原生 Design Tokens 支持
Penpot 内置行业级 **Design Tokens** 系统，提供设计与开发之间的单一真相来源（Single Source of Truth）。颜色、间距、字体等 Token 可统一管理，确保跨平台、跨项目的视觉一致性，轻松应对复杂的设计系统维护场景。

### 3. MCP Server 与 AI 工作流集成
2024 年发布的 **Penpot MCP Server** 将设计工作流引入 AI 时代。开发者和 AI Agent 可通过标准化协议直接读写设计文件，实现设计稿的自动生成、批量修改与 AI 驱动的工作流自动化。

### 4. CSS Grid & Flex 响应式布局
Penpot 原生支持 **CSS Grid 和 Flexbox 布局**，让设计师在画布上直接定义真实的响应式行为，而非简单地拖拽固定元素，大幅提升设计稿对开发工作的参考价值。

### 5. 实时协同编辑
支持多人通过 WebSocket 在同一画布上**实时协作**，内置完整的团队权限管理体系，适合从小型创业团队到企业级组织的各种协作规模。

### 6. 强大的插件生态
Penpot Hub 提供丰富的第三方插件，支持与外部应用集成。开放的 Webhook 和 REST API 使其可以无缝嵌入企业现有的 CI/CD 和开发工具链。

---

## 🚀 快速部署（Docker）

Penpot 官方提供完整的 Docker Compose 配置，最快 5 分钟即可完成私有化部署：

```bash
# 下载官方 docker-compose 配置
curl -o docker-compose.yml https://raw.githubusercontent.com/penpot/penpot/main/docker/images/docker-compose.yaml

# 启动所有服务（后端、前端、Exporter、数据库）
docker compose -p penpot -f docker-compose.yml up -d
```

默认访问地址：`http://localhost:9001`

> 也支持 Kubernetes、Elestio 等多种部署方式，详见[官方文档](https://penpot.app/self-host)。

---

## 🆚 与 Figma 的核心差异

| 特性 | Penpot | Figma |
|------|--------|-------|
| 开源自托管 | ✅ 完全支持 | ❌ 仅 SaaS |
| 数据所有权 | ✅ 完全掌控 | ❌ 存储在 Adobe 服务器 |
| 设计 Token | ✅ 原生内置 | 需第三方插件 |
| 文件格式 | SVG（开放标准）| 专有格式 |
| MCP / AI 集成 | ✅ 官方支持 | 有限支持 |
| 定价 | 免费开源 | 高昂订阅费 |

---

## 💡 适用场景与总结

Penpot 特别适合以下团队：
- **注重数据主权**的企业，需要将设计资产保存在自有服务器上；
- **设计-开发一体化**的全栈团队，希望减少设计稿与代码之间的转译成本；
- **构建大型设计系统**的平台团队，需要强大的 Design Token 和组件变体管理能力；
- 已受够 Figma 高价订阅费的**中小型团队**。

> "Penpot connects design, code, and AI workflows through a code-based approach, making designs readable by developers and AI via the MCP server."
