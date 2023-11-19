<template>
  <div class="modal" v-if="show">
    <div class="modal-content">
      {{ currentText }}
      <button @click="close(true)">Yes</button>
      <button @click="close(false)">No</button>
    </div>
  </div>
</template>

<script setup>
import {ref} from "vue";

const currentText = ref('dgdfgdfg')
const show = ref(false)
const returnedValue = ref(1)
const open = (text) => {
  returnedValue.value = null
  currentText.value = text
  show.value = true
}
const close = (value) => {
  returnedValue.value = value
  show.value = false
}

defineExpose({
  open: open,
  returnedValue: returnedValue,
})
</script>

<style scoped>
.modal {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  position: fixed;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
}

.modal-content {
  margin: auto;
  background: white;
  border-radius: 12px;
  min-height: 50px;
  min-width: 300px;
}
</style>