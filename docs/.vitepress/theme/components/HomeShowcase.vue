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

        <!-- Control Bar -->
        <div class="control-bar">
          <div class="search-wrapper">
            <span class="search-icon">🔍</span>
            <input type="text" v-model="searchQuery" placeholder="搜索工具、专栏或关键字..." class="search-input" />
          </div>
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
          <a :href="tool.link" class="tool-card" v-for="tool in filteredTools" :key="tool.id">
            <div class="card-glow" :style="{ background: tool.iconBg }"></div>
            <div class="time-badge" v-if="getRelativeTime(tool.date)" :class="{ 'is-new': getRelativeTime(tool.date) === '✨ New' }">
              {{ getRelativeTime(tool.date) }}
            </div>
            <div class="tool-card-header">
              <div class="tool-icon-wrapper" :style="{ backgroundColor: tool.iconBg }">
                <span class="tool-icon-inner">{{ tool.icon }}</span>
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
          <button class="reset-btn" @click="searchQuery = ''; activeCategory = '全部'">重置过滤条件</button>
        </div>
      </main>

      <!-- Right Sidebar: Ads / Sponsored -->
      <aside class="sidebar right-sidebar">
        <h2 class="sidebar-title sponsor-title">👑 Sponsored</h2>

        <!-- Sponsor #1: YourWayCareer -->
        <a href="/sponsor/ywc-resume" target="_blank" rel="noopener" class="real-sponsor-card">
          <div class="real-sponsor-badge">✦ 赞助商 #1</div>
          <div class="real-sponsor-logo">📄</div>
          <h3 class="real-sponsor-name">YourWayCareer</h3>
          <p class="real-sponsor-tagline">高竞争岗位简历精修计划</p>
          <ul class="real-sponsor-points">
            <li>🎯 投行 · 咨询 · 外企管培</li>
            <li>✍️ Bullet Point 逐行改写</li>
            <li>🌐 英文简历精修</li>
          </ul>
          <div class="real-sponsor-cta">查看服务详情 →</div>
        </a>

        <div class="ad-card">
          <div class="ad-icon">⭐</div>
          <h3>Advertise Here</h3>
          <ul class="ad-benefits">
            <li>🚀 Reach 10,000+ monthly visitors</li>
            <li>• Highly engaged audience</li>
            <li>• Premium visibility</li>
          </ul>
          <button class="cta-btn">✉️ Get Started</button>
          <div class="ad-price">From $25/month</div>
        </div>
      </aside>
    </div>

    <!-- Custom Footer -->
    <footer class="custom-footer">
      <div class="footer-columns">
        <div class="footer-brand">
          <div class="footer-brand-header">
            <img src="/logo.jpg" alt="YourwayAI Logo" class="footer-logo">
            <h2>YourwayAI</h2>
          </div>
          <p>Discover and explore the best free and open-source software. Curated by the community, for the community.</p>
        </div>
        <div class="footer-links">
          <div class="link-group">
            <h3>Browse</h3>
            <a href="#">All Apps</a>
            <a href="#">Categories</a>
            <a href="#">Self-hosted</a>
            <a href="#">Latest Apps</a>
            <a href="#">Trending</a>
          </div>
          <div class="link-group">
            <h3>Quick Links</h3>
            <a href="#">Add Your App</a>
            <a href="#">JSON Editor</a>
            <a href="#">GitHub Repo</a>
            <a href="#">Report Issue</a>
            <a href="#">Contribute</a>
          </div>
          <div class="link-group">
            <h3>Resources</h3>
            <a href="#">Documentation</a>
            <a href="#">Changelog</a>
            <a href="#">Discussions</a>
            <a href="#">RSS Feed</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>Built with ❤️ by the community. Open source on GitHub.</p>
        <p>© 2026 YourwayAI. All apps belong to their respective owners.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'

// Use Vite's native glob import to read all markdown frontmatter
const modules = import.meta.glob('/tools/*.md', { eager: true })

// Simple color rotation for aesthetic card backgrounds
const colors = [
  'rgba(24, 216, 103, 0.1)',
  'rgba(255, 69, 0, 0.1)',
  'rgba(0, 191, 255, 0.1)',
  'rgba(138, 43, 226, 0.1)',
  'rgba(255, 215, 0, 0.1)'
]

const searchQuery = ref('')
const activeCategory = ref('全部')

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
    stars: '-',
    views: '-',
    added: 'New',
    platforms: [],
    date: fm.date || '2000-01-01'
  }
})

// Sort tools by date descending (newest first)
const allTools = rawTools.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())

// Compute unique categories
const uniqueCategories = computed(() => {
  const cats = new Set(allTools.map(t => t.category))
  return ['全部', ...Array.from(cats)]
})

