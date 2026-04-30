---
title: RSSHub
description: 🧡 万物皆可 RSS，一个开源、容易使用、易于扩展的 RSS 生成器
category: '👨‍💻 开发者工具'
date: '2026-04-30T23:02:07+08:00'
---
# RSSHub：万物皆可 RSS

![RSSHub OpenGraph Image](https://opengraph.githubassets.com/1/DIYgod/RSSHub)

**RSSHub** 是一个开源、易于使用且易于扩展的 RSS 生成器。它可以给任何奇奇怪怪的内容生成 RSS 订阅源，让使用者能够在各类 RSS 阅读器中追踪不支持 RSS 的网站更新。结合 RSSHub Radar 等生态工具，它可以极大提升信息获取的效率和体验。

* **GitHub Repo**: [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub)
* **Star 数**: ⭐ 43,700+
* **官方主页**: [https://docs.rsshub.app](https://docs.rsshub.app)
* **核心语言**: TypeScript
* **开源协议**: MIT License

---

## ✨ 核心特性

### 1. 海量路由支持
RSSHub 目前已经支持了上千个网站的 RSS 订阅路由，涵盖：
- **社交媒体**: 微博、Twitter、即刻、小红书、Instagram、Bilibili 等动态。
- **资讯平台**: 微信公众号、知乎、少数派、V2EX 等文章更新。
- **播客/视频**: YouTube、各类播客平台的更新提醒。
- **其他**: 甚至包括天气预报、大学通知、快递状态等。

### 2. 高度可定制与易于扩展
RSSHub 采用极简的路由设计，如果你想要的网站尚未被支持，只需编写数十行 JavaScript 代码，即可轻松为其编写一个新的 RSS 路由。社区每天都有大量贡献者提交新的路由。

### 3. 完善的生态系统
- **RSSHub Radar**: 浏览器扩展，一键发现当前网站支持的 RSS 和 RSSHub 订阅源。
- **Folo**: 专为现代阅读流和 RSSHub 优化的 AI RSS 阅读器。
- **多平台支持**: 配合各类 RSS 阅读器（如 Reeder、NetNewsWire、Miniflux）使用，打造完美的信息流。

---

## 🚀 快速部署

虽然你可以使用官方提供的公共实例，但为了稳定性和速度，强烈建议使用 Docker 自建私有实例。

```bash
# 获取 docker-compose.yml
wget https://raw.githubusercontent.com/DIYgod/RSSHub/master/docker-compose.yml

# 启动容器
docker-compose up -d
```
启动后，默认监听 `1200` 端口。你可以通过 `http://<你的IP>:1200` 访问。

---

## 💻 使用示例

一旦 RSSHub 运行起来，你只需在基础 URL 后拼接特定的路由路径即可获取 RSS 源。例如：

- **B站 UP 主动态**: `/bilibili/user/dynamic/:uid` -> `http://localhost:1200/bilibili/user/dynamic/2267573`
- **知乎热榜**: `/zhihu/hotlist` -> `http://localhost:1200/zhihu/hotlist`
- **微博博主**: `/weibo/user/:uid` -> `http://localhost:1200/weibo/user/1191258123`

---

## 🔌 为什么需要 RSSHub？

在算法推荐和信息孤岛日益严重的今天，平台倾向于将用户圈禁在自己的 App 内，导致优质信息的获取成本变得极高。RSSHub 就像一座桥梁，打破了这些信息孤岛，把主动权交还给用户。

| 方式 | 算法推荐 Feed 流 | 使用 RSSHub + 阅读器 |
|------|------------------|----------------------|
| **控制权** | 平台决定你读什么 | 你决定订阅和阅读什么 |
| **隐私** | 收集你的浏览偏好 | 你的阅读数据完全私有 |
| **干扰** | 充满广告和无效信息| 纯净的阅读体验，无干扰 |
| **效率** | 需要打开几十个 App | 在一个阅读器里看天下事 |

---

## 💡 适用场景与总结

RSSHub 适合每一位患有“信息焦虑症”、希望重新掌控自己信息流的高级用户、研究员和开发者。它是现代 RSS 复兴运动的核心基础设施。配合 Docker 轻松自建后，你将拥有一个不受限制的超级信息聚合引擎。
