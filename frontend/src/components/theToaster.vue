<template>
  <div class="toasts">
    <div class="toast_container" v-for="message in messages">
      <div :class="['toast', message.type === 'success' ? 'toast_success' : 'toast_error']">
        {{ message.message }}
      </div>
    </div>
  </div>
</template>

<script setup>

import {ref} from "vue";

const index = ref(-1)
const messages = ref([])

const addAlert = (message, type) => {
  messages.value.push({
    id: ++index.value,
    message,
    type
  })
  let i = index.value
  setTimeout(() => messages.value = messages.value.filter((el) => el.id !== i), 3000)
}

defineExpose(
    {
      addAlert: addAlert
    }
)
</script>

<style scoped>
.toasts {
}

.toast_container {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.toast {
  margin: 5px;
  display: flex;
  flex: 0 0 auto;
  padding: 16px;
  background: #ffffff;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  border-radius: 4px;
  font-size: 18px;
  line-height: 28px;
  width: fit-content;
}

.toast_success {
  color: mediumseagreen;
}

.toast_error {
  color: red;
}
</style>