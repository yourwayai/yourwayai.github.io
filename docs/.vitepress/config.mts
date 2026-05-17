import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/',
  title: "YourwayAI开源导航站",
  description: "发现优质的免费开源软件",

  // 网站头部配置 (Favicon 与 OpenGraph 多媒体分享标签)
  head: [
    ['link', { rel: 'icon', href: '/logo.jpg' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'YourwayAI开源导航站' }],
    ['meta', { property: 'og:image', content: 'https://yourwayai.github.io/logo.jpg' }],
    ['meta', { property: 'og:description', content: '发现极致优雅的重磅开源软件与极客工具' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }]
  ],
  
  // 启用最后更新时间
  lastUpdated: true,

  themeConfig: {
    // 网站Logo
    logo: '/logo.jpg',

    // 网站顶部的导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '✨ 求职服务', link: '/ywc_resume_landing_page.html', target: '_blank' },
      { text: '关于', link: '/about' }
    ],

    // 网站左侧的分类侧边栏
    sidebar: [
      {
        text: '📝 知识管理 (2)',
        collapsed: false,
        items: [
          { text: 'Outline — 团队 Wiki 知识库', link: '/tools/outline' },
          { text: 'Memos — 碎片化灵感笔记', link: '/tools/memos' }
        ]
      },
      {
        text: '💬 沟通协作 (1)',
        collapsed: false,
        items: [
          { text: 'Chatwoot — 全渠道客服中台', link: '/tools/chatwoot' }
        ]
      },
      {
        text: '🎬 媒体与娱乐 (1)',
        collapsed: false,
        items: [
          { text: 'Jellyfin — 自建私人影院', link: '/tools/jellyfin' }
        ]
      },
      {
        text: '👨‍💻 开发者工具 (23)',
        collapsed: false,
        items: [
          { text: 'The Art of Command Line — 终端神技',
          link: '/tools/the-art-of-command-line' },
          { text: 'V8 Engine — JS 运行引擎',
          link: '/tools/v8' },
          { text: 'Storybook — UI 组件开发环境',
          link: '/tools/storybook' },
          { text: 'Hermes Agent — 开源 AI 代理',
          link: '/tools/hermes-agent' },
          { text: '3x-ui — Xray 协议面板',
          link: '/tools/3x-ui' },
          { text: 'Ghost — 开源博客系统',
          link: '/tools/wx_20260421130229' },
          { text: 'Open Chrome — 浏览器神器',
          link: '/tools/wx_20260413125458' },
          { text: 'CookCLI — 菜谱管理命令行',
          link: '/tools/cookcli' },
          { text: 'Penpot — 开源设计工具',
          link: '/tools/penpot' },
          { text: 'Goose — 本地 AI 代理',
          link: '/tools/goose' },
          { text: 'FluentFlyout — 电池弹窗美化',
          link: '/tools/fluentflyout' },
          { text: 'ConvertX — 格式转换利器',
          link: '/tools/wx_20260429211232' },
          { text: '2FAuth — 自托管 2FA 令牌',
          link: '/tools/2fauth' },
          { text: 'Beszel — 轻量服务器监控',
          link: '/tools/beszel' },
          { text: 'Stirling-PDF — 全能 PDF 工具箱',
          link: '/tools/stirling-pdf' },
          { text: 'RSSHub — 万物皆可 RSS',
          link: '/tools/rsshub' },
          { text: 'Prometheus — 云原生监控',
          link: '/tools/wx_20260511214354' },
          { text: 'InvoiceShelf — 开源财务管理',
          link: '/tools/wx_20260511214626' },
          { text: 'Vaultwarden — 轻量级密码库',
          link: '/tools/wx_20260511214924' },
          { text: 'LocalSend — 跨平台文件传输',
          link: '/tools/wx_20260511215131' },
          { text: 'Rapid-MLX — 本地 AI 加速引擎',
          link: '/tools/wx_20260511215328' },
          { text: 'The Agency — AI 专家智能体',
          link: '/tools/wx_20260518003237' },
          { text: 'Mercury Agent — 本地 AI 智能体', link: '/tools/wx_20260518005305' }
        ]
      },
      {
        text: '💡 微信专栏 (3)',
        collapsed: false,
        items: [
          { text: '熊猫速汇 — 跨境汇款攻略', link: '/tools/wx_20260419212801' },
          { text: 'AI 订阅 — 支付宝付款全攻略', link: '/tools/wx_20260419212858' },
          { text: '效率工具 — AI 时代神器推荐', link: '/tools/wx_20260421112236' }
        ]
      }
    ],

    // 右上角的社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/yourwayai/yourwayai.github.io' }
    ],

    // 搜索功能
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: '搜索文档',
                buttonAriaLabel: '搜索文档'
              },
              modal: {
                noResultsText: '无法找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换',
                  closeText: '关闭'
                }
              }
            }
          }
        }
      }
    },

    // 编辑此页
    editLink: {
      pattern: 'https://github.com/yourwayai/yourwayai.github.io/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },

    // 页面导航及本地化中文字段
    outline: {
      level: [2, 3],
      label: '页面导航'
    },
    docFooter: {
      prev: '上一页',
      next: '下一页'
    },
    lastUpdated: {
      text: '最后更新于'
    },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '相关文章',
    darkModeSwitchLabel: '主题',

    // 页脚
    footer: {
      message: 'Released under the MIT License.<br/><span style="display:inline-flex;align-items:center;gap:0.8rem;margin-top:0.5rem;font-size:0.9rem;"><a href="/ywc_resume_landing_page.html" target="_blank" rel="noopener">🏅 赞助我们</a> <span style="opacity:0.3">|</span> <a href="https://github.com" target="_blank" rel="noopener">GitHub</a> <span style="opacity:0.3">|</span> <a href="https://openai.com" target="_blank" rel="noopener">OpenAI</a> <span style="opacity:0.3">|</span> <a href="https://gemini.google.com" target="_blank" rel="noopener">Gemini</a> <span style="opacity:0.3">|</span> <a href="https://claude.ai" target="_blank" rel="noopener">Claude</a></span>',
      copyright: 'Copyright © 2026-present YourwayAI'
    }
  }
})
