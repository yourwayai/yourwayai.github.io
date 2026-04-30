<script setup>
import DefaultTheme from 'vitepress/theme'
import ScrollToTopBottom from './components/ScrollToTopBottom.vue'
import SiteFooter from './components/SiteFooter.vue'

const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #layout-bottom>
      <SiteFooter />
      <ScrollToTopBottom />
    </template>
  </Layout>
</template>
