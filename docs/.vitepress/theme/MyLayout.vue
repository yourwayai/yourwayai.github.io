<script setup>
import DefaultTheme from 'vitepress/theme'
import ScrollToTopBottom from './components/ScrollToTopBottom.vue'
import SiteFooter from './components/SiteFooter.vue'
import { useData } from 'vitepress'
import { watch, onMounted, onUnmounted } from 'vue'

const { Layout } = DefaultTheme
const { page } = useData()

onMounted(() => {
  watch(() => page.value.relativePath, (path) => {
    if (path === 'index.md') {
      document.documentElement.classList.add('is-home')
    } else {
      document.documentElement.classList.remove('is-home')
    }
  }, { immediate: true })
})

onUnmounted(() => {
  document.documentElement.classList.remove('is-home')
})
</script>

<template>
  <Layout>
    <template #layout-bottom>
      <SiteFooter />
      <ScrollToTopBottom />
    </template>
  </Layout>
</template>
