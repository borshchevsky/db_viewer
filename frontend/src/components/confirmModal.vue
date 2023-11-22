<template>
  <div class="modal" @click="close(false)">
    <div class="modal-inner" @click.stop>
      <div class="modal-content">
        {{ text }}
        <button @click="close(true)">Yes</button>
        <button @click="close(false)">No</button>
      </div>
    </div>
  </div>
</template>

<script setup>
const emits = defineEmits(['confirm'])

const close = (value) => {
  emits('confirm', value)
}
const props = defineProps({
  text: {
    type: String,
    default: ''
  }
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

.modal-inner {
  margin: auto;
  background: white;
  border-radius: 6px;
  padding: 20px;
}

.modal-content {
  margin: auto;
}

button {
  margin: 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  width: 100px;
}

button:hover {
  background: rgba(0, 0, 0, 0.1);
  transform: translateY(1px);
}

button:active {
  transform: translateY(6px);
}
</style>