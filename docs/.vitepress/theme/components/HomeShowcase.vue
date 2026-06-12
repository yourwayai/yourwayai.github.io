<template>
  <div class="home-showcase-container">
    <div class="showcase-content">

      <!-- Main Content: Tool Grid -->
      <main class="main-content">
        
        <!-- Pinned Section -->
        <section class="pinned-section">
          <div class="pinned-badge">
            <span class="pulse-dot"></span>
            置顶推荐
          </div>
          <div class="pinned-content">
            <h3 class="pinned-title">支付宝可直接付款，3分钟搞定 ChatGPT/Gemini/Claude订阅</h3>
            <p class="pinned-desc">无需海外信用卡，安全稳定地订阅海外顶级AI大模型，彻底打破支付门槛。</p>
            <a href="/tools/wx_20260419212858" class="pinned-link">立即阅读 →</a>
          </div>

        </section>

        <!-- Mobile-only Sponsors Swipe Container -->
        <div class="mobile-sponsors-container">
          <!-- Mobile-only Sponsor Banner 1: GamsGo -->
          <a href="https://www.gamsgo.com/partner/WzbXX" target="_blank" rel="noopener" class="mobile-sponsor-banner" style="background: linear-gradient(135deg, rgba(138, 43, 226, 0.08) 0%, rgba(255, 69, 0, 0.04) 100%); border-color: rgba(138, 43, 226, 0.25);">
            <img class="mobile-sponsor-icon" src="/gamsgo.png" style="width: 24px; height: 24px; border-radius: 6px; object-fit: cover;" />
            <div class="mobile-sponsor-text">
              <strong style="color: #8a2be2;">GamsGo</strong>
              <span>流媒体与 AI 合租平台</span>
            </div>
            <span class="mobile-sponsor-arrow" style="color: #8a2be2;">→</span>
          </a>

          <!-- Mobile-only Sponsor Banner 2: YourWayCareer -->
          <a href="/ywc_resume_landing_page.html" target="_blank" rel="noopener" class="mobile-sponsor-banner">
            <img class="mobile-sponsor-icon" src="/ywc.jpg" style="width: 24px; height: 24px; border-radius: 6px; object-fit: cover;" />
            <div class="mobile-sponsor-text">
              <strong>YourWayCareer</strong>
              <span>高端简历精修服务</span>
            </div>
            <span class="mobile-sponsor-arrow">→</span>
          </a>

          <!-- Mobile-only Sponsor Banner 3: giffgaff -->
          <a href="/giffgaff-sim-promo.html" target="_blank" rel="noopener" class="mobile-sponsor-banner" style="background: linear-gradient(135deg, rgba(255, 79, 109, 0.08) 0%, rgba(255, 204, 0, 0.04) 100%); border-color: rgba(255, 79, 109, 0.25);">
            <img class="mobile-sponsor-icon" src="/giffgaff.png" style="width: 24px; height: 24px; border-radius: 6px; object-fit: cover;" />
            <div class="mobile-sponsor-text">
              <strong style="color: #ff4f6d;">giffgaff</strong>
              <span>英国免费 SIM 全球直邮</span>
            </div>
            <span class="mobile-sponsor-arrow" style="color: #ff4f6d;">→</span>
          </a>
        </div>

        <!-- Control Bar -->
        <div class="control-bar">
          <div class="search-container">
            <div class="search-wrapper">
              <span class="search-icon">🔍</span>
              <input 
                ref="searchInput"
                type="text" 
                v-model="searchQuery" 
                placeholder="在当前页面过滤卡片..." 
                class="search-input" 
              />
              <span class="search-shortcut">/</span>
            </div>
            <button 
              class="filter-toggle-btn" 
              :class="{ active: isFilterOpen }"
              @click="isFilterOpen = !isFilterOpen"
            >
              <span class="filter-icon">
                <svg xmlns="http://www.w3.org/2005/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon></svg>
              </span>
              <span>筛选</span>
              <span class="active-filters-badge" v-if="selectedPlatforms.length || selectedDeployments.length">
                {{ selectedPlatforms.length + selectedDeployments.length }}
              </span>
            </button>
            <button
              class="random-btn"
              @click="redirectToRandom"
              title="随机推荐一个工具"
            >
              <span class="random-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg>
              </span>
              <span class="random-text">手气不错</span>
            </button>
          </div>

          <!-- Filters Panel -->
          <transition name="slide-fade">
            <div v-if="isFilterOpen" class="filter-panel">
              <div class="filter-columns">
                <!-- Platform Column -->
                <div class="filter-column">
                  <h4 class="filter-column-title">支持系统</h4>
                  <div class="filter-options">
                    <label v-for="plat in availablePlatforms" :key="plat" class="filter-option-label">
                      <input type="checkbox" :value="plat" v-model="selectedPlatforms" />
                      <span class="checkbox-custom"></span>
                      <span class="option-text">{{ plat }}</span>
                      <span class="option-count">{{ getPlatformCount(plat) }}</span>
                    </label>
                  </div>
                </div>

                <!-- Deployment Column -->
                <div class="filter-column">
                  <h4 class="filter-column-title">部署与安装</h4>
                  <div class="filter-options">
                    <label v-for="dep in availableDeployments" :key="dep" class="filter-option-label">
                      <input type="checkbox" :value="dep" v-model="selectedDeployments" />
                      <span class="checkbox-custom"></span>
                      <span class="option-text">{{ dep }}</span>
                      <span class="option-count">{{ getDeploymentCount(dep) }}</span>
                    </label>
                  </div>
                </div>

                <!-- Sorting Column -->
                <div class="filter-column">
                  <h4 class="filter-column-title">排序规则</h4>
                  <div class="filter-options">
                    <label class="filter-option-label">
                      <input type="radio" value="newest" v-model="sortBy" />
                      <span class="radio-custom"></span>
                      <span class="option-text">最新发布</span>
                    </label>
                    <label class="filter-option-label">
                      <input type="radio" value="stars" v-model="sortBy" />
                      <span class="radio-custom"></span>
                      <span class="option-text">GitHub Star数</span>
                    </label>
                    <label class="filter-option-label">
                      <input type="radio" value="views" v-model="sortBy" />
                      <span class="radio-custom"></span>
                      <span class="option-text">浏览热度</span>
                    </label>
                  </div>
                </div>
              </div>

              <div class="filter-footer">
                <button class="clear-filters-btn" @click="clearFilters">重置筛选</button>
              </div>
            </div>
          </transition>

          <div class="category-pills">
            <button 
              v-for="cat in uniqueCategories" 
              :key="cat"
              class="pill-btn"
              :class="{ active: activeCategory === cat }"
              @click="activeCategory = cat"
            >
              {{ cat }}
            </button>
          </div>
        </div>

        <div class="tools-grid">
          <a
            :href="tool.link"
            class="tool-card"
            v-for="tool in filteredTools"
            :key="tool.id"
            @mousemove="onCardMouseMove($event)"
            @mouseleave="onCardMouseLeave($event)"
          >
            <div class="card-glow" :style="{ background: tool.iconBg }"></div>
            <div class="time-badge" v-if="getRelativeTime(tool.date)" :class="{ 'is-new': getRelativeTime(tool.date) === '✨ New' }">
              {{ getRelativeTime(tool.date) }}
            </div>
            <div class="tool-card-header">
              <div class="tool-icon-wrapper" :style="{ backgroundColor: tool.iconBg }">
                <img v-if="isUrl(tool.icon)" :src="tool.icon" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px;" />
                <span v-else class="tool-icon-inner">{{ tool.icon }}</span>
              </div>
              <div class="tool-meta-header">
                <h3>{{ tool.name }}</h3>
                <span class="tech-tag">{{ tool.category }}</span>
              </div>
            </div>
            <p class="tool-desc">{{ tool.desc }}</p>
            <div class="tool-footer">
              <div class="stats">
                <span v-if="tool.stars !== '-'">⭐ {{ tool.stars }}</span>
                <span v-if="tool.views !== '-'">👁️ {{ tool.views }}</span>
              </div>
              <div class="visit-btn">详情阅读 →</div>
            </div>
          </a>
        </div>

        <!-- Empty State -->
        <div v-if="filteredTools.length === 0" class="empty-state">
          <div class="empty-icon">📭</div>
          <h3>没有找到匹配的内容</h3>
          <p>请尝试其他关键词或分类</p>
          <button class="reset-btn" @click="searchQuery = ''; activeCategory = '全部'; clearFilters()">重置过滤条件</button>
        </div>
      </main>

      <!-- Right Sidebar: Ads / Sponsored -->
      <aside class="sidebar right-sidebar">
        <h2 class="sidebar-title sponsor-title">👑 Sponsored</h2>

        <!-- Sponsor #1: GamsGo -->
        <a href="https://www.gamsgo.com/partner/WzbXX" target="_blank" rel="noopener" class="real-sponsor-card" style="background: linear-gradient(145deg, rgba(138, 43, 226, 0.06) 0%, rgba(255, 69, 0, 0.03) 100%); border-color: rgba(138, 43, 226, 0.3);">
          <div class="sponsor-header">
            <img class="sponsor-logo" src="/gamsgo.png" style="background: rgba(138, 43, 226, 0.08); object-fit: cover;" />
            <div class="sponsor-meta">
              <h3 class="sponsor-name">GamsGo</h3>
              <p class="sponsor-tagline" style="color: #8a2be2;">流媒体与 AI 合租平台</p>
            </div>
          </div>
          <div class="sponsor-action" style="color: #8a2be2; border-top-color: rgba(138, 43, 226, 0.15);">立即上车体验 →</div>
        </a>

        <!-- Sponsor #2: YourWayCareer -->
        <a href="/ywc_resume_landing_page.html" target="_blank" rel="noopener" class="real-sponsor-card">
          <div class="sponsor-header">
            <img class="sponsor-logo" src="/ywc.jpg" style="object-fit: cover;" />
            <div class="sponsor-meta">
              <h3 class="sponsor-name">YourWayCareer</h3>
              <p class="sponsor-tagline">高竞争岗位简历精修计划</p>
            </div>
          </div>
          <div class="sponsor-action">查看服务详情 →</div>
        </a>

        <!-- Sponsor #3: giffgaff -->
        <a href="/giffgaff-sim-promo.html" target="_blank" rel="noopener" class="real-sponsor-card" style="background: linear-gradient(145deg, rgba(255, 79, 109, 0.06) 0%, rgba(255, 204, 0, 0.03) 100%); border-color: rgba(255, 79, 109, 0.3);">
          <div class="sponsor-header">
            <img class="sponsor-logo" src="/giffgaff.png" style="background: rgba(255, 79, 109, 0.08); object-fit: cover;" />
            <div class="sponsor-meta">
              <h3 class="sponsor-name">giffgaff</h3>
              <p class="sponsor-tagline" style="color: #ff4f6d;">英国免费 SIM 全球直邮</p>
            </div>
          </div>
          <div class="sponsor-action" style="color: #ff4f6d; border-top-color: rgba(255, 79, 109, 0.15);">免费申领手机卡 →</div>
        </a>

      </aside>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'

