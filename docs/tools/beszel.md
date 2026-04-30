---
title: beszel
description: 轻量级、极简的服务器和 Docker 容器监控面板，带历史数据与告警。
category: '👨‍💻 开发者工具'
date: '2026-04-30T22:59:04+08:00'
---
# beszel：轻巧优雅的服务器状态监控面板

![beszel OpenGraph Image](https://opengraph.githubassets.com/1/henrygd/beszel)

**beszel** 是一款轻量级的服务器监控系统，专为那些认为传统监控方案（如 Prometheus + Grafana）过于沉重和复杂的开发者设计。它提供了一个现代化的 Web UI，支持多用户管理，不仅可以监控主机的 CPU、内存和磁盘，还能精确追踪 Docker 容器的历史资源占用情况，并内置了灵活的告警系统。

* **GitHub Repo**: [henrygd/beszel](https://github.com/henrygd/beszel)
* **Star 数**: ⭐ 21,400+
* **官方主页**: [https://beszel.dev](https://beszel.dev)
* **核心语言**: Go (后端) / Svelte (前端)
* **开源协议**: MIT License

---

## ✨ 核心特性

### 1. 极致轻量与易用
- **低资源占用**: 代理端（Agent）体积极小，运行时的 CPU 和内存消耗远低于主流监控方案，不会给你的服务器带来额外负担。
- **开箱即用**: 无需繁琐的手动配置 YAML 文件，几分钟即可完成部署并开始收集数据。

### 2. 深度的 Docker 监控
相比于普通的探针面板，Beszel 可以记录并绘制每个 Docker 容器的 CPU、内存和网络 I/O 的**历史曲线图**。这对于排查哪个容器在半夜导致了内存泄露或 CPU 飙升极为有效。

### 3. 灵活的告警系统
内置完善的告警触发器，当以下指标超过阈值时，可通过 Webhook 或 Email 及时通知你：
- CPU 或内存使用率
- 磁盘空间不足
- 异常的负载或网络带宽
- 服务器掉线 / 容器停止运行状态

### 4. 现代化权限管理
- **多用户支持**: 用户可以管理自己的系统，管理员可以跨用户共享系统仪表板。
- **OAuth / OIDC 登录**: 支持接入大量第三方身份验证提供商，安全可靠，甚至可以禁用密码登录。

---

## 🚀 快速部署

Beszel 采用 `Hub (控制面板) + Agent (被控端代理)` 的架构。

**1. 部署 Hub 控制面板 (使用 Docker Compose)**:
```yaml
version: '3'
services:
  beszel:
    image: henrygd/beszel:latest
    container_name: beszel
    restart: unless-stopped
    ports:
      - "8090:8090"
    volumes:
      - ./beszel_data:/beszel_data
```

**2. 在被监控的服务器上部署 Agent**:
在 Hub 面板中添加节点后，系统会生成一行安装命令，直接在被控机运行即可：
```bash
docker run -d --name beszel-agent --restart unless-stopped \
  --network host \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -e PORT=45876 -e KEY="<生成的专属通信密钥>" \
  henrygd/beszel-agent
```

---

## 🔌 与其他工具的对比

| 特性 | Beszel | Netdata | 哪吒监控 (Nezha) |
|------|--------|---------|------------------|
| **资源占用** | ✅ 极低 | ⚠️ 较高 | ✅ 低 |
| **UI 风格** | 现代化、干净 | 信息密集、复杂 | 传统探针面板 |
| **Docker 历史** | ✅ 原生支持 | ✅ 支持但臃肿 | ❌ 仅限基础主机信息 |
| **部署难度** | 极简 | 中等 | 需要配置 GitHub OAuth |

---

## 💡 适用场景与总结

对于拥有多台 VPS 或 HomeLab 的个人开发者、独立站长以及中小型团队来说，Beszel 找到了功能与轻量的绝佳平衡点。它去除了企业级监控工具（如 Prometheus）那陡峭的学习曲线，又比传统的探针（如 ServerStatus）提供了更具价值的历史数据记录和容器追踪能力，是目前不可多得的新锐监控工具。
