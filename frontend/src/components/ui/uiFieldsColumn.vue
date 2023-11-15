<template>
<div class="fields-container">
  {{ type }}
  <div
      class="field"
      v-for="field in globalStore[type].value"
      :key="field.id"
      @click="globalStore.removeField(field.id)"
  >
    {{ field.fieldName }}
  </div>
</div>
</template>

<script setup>
import {inject} from "vue";

const globalStore = inject('globalStore');

defineProps({
  type: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.fields-container {
  display: flex;
  flex-direction: column;
}

.field:hover {
  cursor: default;
}
</style>