const onCardMouseMove = (e) => {
  const card = e.currentTarget
  const rect = card.getBoundingClientRect()
  const x = e.clientX - rect.left
  const y = e.clientY - rect.top
  card.style.setProperty('--spotlight-x', `${x}px`)
  card.style.setProperty('--spotlight-y', `${y}px`)
  card.style.setProperty('--spotlight-opacity', '1')
}

const onCardMouseLeave = (e) => {
  e.currentTarget.style.setProperty('--spotlight-opacity', '0')
}

// Use Vite's native glob import to read all markdown frontmatter
const modules = import.meta.glob('/tools/*.md', { eager: true })

// Simple color rotation for aesthetic card backgrounds
const colors = [
  'rgba(52, 199, 89, 0.12)',
  'rgba(0, 122, 255, 0.12)',
  'rgba(255, 149, 0, 0.12)',
  'rgba(175, 82, 222, 0.12)',
  'rgba(255, 45, 85, 0.12)'
]

const searchQuery = ref('')
const activeCategory = ref('全部')

const searchInput = ref(null)
const isFilterOpen = ref(false)
const selectedPlatforms = ref([])
const selectedDeployments = ref([])
const sortBy = ref('newest') // newest, stars, views

// Available filter choices
const availablePlatforms = ['Linux', 'Windows', 'macOS']
const availableDeployments = ['Docker', 'Source Code', 'CLI / Command Line', 'Binary / packages']

