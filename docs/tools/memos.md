---
title: Memos
description: 轻量级的碎片化知识管理工具，轻松记录每一次灵感闪现。
icon: '📝'
category: '效率与生产力 (Productivity)'
---
# Memos

**Memos** 是一个开源、自托管的碎片化笔记，它能帮助您像发微博、发朋友圈一样记录您的灵感、想法和待办事项。

## 🌟 核心特色
* **纯碎碎念体验**：为您提供最纯粹的记录环境，无干扰，专注于想法本身。
* **Markdown 增强**：支持表格、列表、代办事项等 Markdown 语法。
* **数据主权**：所有数据均存储在本地 SQLite 数据库中，完全由您控制。
* **多端支持**：拥有优雅的 Web 界面，以及成熟的第三方 APP 和插件。

## 🚀 Docker 快速部署

使用以下命令或 `docker-compose.yml` 即可快速启动：

```yaml
version: "3"
services:
  memos:
    image: neosmemo/memos:latest
    container_name: memos
    ports:
      - "5230:5230"
    volumes:
      - ~/.memos/:/var/opt/memos
```
