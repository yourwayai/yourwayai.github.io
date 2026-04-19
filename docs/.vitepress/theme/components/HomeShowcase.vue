<template>
  <div class="home-showcase-container">
    <div class="showcase-content">
      
      <!-- Left Sidebar: Categories -->
      <aside class="sidebar categories-sidebar">
        <h2 class="sidebar-title">Categories</h2>
        <div class="category-group">
          <div class="group-title">PLATFORM & INFRASTRUCTURE</div>
          <ul class="category-list">
            <li>
              <div class="cat-label"><span class="icon">💻</span> Backend</div>
              <span class="cat-count">5</span>
            </li>
            <li>
              <div class="cat-label"><span class="icon">☁️</span> Cloud & Object Storage</div>
              <span class="cat-count">4</span>
            </li>
            <li>
              <div class="cat-label"><span class="icon">🐳</span> Containers & Docker</div>
              <span class="cat-count">23</span>
            </li>
            <li class="active">
              <div class="cat-label"><span class="icon">📊</span> Dashboards & Visualization</div>
              <span class="cat-count">39</span>
            </li>
            <li>
              <div class="cat-label"><span class="icon">🗄️</span> Databases</div>
              <span class="cat-count">24</span>
            </li>
            <li>
              <div class="cat-label"><span class="icon">🚀</span> Deployment & CI/CD</div>
              <span class="cat-count">16</span>
            </li>
            <li>
              <div class="cat-label"><span class="icon">🌐</span> Web Platforms</div>
              <span class="cat-count">40</span>
            </li>
          </ul>
        </div>
        
        <div class="category-group">
          <div class="group-title">DEVELOPMENT</div>
          <ul class="category-list">
            <li>
              <div class="cat-label"><span class="icon">👨‍💻</span> Code & Development</div>
              <span class="cat-count">40</span>
            </li>
          </ul>
        </div>

        <div class="category-group">
          <div class="group-title">NETWORKING</div>
          <ul class="category-list">
            <li>
              <div class="cat-label"><span class="icon">📡</span> Networking</div>
              <span class="cat-count">54</span>
            </li>
          </ul>
        </div>
      </aside>

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

        <header class="main-header">
          <div class="header-title">
            <h2>📈 Trending</h2>
            <span class="tagline">Last 30 Days</span>
          </div>
          <div class="header-actions">
            <button class="text-btn">More</button>
            <button class="primary-btn">View All</button>
          </div>
        </header>

        <div class="tabs">
          <button class="tab active">📈 Trending</button>
          <button class="tab">🗓️ Newest</button>
          <button class="tab">⭐ Popular</button>
        </div>

        <div class="tools-grid">
          <!-- Card 1 -->
          <div class="tool-card" v-for="tool in tools" :key="tool.id">
            <div class="tool-card-header">
              <div class="tool-icon" :style="{ backgroundColor: tool.iconBg }">{{ tool.icon }}</div>
              <div class="tool-meta-header">
                <h3>{{ tool.name }}</h3>
                <span class="tech-tag">{{ tool.category }}</span>
              </div>
            </div>
            <p class="tool-desc">{{ tool.desc }}</p>
            <div class="tool-footer">
              <div class="stats">
                <span>⭐ {{ tool.stars }}</span>
                <span>👁️ {{ tool.views }}</span>
              </div>
              <div class="added-time">Added {{ tool.added }} ago</div>
            </div>
            <div class="platform-tags">
              <span v-for="plat in tool.platforms" :key="plat">{{ plat }}</span>
            </div>
          </div>
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
import { ref } from 'vue'

