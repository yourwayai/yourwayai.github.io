# YourwayAI 网站 Nexconn 在线咨询系统 — 项目总结

> 用途: 同步项目背景给 IDE (Antigravity) 及后续维护者。
> 状态: 全部上线并实测通过 (2026-10-23)。
> 网站: https://yourwayai.github.io — 仓库: https://github.com/yourwayai/yourwayai.github.io
> 网站技术栈: VitePress 1.6.4 + Vue, 纯静态 GitHub Pages (GitHub Actions 部署), 无后端、无用户体系。

## 一句话架构

静态网站本身放不了密钥, 所以系统 = 静态站前端 + 两个 Cloudflare Worker + Nexconn 云服务:

    访客浏览器
      |  1. 向 Token Worker 要访问令牌
      v
    Token Worker (Cloudflare)  — 用 App Secret 签名调 Nexconn 换 Token
      |  2. 拿 Token 直连 Nexconn 发消息
      v
    Nexconn 云 (新加坡数据中心) — 消息通道, 访客与站长 1 对 1 单聊
      |  3. 每条新消息通过 Webhook 推送给 AI Worker
      v
    AI Worker (Cloudflare) — Workers AI 生成回复, 以站长身份发回访客
      ^
    站长浏览器打开 /owner 页 — 同样经 Token Worker 拿令牌后收发消息

## 关键标识 (可公开部分)

| 项目 | 值 |
| --- | --- |
| Nexconn App Key | `uwd1c0sxum371` (前端公开值, 非机密) |
| 数据中心 | 新加坡 sg, API Host: `api.sg-light-api.com` |
| 站长 userId | `yourwayai-owner` |
| 访客 userId | 浏览器 localStorage 生成的随机 `guest-xxxxxxxx` (换浏览器即新身份) |
| Token Worker | https://nexconn-token-yourwayai.bruce-mi.workers.dev/ |
| AI Worker | https://nexconn-ai-yourwayai.bruce-mi.workers.dev/ |
| 站长收件箱 | https://yourwayai.github.io/owner (不挂导航, 靠地址访问) |
| 套餐 | Nexconn Chat 免费档 10K MAU (已通过"集成 SDK + 发 1 条消息"激活) |

机密 (App Secret、站长口令 OWNER_CODE) 只存在于 Cloudflare Worker 的机密变量中,
不进仓库、不进本文档。App Secret 一旦在 Nexconn 控制台刷新, 所有旧 Token 立即失效。

## 第一部分: Token 服务 (Cloudflare Worker)

为什么需要: Nexconn 客户端 SDK 不能自己获取 Token (官方硬约束), 必须由服务端
用 App Secret 签名调 `POST /v4/auth/access-token/issue` 换取。

- 签名算法: `SHA1(AppSecret + Nonce + Timestamp)`, 请求头带
  App-Key / Nonce / Timestamp / Signature / X-Request-ID。
- 接口: POST 请求体 `{ userId, name? }`, 返回 `{ userId, accessToken }`。
- CORS: 只允许来源 `https://yourwayai.github.io`。
- v2 安全加固: 以站长身份 `yourwayai-owner` 领 Token 时必须额外带站长口令
  (请求头或请求体的 ownerCode 字段, 与机密变量 OWNER_CODE 比对),
  防止任何人知道 Worker 地址后冒领站长身份。普通访客领令牌不需要口令。
- 所需机密/变量 (Cloudflare 后台设置): NEXCONN_APP_KEY、NEXCONN_APP_SECRET、
  OWNER_CODE (机密), NEXCONN_API_HOST、ALLOWED_ORIGIN (普通变量)。

## 第二部分: 网站访客端 (仓库内改动, commit 4dd9853 已上线)

新增/修改文件 (均在仓库 `docs/` 目录下):

- `docs/.vitepress/theme/NexconnChat.vue` (新增): 右下角浮动「💬 咨询」按钮与聊天面板。
  逻辑: 从 localStorage 读/建访客 ID, 向 Token Worker 领 Token,
  Engine 初始化一次后 connect, 与站长建 Direct Channel (单聊) 收发文本消息。
- `docs/.vitepress/theme/OwnerChat.vue` (新增): 站长收件箱组件 (见第三部分)。
- `docs/.vitepress/theme/MyLayout.vue` (修改): 在 layout 的 layout-bottom 插槽挂载 NexconnChat。
- `docs/owner.md` (新增): 站长页路由 /owner, 只渲染 OwnerChat, 不挂导航菜单。
- `docs/.env` (新增): 前端环境变量 (VitePress 只读 docs/ 下的 .env, 放仓库根读不到):
  - `VITE_NEXCONN_APP_KEY=uwd1c0sxum371`
  - `VITE_NEXCONN_TOKEN_API=https://nexconn-token-yourwayai.bruce-mi.workers.dev/`
  - `VITE_NEXCONN_OWNER_ID=yourwayai-owner`
