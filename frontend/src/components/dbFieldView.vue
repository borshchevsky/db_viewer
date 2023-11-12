<template>
  <div class="field">
    {{ name }}: {{ data }}
  </div>
</template>

<script setup>
defineProps(
    {
      name: {
        type: String,
        required: true
      },
      data: {
        type: String,
        required: true
      }
    }
)
</script>

<style scoped>
.field:hover {
  cursor: default;
}
</style>