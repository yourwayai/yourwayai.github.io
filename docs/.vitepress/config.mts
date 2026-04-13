import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/yourwayai/',
  title: "YourwayAI开源导航站",
  description: "发现优质的免费开源软件",
  
  // 启用最后更新时间
  lastUpdated: true,

  themeConfig: {
    // 网站Logo
    logo: '/logo.png',

    // 网站顶部的导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '软件库', link: '/tools/outline' },
      { text: '关于', link: '/about' }
    ],

    // 网站左侧的分类侧边栏
    sidebar: [
      {
        text: '笔记与知识库',
        collapsed: false,
        items: [
          { text: 'Outline (团队Wiki)', link: '/tools/outline' },
          { text: 'Memos (碎片化笔记)', link: '/tools/memos' }
        ]
      },
      {
        text: '媒体与影音',
        collapsed: false,
        items: [
          { text: 'Jellyfin (私人影院)', link: '/tools/jellyfin' }
        ]
      },
      {
        text: '自动化收录',
        collapsed: false,
        items: [
          { text: '命令行的艺术', link: '/tools/the-art-of-command-line' },
          { text: 'V8 Engine', link: '/tools/v8' },
          { text: 'chatwoot', link: '/tools/chatwoot' }
        ]
      },
      {
        text: '公众号优选',
        collapsed: false,
        items: [
          { text: 'GitHub热榜开源 Tabb...', link: '/tools/wx_20260413125042' },
          { text: '最强浏览器杀手 Open Ch...', link: '/tools/wx_20260413125458' }
        ]
      }
    ],

    // 右上角的社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/BruceMi321/yourwayai' }
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
      pattern: 'https://github.com/BruceMi321/yourwayai/edit/main/docs/:path',
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