- `package.json` (修改): 新增依赖 `@nexconn/chat` ^26.2.1、`@nexconn/engine` ^26.2.1。

已验证: GitHub Actions 构建部署成功, 线上首页出现咨询按钮, 访客可与站长双向发消息。

## 第三部分: 站长收件箱 (/owner 页)

- 打开页面时先要求输入站长口令 (只存浏览器 sessionStorage, 页面关掉即清),
  拿口令向 Token Worker 换站长 Token 后登录。
- 功能: 会话列表 (createChannelsQuery 查 DIRECT 频道, 显示对方 ID、最后消息、未读数徽标),
  点开会话看历史 (createMessagesQuery), 底部输入框直接回复访客。
- 局限: 只有页面打开时才实时收消息; 离线期间的留言在下次登录时以未读形式出现
  (Nexconn 云端保留消息历史 180 天, 不会丢)。

## 第四部分: AI 自动回复 (AI Worker, 2026-10-23 上线实测通过)

链路: Nexconn Webhook (事件 message:send) → AI Worker 验签 → Workers AI 生成
→ Server API 以站长身份发回。访客感知: 站长不在线时 AI 先接待。

- Webhook 配置位置: Nexconn 控制台 Chat → Chat settings → Webhooks,
  URL 指向 AI Worker, 只订阅 `message:send` 一个事件。
- Webhook 要点 (官方文档): POST JSON, 信封格式 `{ type, id, time, data: [...] }`;
  单聊消息在 data[0] 里, content 是 JSON 字符串 (形如 {"content": "你好"});
  channelType 1 = 单聊; 请求头带 AppKey/Nonce/Timestamp/Signature,
  验签公式同 Token 签名; 投递超时 5 秒、失败重试 2 次, 所以 Worker 必须先回 200,
  真正的 AI 调用放 ctx.waitUntil 后台执行。
- 发回复接口: `POST https://api.sg-light-api.com/v4/direct-channel/message/send`,
  请求体 fromUserId=站长 ID、toUserIds=[访客 ID]、messageType=RC:TxtMsg、
  content 为 JSON 字符串。关键参数 isEchoToSender 必须为 1,
  否则服务端发的消息不存入站长一侧历史, 站长页看不到 AI 的回复 (踩过此坑)。
- AI 模型: Cloudflare Workers AI 的 `@cf/qwen/qwen3-30b-a3b-fp8` (中文较好),
  通过名为 AI 的 Workers AI 绑定调用, 无需任何外部 API Key, 用 Cloudflare 免费额度。
  可用变量 AI_MODEL 换模型。
- AI 人设 (代码里 SYSTEM_PROMPT 常量): YourwayAI 开源导航站助手, 站长 Bruce;
  只答与网站收录的开源工具、求职陪跑服务有关的问题; 不编造价格与承诺;
  不确定就说已记下、站长会回复; 回复简短 (150 字内)。
- 身份标识: 每条 AI 回复由代码强制加前缀 `AI助手：`, 不冒充站长真人。
- 防循环护栏 (handleEvent 过滤, 缺一不可):
  只处理 channelType=1 的单聊、messageType=RC:TxtMsg 文本、接收方是站长、
  发送方以 guest- 开头、且 os 不为 Server (服务端发的消息含 AI 自己的回复, 一律忽略)。
- 可选 KV 绑定 AI_STATE: 绑定后启用 Webhook 事件去重 (防重试重复回复)
  与每访客每天最多 30 条 AI 回复上限 (超限只提示一次转人工)。没绑也能跑, 只是无限流。
- AI Worker 所需机密/变量: NEXCONN_APP_KEY、NEXCONN_APP_SECRET (机密),
  NEXCONN_API_HOST (普通变量); 绑定: AI (必需)、AI_STATE (可选)。

## 运维速查

- 改 AI 人设/知识: 改 AI Worker 代码顶部 SYSTEM_PROMPT, 在 Cloudflare 后台重新部署。
- 改访客端文案 (欢迎语等): 改 NexconnChat.vue 后 git push, Actions 自动部署。
- 站长口令忘了/要改: 改 Token Worker 的机密变量 OWNER_CODE, 重新部署即生效。
- App Secret 泄漏: Nexconn 控制台刷新 Secret, 然后同步更新两个 Worker 的机密变量。
- 排查连接问题: 先分别测两个 Worker — Token Worker POST 一个测试 userId 应返回
  accessToken; AI Worker GET 应返回 "AI webhook ok"。访客端卡「连接中」多为
  浏览器页面连接挂死, 关页重开即可。
- 消息数据在 Nexconn 云端 (新加坡), 本地与仓库都不存聊天记录。

## 还没做的可选项 (未立项)

- 访客首次打开时的自动欢迎语 (目前只有面板内静态提示文字)。
- 站长离线时有新留言的外部通知 (邮件/推送)。
- 给 AI 喂全站文章内容做知识库, 让它能答具体的工具细节问题。
