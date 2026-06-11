<template>
  <div class="github-repo-card">
    <div class="repo-header">
      <img :src="avatarUrl" style="width: 48px; height: 48px; border-radius: 10px; flex-shrink: 0;" />
      <div class="repo-meta">
        <h4 class="repo-name">{{ repo }}</h4>
        <div class="repo-meta-sub">
          <span class="repo-badge" v-if="license">{{ license }}</span>
          <span class="repo-badge version" v-if="version">{{ version }}</span>
          <span class="repo-time" v-if="pushedAt">{{ updatedAtStr }}</span>
        </div>
      </div>
    </div>
    
    <div class="repo-stats">
      <div class="stat-item">
        <span class="stat-value">⭐ {{ starsStr }}</span>
        <span class="stat-label">Stars</span>
      </div>
      <div class="stat-item">
        <span class="stat-value">🍴 {{ forksStr }}</span>
        <span class="stat-label">Forks</span>
      </div>
      <div class="stat-item">
        <span class="stat-value">👥 {{ contributorsStr }}</span>
        <span class="stat-label">Contributors</span>
      </div>
      <div class="stat-item" v-if="releasesCount !== null">
        <span class="stat-value">📦 {{ releasesCount }}</span>
        <span class="stat-label">Releases</span>
      </div>
    </div>

    <div class="repo-specs" v-if="platforms.length || deployments.length">
      <div class="spec-section" v-if="platforms.length">
        <span class="spec-title">支持系统</span>
        <div class="tag-group">
          <span class="tag platform" v-for="p in platforms" :key="p">{{ p }}</span>
        </div>
      </div>
      <div class="spec-section" v-if="deployments.length">
        <span class="spec-title">部署与安装</span>
        <div class="tag-group">
          <span class="tag deployment" v-for="d in deployments" :key="d">{{ d }}</span>
        </div>
      </div>
    </div>

    <div class="repo-links">
      <a :href="`https://github.com/${repo}`" target="_blank" rel="noopener" class="link-btn primary">GitHub 源码</a>
      <a :href="docsUrl || `https://github.com/${repo}#readme`" target="_blank" rel="noopener" class="link-btn">使用文档</a>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const props = defineProps({
  repo: { type: String, required: true },
  initialStars: { type: String, default: 'N/A' },
  initialForks: { type: String, default: 'N/A' },
  initialContributors: { type: String, default: 'N/A' },
  initialLicense: { type: String, default: 'MIT License' },
  initialVersion: { type: String, default: 'v0.2.1' },
  initialPushedAt: { type: String, default: '' },
  platforms: { type: Array, default: () => [] },
  deployments: { type: Array, default: () => [] },
  docsUrl: { type: String, default: '' },
  logoUrl: { type: String, default: '' }
})

const stars = ref(props.initialStars)
const forks = ref(props.initialForks)
const contributors = ref(props.initialContributors)
const license = ref(props.initialLicense)
const version = ref(props.initialVersion)
const pushedAt = ref(props.initialPushedAt)
const releasesCount = ref(null)

const avatarUrl = computed(() => {
  if (props.logoUrl) return props.logoUrl
  const parts = props.repo.split('/')
  return parts.length ? `https://github.com/${parts[0]}.png` : ''
})

const formatNumber = (num) => {
  if (num >= 1000000) return `${(num/1000000).toFixed(1)}M`
  if (num >= 1000) return `${(num/1000).toFixed(1)}k`
  return num.toString()
}

const formatTimeDiff = (dateString) => {
  const date = new Date(dateString)
  if (isNaN(date.getTime())) return ''
  const diff = new Date() - date
  const diffDays = Math.floor(diff / (1000 * 60 * 60 * 24))
  if (diffDays < 1) return 'today'
  if (diffDays <= 30) return `${diffDays} days ago`
  if (diffDays <= 365) return `${Math.floor(diffDays / 30)} months ago`
  return `${Math.floor(diffDays / 365)} years ago`
}

const updatedAtStr = computed(() => {
  if (!pushedAt.value) return ''
  if (pushedAt.value.includes('T') || pushedAt.value.includes('-')) {
    return formatTimeDiff(pushedAt.value)
  }
  return pushedAt.value
})

const starsStr = computed(() => typeof stars.value === 'number' ? formatNumber(stars.value) : stars.value)
const forksStr = computed(() => typeof forks.value === 'number' ? formatNumber(forks.value) : forks.value)
const contributorsStr = computed(() => typeof contributors.value === 'number' ? formatNumber(contributors.value) : contributors.value)

onMounted(async () => {
  try {
    const res = await fetch(`https://api.github.com/repos/${props.repo}`)
    if (res.status === 200) {
      const data = await res.json()
      stars.value = data.stargazers_count
      forks.value = data.forks_count
      if (data.license) license.value = data.license.spdx_id
      pushedAt.value = data.pushed_at
    }
    
    // Fetch latest release
    const relRes = await fetch(`https://api.github.com/repos/${props.repo}/releases/latest`)
    if (relRes.status === 200) {
      const relData = await relRes.json()
      version.value = relData.tag_name
    }
    
    // Fetch contributors count
    const contribRes = await fetch(`https://api.github.com/repos/${props.repo}/contributors?per_page=1`)
    if (contribRes.status === 200) {
      const link = contribRes.headers.get('Link')
      if (link) {
        const match = link.match(/page=(\d+)>; rel="last"/)
        if (match) contributors.value = parseInt(match[1])
      }
    }
  } catch (e) {
    console.error('Failed to fetch live GitHub stats:', e)
  }
})
</script>