// Setup hotkey listener for "/"
onMounted(() => {
  const handleKeyDown = (e) => {
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      e.preventDefault()
      searchInput.value?.focus()
    }
  }
  window.addEventListener('keydown', handleKeyDown)
  onUnmounted(() => {
    window.removeEventListener('keydown', handleKeyDown)
  })
})

const categoryOrder = [
  '🤖 AI 与智能体',
  '🛠️ 系统与运维',
  '🔒 安全与隐私',
  '✍️ 知识与协作',
  '📂 实用与提效',
  '💰 金融与支付',
  '🎨 设计与极客',
  '🍿 影音与娱乐'
]

const rawTools = Object.entries(modules).map(([path, mod], index) => {
  const fm = mod.default?.__pageData?.frontmatter || mod.__pageData?.frontmatter || {}
  const url = path.replace(/\.md$/, '.html')
  return {
    id: index,
    name: fm.title || 'Untitled',
    desc: fm.description || '',
    category: fm.category || '未分类',
    icon: fm.icon || '📦',
    iconBg: colors[index % colors.length],
    link: url,
    stars: fm.stars || '-',
    views: fm.views || '-',
    date: fm.date || '2000-01-01',
    platforms: fm.platforms || [],
    deployments: fm.deployments || []
  }
})

// Sort tools by date descending (newest first)
const allTools = rawTools.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())

