<script setup>
// OwnerChat.vue — 站长收件箱, 放到 docs/.vitepress/theme/components/
// 页面: docs/owner.md, 地址 /owner (不挂导航, 靠站长口令保护)
// 流程: 输站长口令 -> Worker 校验后发站长 token -> 连上 Nexconn -> 左边会话列表, 右边点开回复
import { ref } from 'vue'

const APP_KEY = import.meta.env.VITE_NEXCONN_APP_KEY
const TOKEN_API = import.meta.env.VITE_NEXCONN_TOKEN_API
const OWNER_ID = import.meta.env.VITE_NEXCONN_OWNER_ID || 'yourwayai-owner'

const code = ref('')
const loggedIn = ref(false)
const loginError = ref('')
const channels = ref([]) // {id, unread, lastText, lastTime}
const current = ref('') // 当前打开的访客 userId
const messages = ref([]) // {from:'me'|'guest', text}
const input = ref('')
const sending = ref(false)
let sdk = null

function fmtTime(ts) {
  if (!ts) return ''
  try { return new Date(ts).toLocaleString() } catch { return '' }
}

async function loadChannels() {
  const { BaseChannel } = sdk
  const query = BaseChannel.createChannelsQuery({ pageSize: 50 })
  const result = await query.loadNextPage()
  if (!result.isOk) return
  const list = (result.data?.data || [])
    .filter(c => c.channelType === 1 || String(c.channelType).includes('DIRECT') || c.channelId)
    .map(c => ({
      id: c.channelId,
      unread: c.unreadCount || 0,
      lastText: c.latestMessage?.content?.text || '',
      lastTime: c.latestMessage?.sentTime || c.operationTime || 0,
    }))
    .filter(c => c.id && c.id !== OWNER_ID)
  channels.value = list
}

async function openChannel(guestId) {
  current.value = guestId
  messages.value = []
  const { BaseChannel, DirectChannelIdentifier } = sdk
  const query = BaseChannel.createMessagesQuery({
    channelIdentifier: new DirectChannelIdentifier(guestId),
    isAscending: true,
    pageSize: 50,
  })
  const result = await query.loadNextPage()
  if (result.isOk) {
    messages.value = (result.data?.data || [])
      .filter(m => m?.content?.text)
      .map(m => ({ from: m.senderUserId === OWNER_ID ? 'me' : 'guest', text: m.content.text }))
  }
}

async function login() {
  loginError.value = ''
  try {
    const r = await fetch(TOKEN_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ userId: OWNER_ID, name: '站长', ownerCode: code.value }),
    })
    const data = await r.json()
    if (!r.ok || !data.accessToken) throw new Error(data.error || '登录失败')

    sdk = await import('@nexconn/chat')
    const { NCEngine, MessageHandler } = sdk
    NCEngine.initialize({ appKey: APP_KEY })
    NCEngine.addMessageHandler('owner-inbox', new MessageHandler({
      onMessageReceived({ messages: incoming }) {
        for (const m of incoming || []) {
          if (m?.content?.text && m.senderUserId === current.value) {
            messages.value.push({ from: 'guest', text: m.content.text })
          }
        }
        loadChannels().catch(() => {})
      },
    }))
    const result = await NCEngine.connect({ token: data.accessToken })
    if (result.code !== 0) throw new Error('连接失败: ' + result.code)
    loggedIn.value = true
    await loadChannels()
  } catch (e) {
    loginError.value = '登录失败: ' + (e.message || e) + ' (先确认 Worker 已更新并设置了 OWNER_CODE)'
  }
}

async function send() {
  const text = input.value.trim()
  if (!text || !current.value || sending.value) return
  sending.value = true
  try {
    const { DirectChannel, SendTextMessageParams } = sdk
    const channel = new DirectChannel(current.value)
    await channel.sendMessage(new SendTextMessageParams({ text }))
    messages.value.push({ from: 'me', text })
    input.value = ''
    loadChannels().catch(() => {})
  } finally {
    sending.value = false
  }
}
</script>

