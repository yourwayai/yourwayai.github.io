<script setup>
import DefaultTheme from 'vitepress/theme'
import ScrollToTopBottom from './components/ScrollToTopBottom.vue'
import SiteFooter from './components/SiteFooter.vue'

const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #doc-footer-before>
      <SiteFooter />
    </template>
    <template #layout-bottom>
      <ScrollToTopBottom />
    </template>
  </Layout>
</template>