// Compute unique categories
const uniqueCategories = computed(() => {
  const cats = new Set(allTools.map(t => t.category))
  const sortedCats = Array.from(cats).sort((a, b) => {
    const idxA = categoryOrder.indexOf(a)
    const idxB = categoryOrder.indexOf(b)
    if (idxA === -1 && idxB === -1) return a.localeCompare(b)
    if (idxA === -1) return 1
    if (idxB === -1) return -1
    return idxA - idxB
  })
  return ['全部', ...sortedCats]
})

// Filter matching deployments (helper)
const matchesDeploymentFilter = (toolDeployments, filterVal) => {
  if (!toolDeployments || !Array.isArray(toolDeployments)) return false
  const lowerDeps = toolDeployments.map(d => d.toLowerCase())
  
  if (filterVal === 'Docker') {
    return lowerDeps.includes('docker') || lowerDeps.includes('docker compose')
  }
  if (filterVal === 'Source Code') {
    return lowerDeps.includes('source code') || lowerDeps.includes('source')
  }
  if (filterVal === 'CLI / Command Line') {
    return lowerDeps.includes('cli') || lowerDeps.includes('command line') || lowerDeps.includes('cargo') || lowerDeps.includes('brew') || lowerDeps.includes('pip')
  }
  if (filterVal === 'Binary / packages') {
    return lowerDeps.includes('binary') || lowerDeps.includes('npx') || lowerDeps.includes('plugins')
  }
  return false
}

// Base filtered tools by category & query
const baseFilteredTools = computed(() => {
  let result = allTools

  if (activeCategory.value !== '全部') {
    result = result.filter(t => t.category === activeCategory.value)
  }

  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase()
    result = result.filter(t => 
      t.name.toLowerCase().includes(q) || 
      t.desc.toLowerCase().includes(q) ||
      t.category.toLowerCase().includes(q)
    )
  }

  return result
})

// Filter Option counts
const getPlatformCount = (plat) => {
  return baseFilteredTools.value.filter(t => t.platforms && Array.isArray(t.platforms) && t.platforms.includes(plat)).length
}

const getDeploymentCount = (dep) => {
  return baseFilteredTools.value.filter(t => matchesDeploymentFilter(t.deployments, dep)).length
}

const clearFilters = () => {
  selectedPlatforms.value = []
  selectedDeployments.value = []
  sortBy.value = 'newest'
}