<template>
  <div class="oc-wrap">
    <div v-if="!loggedIn" class="oc-login">
      <h3>站长收件箱</h3>
      <p>输入你在 Cloudflare Worker 里设置的站长口令 (OWNER_CODE)。</p>
      <input v-model="code" type="password" placeholder="站长口令" @keyup.enter="login" />
      <button @click="login">登录</button>
      <p v-if="loginError" class="oc-err">{{ loginError }}</p>
    </div>

    <div v-else class="oc-main">
      <div class="oc-list">
        <div class="oc-list-head">访客会话 <button @click="loadChannels">刷新</button></div>
        <div v-if="!channels.length" class="oc-empty">暂时没有访客消息。</div>
        <button v-for="c in channels" :key="c.id" :class="['oc-item', { active: c.id === current }]" @click="openChannel(c.id)">
          <span class="oc-id">{{ c.id }}</span>
          <span v-if="c.unread" class="oc-badge">{{ c.unread }}</span>
          <span class="oc-last">{{ c.lastText }}</span>
          <span class="oc-time">{{ fmtTime(c.lastTime) }}</span>
        </button>
      </div>
      <div class="oc-chat">
        <div v-if="!current" class="oc-empty">点左边一个访客, 就能看聊天记录并回复。</div>
        <template v-else>
          <div class="oc-body">
            <div v-for="(m, i) in messages" :key="i" :class="['oc-msg', m.from]">{{ m.text }}</div>
          </div>
          <div class="oc-foot">
            <input v-model="input" placeholder="回复这个访客…" @keyup.enter="send" />
            <button :disabled="sending" @click="send">发送</button>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<style scoped>
.oc-wrap { max-width: 960px; margin: 24px auto; }
.oc-login { border: 1px solid var(--vp-c-border); border-radius: 14px; padding: 24px; display: flex; flex-direction: column; gap: 12px; max-width: 420px; margin: 0 auto; }
.oc-login input { border: 1px solid var(--vp-c-border); border-radius: 8px; padding: 10px; background: var(--vp-c-bg); color: var(--vp-c-text-1); }
.oc-login button, .oc-foot button, .oc-list-head button { border: 0; border-radius: 8px; padding: 9px 16px; background: #18d867; color: #fff; cursor: pointer; font-weight: 600; }
.oc-err { color: #e5484d; font-size: 14px; }
.oc-main { display: flex; gap: 14px; border: 1px solid var(--vp-c-border); border-radius: 14px; overflow: hidden; min-height: 480px; }
.oc-list { width: 280px; border-right: 1px solid var(--vp-c-border); display: flex; flex-direction: column; }
.oc-list-head { padding: 12px; font-weight: 600; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--vp-c-border); }
.oc-item { display: flex; flex-direction: column; gap: 2px; align-items: flex-start; text-align: left; padding: 10px 12px; background: transparent; border: 0; border-bottom: 1px solid var(--vp-c-border); cursor: pointer; color: var(--vp-c-text-1); width: 100%; }
.oc-item.active { background: var(--vp-c-bg-soft); }
.oc-id { font-weight: 600; font-size: 14px; }
.oc-badge { background: #e5484d; color: #fff; border-radius: 999px; font-size: 11px; padding: 0 7px; }
.oc-last { font-size: 13px; opacity: .75; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 240px; }
.oc-time { font-size: 11px; opacity: .55; }
.oc-chat { flex: 1; display: flex; flex-direction: column; }
.oc-body { flex: 1; overflow-y: auto; padding: 14px; display: flex; flex-direction: column; gap: 8px; }
.oc-msg { max-width: 78%; padding: 8px 11px; border-radius: 10px; font-size: 14px; line-height: 1.45; white-space: pre-wrap; }
.oc-msg.me { align-self: flex-end; background: #18d867; color: #fff; }
.oc-msg.guest { align-self: flex-start; background: var(--vp-c-bg-soft); }
.oc-foot { display: flex; gap: 8px; padding: 10px; border-top: 1px solid var(--vp-c-border); }
.oc-foot input { flex: 1; border: 1px solid var(--vp-c-border); border-radius: 8px; padding: 8px 10px; background: var(--vp-c-bg); color: var(--vp-c-text-1); }
.oc-empty { padding: 16px; opacity: .7; font-size: 14px; }
@media (max-width: 720px) { .oc-main { flex-direction: column; } .oc-list { width: 100%; border-right: 0; } }
</style>
