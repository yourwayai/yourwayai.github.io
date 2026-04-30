---
title: Stirling-PDF
description: 本地托管的强大 PDF 瑞士军刀，满足你对 PDF 的一切操作需求。
category: '👨‍💻 开发者工具'
date: '2026-04-30T23:00:32+08:00'
---
# Stirling-PDF：全能开源本地 PDF 工具箱

![Stirling-PDF OpenGraph Image](https://opengraph.githubassets.com/1/Stirling-Tools/Stirling-PDF)

**Stirling-PDF** 是一款功能强大、开源且支持本地托管的网页版 PDF 操作工具（PDF 瑞士军刀）。它允许你在任何设备上编辑和处理 PDF 文件。由于所有操作都在本地服务器上进行，数据不会离开你的机器，彻底解决了商业云端 PDF 工具带来的隐私泄露和费用高昂的问题。

* **GitHub Repo**: [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
* **Star 数**: ⭐ 41,000+
* **官方主页**: [https://stirlingpdf.com](https://stirlingpdf.com)
* **核心语言**: Java / Vue
* **开源协议**: MIT License

---

## ✨ 核心特性

Stirling-PDF 提供了超过 50+ 种 PDF 处理工具，几乎涵盖了日常办公的全部需求：

### 1. 基础编辑与页面管理
- **拆分与合并**: 自由合并多个 PDF，或提取/拆分特定页面。
- **页面重组**: 旋转、删除、重排页面顺序。
- **添加/删除内容**: 插入空白页，添加页码、水印或图片。

### 2. 高级转换 (Convert)
- **PDF 转其他格式**: 转换为 Word、图片、HTML、CSV 等。
- **其他格式转 PDF**: 将图片、Word、Excel 等轻松转为 PDF。
- **OCR 识别**: 将扫描版 PDF 或图片通过 OCR 技术转换为可搜索的文本 PDF（支持多国语言）。

### 3. 安全与权限管理
- **加解密**: 为 PDF 添加密码保护，或移除已知的密码和权限限制。
- **签名与脱敏**: 添加数字签名，或永久涂黑/脱敏文档中的敏感信息。

### 4. 自动化与企业级特性
- **API 支持**: 提供丰富的 REST API，方便开发者集成到自动化工作流中。
- **多语言与自定义**: 支持 40+ 种语言界面，提供暗色模式，并支持自定义企业 Logo。

---

## 🚀 快速部署

最推荐的安装方式是通过 Docker 进行本地部署，确保数据的绝对安全。

```bash
# 运行完整版（包含 OCR 等所有依赖）
docker run -d \
  -p 8080:8080 \
  -v /location/of/trainingData:/usr/share/tessdata \
  -v /location/of/extraConfigs:/configs \
  -v /location/of/customFiles:/customFiles \
  -e DOCKER_ENABLE_SECURITY=false \
  --name stirling-pdf \
  frooodle/s-pdf:latest
```
部署完成后，浏览器访问 `http://localhost:8080` 即可开始使用。

---

## 🔌 与其他工具的对比

| 特性 | Stirling-PDF | Adobe Acrobat | iLovePDF (网页版) |
|------|--------------|---------------|-------------------|
| **隐私安全** | ✅ 数据完全本地处理 | ❌ 上传至云端 | ❌ 上传至云端 |
| **价格** | ✅ 完全免费开源 | 💰 昂贵的订阅费 | 💰 高级功能需付费 |
| **API 支持** | ✅ 免费提供 | ❌ 昂贵的企业 API | ❌ |
| **OCR 功能** | ✅ 本地免费离线识别 | ✅ 支持 | ✅ 仅限高级会员 |

---

## 💡 适用场景与总结

如果你经常需要处理 PDF 文件（合并合同、提取页面、转换格式、打水印），但又对将包含敏感信息的文档上传到第三方网站（如 iLovePDF）感到担忧，那么 **Stirling-PDF** 就是为你量身定制的。它非常适合部署在公司内网供全员使用，或是作为个人的私有云 PDF 处理中心。