// Compute filtered tools including platform, deployment filters and sorting
const filteredTools = computed(() => {
  let result = baseFilteredTools.value

  // Apply Platform Filter
  if (selectedPlatforms.value.length > 0) {
    result = result.filter(t => 
      t.platforms && Array.isArray(t.platforms) && 
      selectedPlatforms.value.some(plat => t.platforms.includes(plat))
    )
  }

  // Apply Deployment Filter
  if (selectedDeployments.value.length > 0) {
    result = result.filter(t => 
      selectedDeployments.value.some(dep => matchesDeploymentFilter(t.deployments, dep))
    )
  }

  // Apply Sorting
  return [...result].sort((a, b) => {
    if (sortBy.value === 'stars') {
      const parseStars = (str) => {
        if (!str || str === '-') return 0
        const s = str.toLowerCase()
        if (s.endsWith('k')) return parseFloat(s) * 1000
        if (s.endsWith('m')) return parseFloat(s) * 1000000
        return parseFloat(s) || 0
      }
      return parseStars(b.stars) - parseStars(a.stars)
    } else if (sortBy.value === 'views') {
      const parseViews = (str) => {
        if (!str || str === '-') return 0
        const s = str.toLowerCase()
        if (s.endsWith('k')) return parseFloat(s) * 1000
        return parseFloat(s) || 0
      }
      return parseViews(b.views) - parseViews(a.views)
    } else {
      return new Date(b.date).getTime() - new Date(a.date).getTime()
    }
  })
})

const isUrl = (str) => {
  if (!str) return false
  return str.startsWith('http://') || str.startsWith('https://') || str.startsWith('/')
}

// Helper for relative time (or "New" badge)
const getRelativeTime = (dateString) => {
  const date = new Date(dateString)
  if (isNaN(date.getTime())) return ''
  
  const now = new Date()
  const diffTime = now - date
  if (diffTime < 0) return '✨ New'
  
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))
  
  if (diffDays < 1) return '✨ New'
  if (diffDays <= 30) return `${diffDays} 天前`
  if (diffDays <= 365) return `${Math.floor(diffDays / 30)} 个月前`
  return `${Math.floor(diffDays / 365)} 年前`
}

// Navigate to a random tool
const redirectToRandom = () => {
  if (allTools && allTools.length > 0) {
    const eligibleTools = allTools.filter(t => !t.link.includes('212801') && !t.link.includes('212858') && !t.link.includes('112236'))
    const pool = eligibleTools.length > 0 ? eligibleTools : allTools
    const randomTool = pool[Math.floor(Math.random() * pool.length)]
    window.location.href = randomTool.link
  }
}
</script>

<style scoped>
/* Reset and Base Constraints */
.home-showcase-container {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
  color: var(--vp-c-text-1);
  font-family: inherit;
}

.showcase-content {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 2rem;
  align-items: start;
}

@media (max-width: 900px) {
  .showcase-content {
    grid-template-columns: 1fr;
  }
  .right-sidebar {
    display: none; /* 桌面端侧边栏在移动端隐藏，改用上方的 mobile-sponsor-banner 代替 */
  }
}

/* Sidebar Styles */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  position: sticky;
  top: calc(var(--vp-nav-height) + 1.5rem); /* 粘帖在导航栏正下方 */
  max-height: calc(100vh - var(--vp-nav-height) - 3rem);
  overflow-y: auto;
  scrollbar-width: none; /* Firefox */
}

.sidebar::-webkit-scrollbar {
  display: none; /* Chrome/Safari */
}

/* Mobile Sponsor Carousel Container */
.mobile-sponsors-container {
  display: none; /* hidden on desktop */
  gap: 0.8rem;
  overflow-x: auto;
  padding: 0.2rem 0.5rem 0.8rem;
  scrollbar-width: none; /* Firefox */
  -webkit-overflow-scrolling: touch;
}

.mobile-sponsors-container::-webkit-scrollbar {
  display: none; /* Chrome/Safari */
}

/* Mobile Sponsor Banner */
.mobile-sponsor-banner {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  padding: 0.55rem 0.8rem;
  background: linear-gradient(135deg, rgba(184, 135, 70, 0.08) 0%, rgba(223, 195, 150, 0.04) 100%);
  border: 1px solid rgba(184, 135, 70, 0.35);
  border-radius: 10px;
  text-decoration: none !important;
  color: inherit !important;
  transition: all 0.25s ease;
  position: relative;
  overflow: hidden;
  flex: 0 0 260px; /* fixed width in scrolling carousel */
}

