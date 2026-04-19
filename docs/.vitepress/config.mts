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
      { text: '软件库', link: '/tools/outline' },
      { text: '关于', link: '/about' }
    ],

    // 网站左侧的分类侧边栏
    sidebar: [
      {
        text: '效率与生产力 (Productivity)',
        collapsed: false,
        items: [
          { text: 'Outline (团队Wiki)', link: '/tools/outline' },
          { text: 'Memos (碎片化笔记)', link: '/tools/memos' },
          { text: 'Chatwoot (沟通与客服)', link: '/tools/chatwoot' }
        ]
      },
      {
        text: '开发者生态 (Developer Ecosystem)',
        collapsed: false,
        items: [
          { text: '命令行的艺术 (终端)', link: '/tools/the-art-of-command-line' },
          { text: 'V8 Engine (运行环境)', link: '/tools/v8' }
        ]
      },
      {
        text: '数字生活与媒体 (Lifestyle & Media)',
        collapsed: false,
        items: [
          { text: 'Jellyfin (私人影院)', link: '/tools/jellyfin' }
        ]
      },
      {
        text: '星球专栏与优选资源 (Featured Resources)',
        collapsed: false,
        items: [
          { text: '最强浏览器杀手 Open Ch...', link: '/tools/wx_20260413125458' },
          { text: '手慢无：送出 5 个免手续费汇...', link: '/tools/wx_20260419212801' },
          { text: '支付宝可直接付款，3分钟搞定 ...', link: '/tools/wx_20260419212858' }
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
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2026-present YourwayAI'
    }
  }
})
