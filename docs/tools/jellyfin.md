---
title: Jellyfin
description: 掌握自己媒体资源的终极私人影院解决方案，拒绝商业捆绑。
icon: '🎬'
category: '数字生活与媒体 (Lifestyle & Media)'
---
# Jellyfin

**Jellyfin** 是一个自由的软件媒体系统，用于控制和管理您的媒体。它是 Emby 和 Plex 的绝佳开源替代品。

## 🌟 核心特色
* **完全免费**：没有高级订阅包，没有付费墙，100% 开源免费。
* **支持多种格式**：支持几乎所有的视频、音频和图片格式。
* **跨平台客户端**：支持 Web、Android、iOS、Apple TV、Roku、Fire TV 等几乎所有主流平台。
* **硬件转码**：支持通过 QSV (Intel)、NVENC (Nvidia) 和 AMF (AMD) 进行硬件加速转码。

## 🚀 Docker 快速部署

使用官方推荐的 Docker 配置：

```yaml
version: '3.5'
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    user: 1000:1000
    network_mode: 'host'
    volumes:
      - /path/to/config:/config
      - /path/to/cache:/cache
      - /path/to/media:/media
    restart: 'unless-stopped'
```