.mobile-sponsor-banner::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(184, 135, 70, 0.04), transparent);
  pointer-events: none;
}

.mobile-sponsor-banner:hover {
  border-color: rgba(184, 135, 70, 0.6);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px -3px rgba(184, 135, 70, 0.15);
}

.mobile-sponsor-icon {
  font-size: 1.25rem;
  flex-shrink: 0;
}

.mobile-sponsor-text {
  display: flex;
  flex-direction: column;
  gap: 0.05rem;
  flex: 1;
  min-width: 0;
}

.mobile-sponsor-text strong {
  font-size: 0.82rem;
  font-weight: 700;
  color: #b88746;
}

.mobile-sponsor-text span {
  font-size: 0.72rem;
  color: var(--vp-c-text-2);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.mobile-sponsor-arrow {
  font-size: 0.85rem;
  color: #b88746;
  font-weight: 700;
  flex-shrink: 0;
  transition: transform 0.2s;
}

.mobile-sponsor-banner:hover .mobile-sponsor-arrow {
  transform: translateX(2px);
}

@media (max-width: 900px) {
  .mobile-sponsors-container {
    display: flex;
  }
}

.sidebar-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--vp-c-border);
}



/* Main Content Styles */
.main-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  min-width: 0; /* 防止子元素横向溢出导致 CSS Grid 被无限撑开 (Grid Blowout) */
}

/* Pinned Section */
.pinned-section {
  background: rgba(150, 150, 150, 0.04);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--vp-c-border);
  border-radius: 20px;
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.02);
}

.pinned-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background-color: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  padding: 0.2rem 0.6rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  background-color: var(--vp-c-brand-1);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(24, 216, 103, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(24, 216, 103, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(24, 216, 103, 0); }
}

.pinned-title {
  font-size: 1.25rem !important;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
  color: var(--vp-c-text-1);
  line-height: 1.4;
}

.pinned-desc {
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  margin: 0 0 1.2rem 0;
  line-height: 1.5;
}

.pinned-link {
  display: inline-block;
  background-color: var(--vp-c-brand-1);
  color: #fff;
  padding: 0.5rem 1.2rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.pinned-link:hover {
  background-color: var(--vp-c-brand-2);
  transform: translateY(-1px);
}


/* Control Bar & Search */
.control-bar {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 1rem;
  margin-bottom: 1.5rem;
  width: 100%;
}

.search-container {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  width: 100%;
}

.search-wrapper {
  position: relative;
  flex: 1;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2rem;
  opacity: 0.6;
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 0.8rem 3rem 0.8rem 3rem;
  border-radius: 999px;
  border: 1px solid var(--vp-c-border);
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 1rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
  box-sizing: border-box;
}

.search-input:focus {
  outline: none;
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 0 0 3px rgba(24, 216, 103, 0.15);
  background-color: var(--vp-c-bg);
}

.search-shortcut {
  position: absolute;
  right: 1.2rem;
  top: 50%;
  transform: translateY(-50%);
  background: var(--vp-c-bg-mute);
  border: 1px solid var(--vp-c-border);
  color: var(--vp-c-text-3);
  font-size: 0.75rem;
  padding: 1px 6px;
  border-radius: 4px;
  pointer-events: none;
  font-family: var(--vp-font-family-mono);
}

.filter-toggle-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.2rem;
  border-radius: 999px;
  border: 1px solid var(--vp-c-border);
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
  white-space: nowrap;
}

.filter-toggle-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background-color: var(--vp-c-bg);
}

.filter-toggle-btn.active {
  background-color: var(--vp-c-brand-soft);
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

/* Random Tool Button */
.random-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.2rem;
  border-radius: 999px;
  border: 1px solid rgba(255, 149, 0, 0.35);
  background-color: rgba(255, 149, 0, 0.06);
  color: #ff9500;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(255, 149, 0, 0.06);
  white-space: nowrap;
}