const tools = ref([
  { id: 1, name: 'stirling-pdf', category: 'System Utilities', icon: 'S', iconBg: '#ff4c4c', desc: 'An all-in-one web-based toolkit for editing and manipulation of PDF files...', stars: '75.0k', views: '557', added: '4mo', platforms: ['PVE', 'Yuno', 'TrueNAS'] },
  { id: 2, name: 'cert-warden', category: 'Security & Privacy', icon: '🔒', iconBg: '#0ea5e9', desc: 'A certificate management tool for issuing and managing SSL/TLS certificates...', stars: '489', views: '356', added: '4mo', platforms: [] },
  { id: 3, name: 'immich', category: 'Media Streaming', icon: '📷', iconBg: '#8b5cf6', desc: 'A self-hosted photo and video backup platform with a premium mobile UI app...', stars: '94.1k', views: '329', added: '4mo', platforms: ['PVE', 'Yuno', 'TrueNAS'] },
  { id: 4, name: 'memos', category: 'Notes & Knowledge Base', icon: '📝', iconBg: '#facc15', desc: 'A lightweight self-hosted note-taking and knowledge management system...', stars: '57.5k', views: '317', added: '4mo', platforms: ['PVE', 'Yuno', 'TrueNAS'] },
  { id: 5, name: 'windmill', category: 'Automation & Workflows', icon: '⚡', iconBg: '#3b82f6', desc: 'A developer platform for building workflows, APIs, and scalable apps...', stars: '15.7k', views: '296', added: '4mo', platforms: ['TrueNAS'] },
  { id: 6, name: 'checkmate', category: 'Observability', icon: '♟️', iconBg: '#14b8a6', desc: 'A self-hosted platform for monitoring service uptime, APIs, and SSL statuses...', stars: '9.4k', views: '276', added: '4mo', platforms: ['PVE'] },
  { id: 7, name: 'outline', category: 'Notes & Knowledge Base', icon: '📓', iconBg: '#f43f5e', desc: 'A modern self-hosted wiki and team knowledge base for growing teams...', stars: '37.5k', views: '270', added: '4mo', platforms: ['PVE', 'Yuno', 'TrueNAS'] },
  { id: 8, name: 'coolify', category: 'Deployment & CI/CD', icon: '☁️', iconBg: '#a855f7', desc: 'A self-hosted platform for deploying applications and databases easily...', stars: '51.4k', views: '283', added: '4mo', platforms: ['PVE', 'TrueNAS'] },
  { id: 9, name: 'appwrite', category: 'Backend', icon: '🅰️', iconBg: '#ef4444', desc: 'A backend platform providing authentication, database functionality, and more...', stars: '55.0k', views: '260', added: '4mo', platforms: [] }
])
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
  grid-template-columns: 260px 1fr 280px;
  gap: 2rem;
  align-items: start;
}

@media (max-width: 1100px) {
  .showcase-content {
    grid-template-columns: 260px 1fr;
  }
  .right-sidebar {
    display: none;
  }
}

@media (max-width: 800px) {
  .showcase-content {
    grid-template-columns: 1fr;
  }
  .categories-sidebar, .right-sidebar {
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

.category-group {
  margin-top: 0.5rem;
}

.group-title {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
  margin-bottom: 0.75rem;
  letter-spacing: 0.05em;
}

.category-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.category-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.category-list li:hover {
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
}

.category-list li.active {
  background-color: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  font-weight: 600;
}

.cat-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.cat-count {
  background-color: var(--vp-c-bg-mute);
  padding: 0.1rem 0.4rem;
  border-radius: 10px;
  font-size: 0.75rem;
  min-width: 24px;
  text-align: center;
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


.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-title {
  display: flex;
  align-items: baseline;
  gap: 1rem;
}

.header-title h2 {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.tagline {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  background-color: var(--vp-c-bg-soft);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.header-actions {
  display: flex;
  gap: 1rem;
}

.header-actions button {
  padding: 0.4rem 1rem;
  font-size: 0.9rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}

.text-btn {
  background: transparent;
  color: var(--vp-c-text-1);
}

.text-btn:hover {
  background-color: var(--vp-c-bg-soft);
}

.primary-btn {
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  border-color: var(--vp-c-border);
}

.primary-btn:hover {
  background-color: var(--vp-c-bg-mute);
}

/* Tabs */
.tabs {
  display: flex;
  gap: 0.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--vp-c-border);
}

.tab {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--vp-c-text-2);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.tab:hover {
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
}

.tab.active {
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  border-color: var(--vp-c-border);
}

/* Tool Grid */
.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.2rem;
}

.tool-card {
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  position: relative;
  overflow: hidden;
}

.tool-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px -10px rgba(0,0,0,0.15);
  border-color: var(--vp-c-brand-1);
}

.tool-card-header {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.tool-icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
  flex-shrink: 0;
}

.tool-meta-header h3 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  line-height: 1.2;
}

.tech-tag {
  font-size: 0.7rem;
  color: var(--vp-c-text-2);
  background: var(--vp-c-default-soft);
  border: 1px solid var(--vp-c-border);
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  display: inline-block;
  margin-top: 0.4rem;
}

.tool-desc {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  line-height: 1.5;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.tool-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
  margin-top: auto;
}

.stats {
  display: flex;
  gap: 0.8rem;
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
