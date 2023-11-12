<template>
  <div>
    <div v-for="message in messages">
      {{ message }}
    </div>
  </div>
</template>

<script setup>

defineProps(
    {
      messages: {
        type: Array,
        required: true
      }
    }
)

</script>

<style scoped>

</style>