.random-btn:hover {
  background-color: rgba(255, 149, 0, 0.14);
  border-color: #ff9500;
  box-shadow: 0 4px 16px rgba(255, 149, 0, 0.18);
  transform: translateY(-1px);
}

.random-btn:active {
  transform: translateY(0px);
}

.dark .random-btn {
  border-color: rgba(255, 149, 0, 0.4);
  background-color: rgba(255, 149, 0, 0.08);
}

.dark .random-btn:hover {
  background-color: rgba(255, 149, 0, 0.18);
}

.random-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.4s ease;
}

.random-btn:hover .random-icon {
  transform: rotate(20deg) scale(1.15);
}


.filter-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.active-filters-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: var(--vp-c-brand-1);
  color: white;
  font-size: 0.72rem;
  font-weight: 700;
  min-width: 18px;
  height: 18px;
  padding: 0 5px;
  border-radius: 9px;
  margin-left: 2px;
}

/* Filter Panel Drawer */
.filter-panel {
  width: 100%;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
  margin-top: 0.5rem;
  box-sizing: border-box;
}

.filter-columns {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

@media (max-width: 768px) {
  .filter-columns {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

.filter-column {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.filter-column-title {
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--vp-c-text-2);
  margin: 0;
  padding-bottom: 0.5rem;
  border-bottom: 1px dashed var(--vp-c-border);
}

.filter-options {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

/* Checkbox & Radio styling */
.filter-option-label {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.9rem;
  color: var(--vp-c-text-1);
  cursor: pointer;
  user-select: none;
  position: relative;
  padding: 0.2rem 0;
  transition: color 0.2s ease;
}

.filter-option-label:hover {
  color: var(--vp-c-brand-1);
}

.filter-option-label input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Custom Checkbox */
.checkbox-custom {
  height: 16px;
  width: 16px;
  background-color: var(--vp-c-bg-mute);
  border: 1px solid var(--vp-c-border);
  border-radius: 4px;
  transition: all 0.2s ease;
  position: relative;
}

.filter-option-label input:checked ~ .checkbox-custom {
  background-color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
}

.checkbox-custom::after {
  content: "";
  position: absolute;
  display: none;
  left: 5px;
  top: 2px;
  width: 4px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.filter-option-label input:checked ~ .checkbox-custom::after {
  display: block;
}

/* Custom Radio */
.radio-custom {
  height: 16px;
  width: 16px;
  background-color: var(--vp-c-bg-mute);
  border: 1px solid var(--vp-c-border);
  border-radius: 50%;
  transition: all 0.2s ease;
  position: relative;
}

.filter-option-label input:checked ~ .radio-custom {
  border-color: var(--vp-c-brand-1);
}

.radio-custom::after {
  content: "";
  position: absolute;
  display: none;
  top: 4px;
  left: 4px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--vp-c-brand-1);
}

.filter-option-label input:checked ~ .radio-custom::after {
  display: block;
}

.option-text {
  flex: 1;
}

.option-count {
  font-size: 0.78rem;
  color: var(--vp-c-text-3);
  font-weight: 500;
  background-color: var(--vp-c-bg-mute);
  padding: 1px 6px;
  border-radius: 10px;
}

.filter-footer {
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--vp-c-border);
  display: flex;
  justify-content: flex-end;
}

.clear-filters-btn {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
  background: transparent;
  border: 1px solid var(--vp-c-border);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.clear-filters-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background-color: var(--vp-c-brand-soft);
}

/* slide-fade animation */
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.25s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}

/* Category Pills */
.category-pills {
  display: flex;
  gap: 0.8rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
  scrollbar-width: none;
}

.category-pills::-webkit-scrollbar {
  display: none;
}

.pill-btn {
  white-space: nowrap;
  padding: 0.4rem 1.2rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
  background-color: transparent;
  border: 1px solid var(--vp-c-border);
  cursor: pointer;
  transition: all 0.2s ease;
}

.pill-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.pill-btn.active {
  background-color: var(--vp-c-brand-1);
  color: white;
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 4px 12px rgba(24, 216, 103, 0.3);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  background: var(--vp-c-bg-soft);
  border-radius: 16px;
  border: 1px dashed var(--vp-c-border);
  margin-top: 1rem;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  opacity: 0.8;
}

.empty-state h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.2rem;
  color: var(--vp-c-text-1);
}

.empty-state p {
  margin: 0 0 1.5rem 0;
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
}

.reset-btn {
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  background: var(--vp-c-brand-1);
  color: white;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: opacity 0.2s;
}

.reset-btn:hover {
  opacity: 0.9;
}

/* Tool Grid */
.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

@media (max-width: 480px) {
  .tools-grid {
    grid-template-columns: 1fr;
  }
}

.tool-card {
  position: relative;
  background: var(--vp-c-bg-soft);
  border: 1px solid rgba(150, 150, 150, 0.15);
  border-radius: 20px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
  text-decoration: none !important;
  color: inherit !important;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.02);
}

