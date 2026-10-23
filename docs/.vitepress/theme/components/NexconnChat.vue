<script setup>
// NexconnChat.vue — 放到 docs/.vitepress/theme/components/
// 作用: 右下角浮动聊天窗, 访客以 guest 身份和站长 1 对 1 发消息
// 依赖: npm install @nexconn/engine@latest @nexconn/chat@latest -S
// 构建变量 (GitHub Actions / 本地 .env):
//   VITE_NEXCONN_APP_KEY     Nexconn App Key (前端可见, 可以公开)
//   VITE_NEXCONN_TOKEN_API   Cloudflare Worker 地址, 如 https://nexconn-token-yourwayai.<你>.workers.dev/token
//   VITE_NEXCONN_OWNER_ID    站长 userId, 默认 yourwayai-owner
import { ref, onMounted } from 'vue'

const APP_KEY = import.meta.env.VITE_NEXCONN_APP_KEY
const TOKEN_API = import.meta.env.VITE_NEXCONN_TOKEN_API
const OWNER_ID = import.meta.env.VITE_NEXCONN_OWNER_ID || 'yourwayai-owner'

const open = ref(false)
const connected = ref(false)
const sending = ref(false)
const input = ref('')
const messages = ref([]) // {from: 'me'|'owner', text}
let channel = null

function guestId() {
  let id = localStorage.getItem('nexconn_guest_id')
  if (!id) {
    id = 'guest-' + Math.random().toString(36).slice(2, 12)
    localStorage.setItem('nexconn_guest_id', id)
  }
  return id
}

async function ensureConnected() {
  if (connected.value || !APP_KEY || !TOKEN_API) return
  const { NCEngine, DirectChannel, MessageHandler } = await import('@nexconn/chat')

  const userId = guestId()
  const r = await fetch(TOKEN_API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ userId, name: '网站访客' }),
  })
  const { accessToken } = await r.json()
  if (!accessToken) throw new Error('token failed')

  // Web SDK 全生命周期只初始化一次, 本组件在 Layout 里全局挂载, 天然只跑一次
  NCEngine.initialize({ appKey: APP_KEY })
  NCEngine.addMessageHandler('site-chat', new MessageHandler({
    onMessageReceived({ messages: incoming }) {
      for (const m of incoming || []) {
        if (m?.content?.text) messages.value.push({ from: 'owner', text: m.content.text })
      }
    },
  }))
  const result = await NCEngine.connect({ token: accessToken })
  if (result.code !== 0) throw new Error('connect failed: ' + result.code)

  channel = new DirectChannel(OWNER_ID)
  connected.value = true
}

async function send() {
  const text = input.value.trim()
  if (!text || sending.value) return
  sending.value = true
  try {
    await ensureConnected()
    const { SendTextMessageParams } = await import('@nexconn/chat')
    await channel.sendMessage(new SendTextMessageParams({ text }))
    messages.value.push({ from: 'me', text })
    input.value = ''
  } catch (e) {
    messages.value.push({ from: 'owner', text: '发送失败, 请稍后再试或通过关于页的邮箱联系我们。' })
    console.error(e)
  } finally {
    sending.value = false
  }
}

function toggle() {
  open.value = !open.value
  if (open.value) ensureConnected().catch(console.error)
}
</script>

<template>
  <div class="nc-wrap">
    <div v-if="open" class="nc-panel">
      <div class="nc-head">在线咨询 <span>{{ connected ? '已连接' : '连接中…' }}</span></div>
      <div class="nc-body">
        <div v-for="(m, i) in messages" :key="i" :class="['nc-msg', m.from]">{{ m.text }}</div>
        <div v-if="!messages.length" class="nc-hint">你好, 有什么想问的? 直接发消息, 站长上线后会回复。</div>
      </div>
      <div class="nc-foot">
        <input v-model="input" placeholder="输入消息…" @keyup.enter="send" />
        <button :disabled="sending" @click="send">发送</button>
      </div>
    </div>
    <button class="nc-btn" @click="toggle">{{ open ? '✕' : '💬 咨询' }}</button>
  </div>
</template>

<style scoped>
.nc-wrap { position: fixed; right: 20px; bottom: 88px; z-index: 99; display: flex; flex-direction: column; align-items: flex-end; gap: 10px; }
.nc-btn { border: 0; border-radius: 999px; padding: 10px 18px; background: #18d867; color: #fff; font-weight: 600; cursor: pointer; box-shadow: 0 8px 24px rgba(0,0,0,.18); }
.nc-panel { width: 320px; max-width: 86vw; height: 420px; display: flex; flex-direction: column; background: var(--vp-c-bg); border: 1px solid var(--vp-c-border); border-radius: 14px; overflow: hidden; box-shadow: 0 16px 40px rgba(0,0,0,.22); }
.nc-head { padding: 10px 14px; font-weight: 600; border-bottom: 1px solid var(--vp-c-border); display: flex; justify-content: space-between; }
.nc-head span { font-weight: 400; font-size: 12px; opacity: .7; }
.nc-body { flex: 1; overflow-y: auto; padding: 12px; display: flex; flex-direction: column; gap: 8px; }
.nc-msg { max-width: 82%; padding: 8px 11px; border-radius: 10px; font-size: 14px; line-height: 1.45; white-space: pre-wrap; }
.nc-msg.me { align-self: flex-end; background: #18d867; color: #fff; }
.nc-msg.owner { align-self: flex-start; background: var(--vp-c-bg-soft); }
.nc-hint { font-size: 13px; opacity: .75; }
.nc-foot { display: flex; gap: 8px; padding: 10px; border-top: 1px solid var(--vp-c-border); }
.nc-foot input { flex: 1; border: 1px solid var(--vp-c-border); border-radius: 8px; padding: 8px 10px; background: var(--vp-c-bg); color: var(--vp-c-text-1); }
.nc-foot button { border: 0; border-radius: 8px; padding: 8px 14px; background: #18d867; color: #fff; cursor: pointer; }
</style>
