# Chatwoot

<p align="center">
  <img src="https://opengraph.githubassets.com/1/chatwoot/chatwoot" alt="chatwoot Preview" style="border-radius: 8px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">
</p>

**Chatwoot** 是一款现代化、开源且支持自托管的客户支持平台。它旨在全方位升级您的客服体验，是 Intercom、Zendesk 和 Salesforce Service Cloud 等昂贵商业软件的完美开源替代品。

## 📊 项目信息
* **GitHub**: [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)
* **官方主页**: [https://www.chatwoot.com](https://www.chatwoot.com)
* **星标数**: ⭐ 28k+
* **主要语言**: 🏷️ Ruby, Vue
* **开源协议**: ⚖️ MIT / 商业双授权

---

## ✨ 核心特性

我为您深度总结了 Chatwoot 强大的企业级功能：

#### 💬 真正的全渠道服务台 (Omnichannel)
将所有客户对话集中到一个强大的收件箱中，无论客户从哪里来：
- 支持**网站实时聊天 (Live Chat)**
- 深度集成**社交媒体**：WhatsApp、Facebook、Instagram、Twitter、Telegram、Line、SMS 和传统的 Email。

#### 🤖 专属 AI 客服助理 (Captain)
内置 AI 助手帮您分担压力：
- **自动回复**：处理常见问题，给客户秒回体验。
- **降本增效**：减少人工客服的工作量，让人力聚焦在更复杂的退换货和客诉沟通上。

#### 📚 知识库与自助服务
内置完整的 Help Center 门户站点：
- 支持发布帮助文档、FAQ 和操作指南。
- 让客户“自助排障”，大幅降低工单量。

#### 🤝 极致的团队协作效能
- **内部沟通**：支持私密备注 (Private Notes) 和 `@成员`。
- **智能化分配**：可根据客服状态自动分发对话 (Auto-Assignment)。
- **快捷操作**：支持快捷键、命令面板 (Command Bar) 以及快捷回复短语 (Canned Responses)。

#### 🔌 丰富的生态集成
您可以将它无缝嵌入到现有的工作流中：
- 在 **Slack** 里直接回复客服消息。
- 绑定 **Dialogflow** 实现复杂聊天机器人。
- 接入 **Shopify** 直接在对话窗中查看客户订单！

---

## 🚀 Docker 快速部署

如果您想快速体验，建议使用官方的 `docker-compose.yaml` 进行一键自建服务：

```yaml
version: '3'
services:
  chatwoot:
    image: chatwoot/chatwoot:latest
    env_file: .env # 注意：您需要配置官方要求的环境变量文件
    ports:
      - "3000:3000"
    volumes:
      - chatwoot_data:/app/storage
volumes:
  chatwoot_data:
```

*(温馨提示：生产环境部署请务必参考[官方环境配置文档](https://www.chatwoot.com/docs/environment-variables) 设置正确的 Redis、Postgres 和环境变量。)*
