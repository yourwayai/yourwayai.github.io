<script setup>
import { useData } from 'vitepress'
import { computed } from 'vue'

const { frontmatter } = useData()
const isHome = computed(() => frontmatter.value.layout === 'home')
</script>

<template>
  <footer class="site-footer" :class="{ 'has-sidebar': !isHome }">
    <div class="footer-inner">
      <div class="footer-top">
        <!-- Left: SEO Optimized Brand Section -->
        <div class="footer-brand-section">
          <div class="footer-brand">
            <img src="/logo.jpg" alt="YourwayAI - 高质量开源软件与AI前沿工具导航站" class="footer-logo" />
            <span class="footer-name">YourwayAI</span>
          </div>
          <!-- 使用 h2 有利于 SEO，通过 CSS 重置为其表现为普通段落 -->
          <h2 class="footer-tagline">
            YourwayAI 致力于打造最纯粹的极客导航站。我们持续挖掘、聚合全球优质的<strong>开源软件</strong>、<strong>AI 前沿工具</strong>与高效生产力神器，打破技术信息差，与千万开发者共同拥抱开源生态。
          </h2>
        </div>

        <!-- Right: Links Section -->
        <div class="footer-links-section">
          <div class="footer-links-column">
            <h3 class="footer-column-title">支持我们</h3>
            <a href="/ywc_resume_landing_page.html" target="_blank" rel="noopener" class="footer-link sponsor-link">🏅 成为赞助商</a>
          </div>
          <div class="footer-links-column">
            <h3 class="footer-column-title">关注动态</h3>
            <a href="https://x.com" target="_blank" rel="noopener" class="footer-link">X (Twitter)</a>
            <a href="https://threads.net" target="_blank" rel="noopener" class="footer-link">Threads</a>
          </div>
          <div class="footer-links-column">
            <h3 class="footer-column-title">生态推荐</h3>
            <a href="https://github.com" target="_blank" rel="noopener" class="footer-link">GitHub</a>
            <a href="https://openai.com" target="_blank" rel="noopener" class="footer-link">OpenAI</a>
            <a href="https://gemini.google.com" target="_blank" rel="noopener" class="footer-link">Gemini</a>
            <a href="https://claude.ai" target="_blank" rel="noopener" class="footer-link">Claude</a>
          </div>
        </div>
      </div>

      <div class="footer-divider"></div>

      <div class="footer-bottom">
        <span class="footer-copyright">© 2026-present YourwayAI. All rights reserved.</span>
        <a href="mailto:brucemi@yourwaycareer.com" class="footer-contact">
          <span class="contact-icon">✉️</span>
          brucemi@yourwaycareer.com
        </a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  margin-top: 3rem;
  border-top: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  padding: 3rem 1.5rem 2.5rem;
  width: 100%;
  box-sizing: border-box;
  transition: padding-left 0.25s ease;
}

@media (min-width: 960px) {
  .site-footer.has-sidebar {
    padding-left: calc(var(--vp-sidebar-width, 279px) + 1.5rem);
  }
}

.footer-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  width: 100%;
  box-sizing: border-box;
}

.footer-top {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 3rem;
  width: 100%;
}

/* Brand Section */
.footer-brand-section {
  flex: 1 1 400px;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.footer-logo {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  object-fit: cover;
}

.footer-name {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  letter-spacing: -0.01em;
}

.footer-tagline {
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.7;
  font-weight: 400;
}

.footer-tagline strong {
  color: var(--vp-c-text-1);
  font-weight: 600;
}

/* Links Section */
.footer-links-section {
  flex: 1 1 400px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 2rem;
}

.footer-links-column {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.footer-column-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  margin: 0 0 0.2rem 0;
}

.footer-link {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: var(--vp-c-brand-1);
}

.sponsor-link {
  color: var(--vp-c-brand-1);
  font-weight: 600;
}

/* Divider */
.footer-divider {
  width: 100%;
  height: 1px;
  background: var(--vp-c-divider);
}

/* Bottom row */
.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.footer-copyright {
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
}

.footer-contact {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.85rem;
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 600;
  transition: opacity 0.2s;
}

.footer-contact:hover {
  opacity: 0.75;
}

.contact-icon {
  font-size: 0.9rem;
}

/* Responsive */
@media (max-width: 768px) {
  .footer-top {
    gap: 2.5rem;
  }
  
  .footer-brand-section {
    max-width: 100%;
    align-items: center;
    text-align: center;
  }
  
  .footer-links-section {
    grid-template-columns: repeat(2, 1fr);
    text-align: center;
  }
  
  .footer-bottom {
    justify-content: center;
    text-align: center;
  }
}
</style>