// Compute filtered tools
const filteredTools = computed(() => {
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

// Helper for relative time (or "New" badge)
const getRelativeTime = (dateString) => {
  const date = new Date(dateString)
  if (isNaN(date.getTime())) return ''
  
  const now = new Date()
  const diffTime = now - date
  // Handle edge cases where date is slightly in the future due to timezone
  if (diffTime < 0) return '✨ New'
  
  const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))
  
  if (diffDays <= 7) return '✨ New'
  if (diffDays <= 30) return `${diffDays} 天前`
  if (diffDays <= 365) return `${Math.floor(diffDays / 30)} 个月前`
  return `${Math.floor(diffDays / 365)} 年前`
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
    display: none;
  }
}

/* Sidebar Styles */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
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
  background: linear-gradient(135deg, rgba(24, 216, 103, 0.1) 0%, rgba(24, 216, 103, 0.02) 100%);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 12px;
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 20px -5px rgba(24, 216, 103, 0.15);
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
  gap: 1.2rem;
  margin-bottom: 1.5rem;
}

.search-wrapper {
  position: relative;
  width: 100%;
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
  padding: 0.8rem 1rem 0.8rem 3rem;
  border-radius: 12px;
  border: 1px solid var(--vp-c-border);
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 1rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.search-input:focus {
  outline: none;
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 0 0 3px rgba(24, 216, 103, 0.15);
  background-color: var(--vp-c-bg);
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

.tool-card {
  position: relative;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none !important;
  color: inherit !important;
  overflow: hidden;
}

.card-glow {
  position: absolute;
  top: -20%;
  left: -20%;
  width: 140%;
  height: 140%;
  opacity: 0;
  filter: blur(40px);
  z-index: 0;
  transition: opacity 0.4s;
}

.tool-card:hover {
  transform: translateY(-5px);
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.2);
}

.tool-card:hover .card-glow {
  opacity: 0.05;
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
  font-size: 1.2rem;
  font-weight: 700;
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

.platform-tags {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.platform-tags span {
  font-size: 0.65rem;
  background-color: var(--vp-c-bg-mute);
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  border: 1px solid var(--vp-c-border);
  font-weight: 600;
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
  align-items: center;
  gap: 0.7rem;
  background: linear-gradient(145deg, rgba(184, 135, 70, 0.08) 0%, rgba(223, 195, 150, 0.05) 100%);
  border: 1.5px solid rgba(184, 135, 70, 0.5);
  border-radius: 14px;
  padding: 1.4rem 1.2rem;
  text-align: center;
  text-decoration: none !important;
  color: inherit !important;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
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
  transform: translateY(-3px);
  border-color: rgba(184, 135, 70, 0.9);
  box-shadow: 0 12px 30px -8px rgba(184, 135, 70, 0.25);
}

.real-sponsor-badge {
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: #b88746;
  background: rgba(184, 135, 70, 0.12);
  padding: 0.2rem 0.6rem;
  border-radius: 20px;
  text-transform: uppercase;
}

.real-sponsor-logo {
  font-size: 2.2rem;
  margin: 0.2rem 0;
}

.real-sponsor-name {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0;
  color: var(--vp-c-text-1);
}

.real-sponsor-tagline {
  font-size: 0.82rem;
  color: #b88746;
  font-weight: 600;
  margin: 0;
}

.real-sponsor-points {
  list-style: none;
  padding: 0;
  margin: 0.3rem 0;
  text-align: left;
  font-size: 0.78rem;
  color: var(--vp-c-text-2);
  line-height: 1.8;
  width: 100%;
}

.real-sponsor-cta {
  margin-top: 0.4rem;
  font-size: 0.82rem;
  font-weight: 700;
  color: #b88746;
  transition: transform 0.2s;
}

.real-sponsor-card:hover .real-sponsor-cta {
  transform: translateX(3px);
}

.ad-card {
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
}

.ad-card h3 {
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
}

.ad-icon {
  font-size: 2rem;
}

.ad-benefits {
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: left;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  line-height: 1.6;
}

.cta-btn {
  width: 100%;
  padding: 0.6rem;
  background-color: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-border);
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cta-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.ad-price {
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
}

/* Custom Footer */
.custom-footer {
  margin-top: 5rem;
  padding-top: 3rem;
  border-top: 1px solid var(--vp-c-border);
  color: var(--vp-c-text-2);
}

.footer-columns {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 3rem;
  margin-bottom: 3rem;
}

.footer-brand {
  max-width: 300px;
}

.footer-brand-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 1rem;
}

.footer-logo {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  object-fit: cover;
}

.footer-brand h2 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0;
  color: var(--vp-c-text-1);
}

.footer-brand p {
  font-size: 0.9rem;
  line-height: 1.6;
}

.footer-links {
  display: flex;
  gap: 4rem;
  flex-wrap: wrap;
}

.link-group h3 {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 1rem;
}

.link-group a {
  display: block;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  text-decoration: none;
  margin-bottom: 0.6rem;
  transition: color 0.2s;
}

.link-group a:hover {
  color: var(--vp-c-brand-1);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1.5rem;
  border-top: 1px solid var(--vp-c-border);
  font-size: 0.8rem;
}

@media (max-width: 600px) {
  .footer-columns {
    flex-direction: column;
  }
  .footer-bottom {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
}
</style>