.tool-card:hover {
  transform: scale(1.015) translateY(-2px);
  border-color: rgba(150, 150, 150, 0.3);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.06);
}

.card-glow {
  display: none;
}

.tool-card-header {
  position: relative;
  z-index: 1;
  display: flex;
  gap: 1.2rem;
  align-items: center;
}

.tool-icon-wrapper {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  flex-shrink: 0;
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.1);
}

.tool-meta-header h3 {
  margin: 0;
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.4;
  color: var(--vp-c-text-1);
}

.tech-tag {
  font-size: 0.75rem;
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
  padding: 2px 8px;
  border-radius: 4px;
  display: inline-block;
  margin-top: 0.5rem;
  font-weight: 600;
}

/* Time Badge */
.time-badge {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  font-size: 0.7rem;
  font-weight: 600;
  color: var(--vp-c-text-3);
  background: var(--vp-c-bg-mute);
  padding: 0.2rem 0.6rem;
  border-radius: 6px;
  pointer-events: none;
  z-index: 2;
}

.time-badge.is-new {
  color: #fff;
  background: linear-gradient(135deg, #FF6B6B, #FF8E53);
  box-shadow: 0 2px 8px rgba(255, 107, 107, 0.3);
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-3px); }
  100% { transform: translateY(0px); }
}

.tool-desc {
  position: relative;
  z-index: 1;
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0;
  min-height: 2.8em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.tool-footer {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid var(--vp-c-divider);
}

.stats {
  display: flex;
  gap: 1rem;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  font-weight: 500;
}

.visit-btn {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
  transition: transform 0.2s;
}

.tool-card:hover .visit-btn {
  transform: translateX(4px);
}

/* Right Sidebar: Ads */
.sponsor-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* Real Sponsor Card */
.real-sponsor-card {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  background: linear-gradient(145deg, rgba(184, 135, 70, 0.08) 0%, rgba(223, 195, 150, 0.05) 100%);
  border: 1px solid rgba(184, 135, 70, 0.35);
  border-radius: 12px;
  padding: 0.75rem 0.9rem;
  text-decoration: none !important;
  color: inherit !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.01);
}

.real-sponsor-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #b88746, #dfc396, #b88746);
}

.real-sponsor-card:hover {
  transform: translateY(-2px);
  border-color: rgba(184, 135, 70, 0.6);
  box-shadow: 0 6px 16px -4px rgba(184, 135, 70, 0.15);
}

.sponsor-header {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.sponsor-logo {
  font-size: 1.6rem;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(184, 135, 70, 0.08);
  border-radius: 8px;
  flex-shrink: 0;
}

.sponsor-meta {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  text-align: left;
  min-width: 0;
}

.sponsor-name {
  font-size: 0.95rem;
  font-weight: 700;
  margin: 0;
  color: var(--vp-c-text-1);
  line-height: 1.2;
}

.sponsor-tagline {
  font-size: 0.75rem;
  color: #b88746;
  font-weight: 500;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sponsor-action {
  margin-top: 0.5rem;
  padding-top: 0.4rem;
  border-top: 1px dashed rgba(150, 150, 150, 0.15);
  font-size: 0.78rem;
  font-weight: 700;
  color: #b88746;
  text-align: right;
  transition: transform 0.2s;
}

.real-sponsor-card:hover .sponsor-action {
  transform: translateX(2px);
}


</style>
