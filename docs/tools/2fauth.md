---
title: 2FAuth
description: 自托管的 Web 版两步验证（2FA）管理器，安全生成并管理你的动态密码。
category: '👨‍💻 开发者工具'
date: '2026-04-30T22:55:42+08:00'
---
# 2FAuth：你的私有两步验证（2FA）令牌管家

![2FAuth OpenGraph Image](https://opengraph.githubassets.com/1/Bubka/2FAuth)

**2FAuth** 是一个基于 Web 的开源应用程序，用于安全地管理你的两步验证（2FA）账户并生成其安全代码（动态密码）。对于不想将 2FA 令牌绑定在单一手机设备（如 Google Authenticator）上，或者不信任第三方云同步服务（如 Authy）的用户来说，2FAuth 提供了一个完美且优雅的自托管替代方案。

* **GitHub Repo**: [Bubka/2FAuth](https://github.com/Bubka/2FAuth)
* **Star 数**: ⭐ 3,900+
* **官方主页**: [https://docs.2fauth.app/](https://docs.2fauth.app/)
* **核心语言**: PHP (Laravel) / Vue.js
* **开源协议**: AGPL v3.0

---

## ✨ 核心特性

### 1. 跨平台与跨设备访问
既然是 Web 应用，意味着你可以通过浏览器在手机、平板、电脑等任何设备上访问你的 2FA 动态密码，彻底摆脱了“手机丢失等于失去所有账户访问权限”的困扰。

### 2. 便捷的令牌管理
- **扫描与解析**: 支持通过设备摄像头扫描二维码添加账户，或者直接上传包含二维码的图片进行解析。
- **多种协议支持**: 除了标准的 TOTP (基于时间) 和 HOTP (基于 HMAC) 外，还支持生成 Steam Guard 代码。
- **分组与归类**: 可以将众多的 2FA 账户进行分组（如：工作、个人、财务），保持界面整洁有序。

### 3. 数据安全与便携性
- **自主掌控**: 数据存储在你自己托管的服务器数据库中。
- **导入导出**: 支持从其他验证器导入数据，也支持导出数据以进行本地离线备份。

### 4. 现代化的接口与多语言
提供功能完善的 RESTful API，方便与其他应用集成，并且目前支持包括中文在内的多种语言。

---

## 🚀 快速部署

推荐使用 Docker 进行一键部署，将你的私有验证器轻松上线。

```yaml
version: '3.8'

services:
  2fauth:
    image: 2fauth/2fauth
    container_name: 2fauth
    restart: always
    ports:
      - 8000:8000
    volumes:
      - ./2fauth_data:/srv
    environment:
      - APP_NAME=2FAuth
      - APP_ENV=production
      - APP_DEBUG=false
      - APP_URL=http://localhost:8000
      - DB_DATABASE=/srv/database/database.sqlite
```
将上述内容保存为 `docker-compose.yml` 并执行 `docker-compose up -d`。之后通过 `http://localhost:8000` 即可访问你的专属 2FA 密码库。

---

## 🔌 为什么选择自托管 2FA？

| 特性 | 2FAuth (自托管) | Google Authenticator | Authy |
|------|-----------------|----------------------|-------|
| **多设备同步** | ✅ 浏览器随时访问 | ⚠️ 仅依赖云端同步 (易泄漏) | ✅ 支持 |
| **数据所有权** | ✅ 绝对私有 | ❌ 绑定谷歌账号 | ❌ 绑定手机号及云端 |
| **设备丢失风险**| ✅ 无风险 (在服务器) | ⚠️ 极高风险 | ⚠️ 依赖云端恢复 |
| **备份便捷度** | ✅ 自主导出备份 | ❌ 不支持直接导出 | ❌ 不支持直接导出 |

---

## 💡 适用场景与总结

对于注重隐私安全、拥有多台设备（手机和多台电脑）、经常需要在不同终端输入验证码的数字极客和开发者来说，**2FAuth** 是极佳的选择。它不仅消除了手机不在手边时的焦虑，更确保了所有核心安全令牌完全掌握在自己手中。
