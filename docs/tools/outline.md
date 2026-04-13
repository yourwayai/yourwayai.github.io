# Outline

**Outline** 是一个现代化的自托管 Wiki 和团队知识库，设计非常优雅，是 Notion 的完美开源替代品。

## 🌟 核心特色
* **实时协作**：支持多人同时在线编辑文档。
* **Markdown 支持**：原生支持 Markdown 快捷键。
* **层级管理**：可以像书本一样将文档嵌套分类。

## 🚀 Docker 快速部署

你可以使用以下 `docker-compose.yml` 文件一键启动：

```yaml
version: '3'
services:
  outline:
    image: outlinewiki/outline
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```
