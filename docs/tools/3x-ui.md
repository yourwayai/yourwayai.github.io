---
title: 3x-ui — 下一代 Xray 节点可视化管理面板
description: 支持目前最全代理通信协议与多出口配置的极客首选自建节点管理系统。
category: '👨‍💻 开发者工具'
---

# 3x-ui: 顶级的 Xray 节点全能可视化桌面

![3x-ui OpenGraph Image](https://opengraph.githubassets.com/1/MHSanaei/3x-ui)

在现今纷繁复杂的网络分流与多协议架构需求下，**3x-ui** 凭借其对 Xray-core 底层的极致榨取和优雅的中文 Web 管理交互面，成为了极客群体自建节点时几乎必然装配的“大杀器”。它不仅支持市面上所有的主流网络协议配置，还能精确展示服务器硬件资源曲线和流量大盘。

* **GitHub Repo**: [MHSanaei/3x-ui](https://github.com/MHSanaei/3x-ui)
* **Star 数**: ⭐ 29000+
* **核心语言**: Go (Golang) / Vue
* **开源协议**: GPL-3.0 License

---

## ✨ 核心特性

### 1. 全协议兼容与即插即用 (Multi-Protocol Mastery)
完美支持当今最流行、最高速的网络握手与加密协议：`Vless`, `Vmess`, `Trojan`, `Shadowsocks`, `Wireguard`。甚至是诸如 XTLS-Reality 与 gRPC 等复杂前沿底层架构的设定，也可通过图形页面极简的勾选开关进行部署，让新手也能彻底摆脱纯靠手动敲写长达几百行 JSON 文件的折磨。

### 2. 多用户全时监控系统 (Comprehensive Metrics & Multi-User)
你可以用它为你的开发小团队提供网络支持。面板提供实时的系统负载（CPU、内存）及网络实时 I/O 速率动态图表。允许管理员无限添加、设定超期日以及统计和限制单个用户的独立流量状态；到期/超额后全自动断连，防止被乱刷。

### 3. 多重出站代理规则 (Advanced Outbound Routing)
不仅仅能接收访问请求，3x-ui 还支持高端的**反向代理与多层链式出口分流 (Routing Flow)**。例如，你可建立分流节点，规定去往某些敏感流媒体网站的请求交由后置专属的专线节点（如 Warp+）发出，完全依靠 Web 上的几条规则列表点击保存解决。

### 4. 极致的一键快装体系 (One-Click Installer)
无论是 Debian, Ubuntu 还是 CentOS 主流系统环境，不需要预先安装繁琐的依赖构件甚至 Docker，直接执行一条 Bash 命令，这套脚本就会自动装满所有底层库、编译并部署 Web 端口生成安全入口。

### 5. Telegram Bot 无缝联动控制
自带机器人绑定！直接将个人面板的 API 参数与 Telegram 机器人打通，当你手边没有登录后台条件时，通过 TG 发送斜杠命令即可轻松拉取当前的流量消耗报表、创建新连接甚至是热重启面板进程。

---

## 🚀 极速部署方案

要在一台纯净并拥有静态 IP 的廉价 VPS（Linux Server）上拉起整套 3x-ui 后台：

```bash
# SSH 远程连接至你的 Linux 服务器后，推荐使用 Root 权限闭眼运行这行安装神令：
bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)
```
*在跑动过程其控制台交互会引导你设置随机访问端口与初始化管理员账号密码。执行完毕之后，使用浏览器访问 `IP:你设定的端口` 即可进入系统开始创建节点。*

---

## 💡 适用场景与总结

这个开源系统属于典型的**基础设施/网络测试通道类利器**。

极度推荐应用于以下领域：
* 开发组或者独立全栈工作者常需与海外服务器拉取大型构建环境（国际化部署）时确保网络无瓶颈。
* 需要针对不同的物理设备（如手机、外置路由器软路由平台等）精准分发特定专线通道配置操作。
* 对直接操控晦涩难懂的 Xray-core `config.json` 感到极大排斥，渴望一键生成所有主流协议分享链接并能从 UI 点选免费申请域名的技术玩家。
