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

        <div class="tools-grid">
          <a :href="tool.link" class="tool-card" v-for="tool in allTools" :key="tool.id">
            <div class="card-glow" :style="{ background: tool.iconBg }"></div>
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
      </main>

      <!-- Right Sidebar: Ads / Sponsored -->
      <aside class="sidebar right-sidebar">
        <h2 class="sidebar-title sponsor-title">👑 Sponsored Tools</h2>
        
        <div class="sponsor-card">
          <div class="sponsor-icon">👑</div>
          <h3>5 Spots Available</h3>
          <p>Be the first to sponsor!</p>
        </div>

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
          <h2>YourwayAI</h2>
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
import { computed } from 'vue'

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

const allTools = computed(() => {
  return Object.entries(modules).map(([path, mod], index) => {
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
      platforms: []
    }
  })
})

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

.sponsor-card, .ad-card {
  background-color: var(--vp-c-bg-soft);
  border: 1px dashed var(--vp-c-border);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
}

.sponsor-card h3, .ad-card h3 {
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
}

.sponsor-card p {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  margin: 0;
}

.sponsor-icon, .ad-icon {
  font-size: 2rem;
}

.ad-card {
  border-style: solid;
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

.footer-brand h2 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
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
