<template>
  {{ schema }}
</template>

<script setup>
import {onMounted, ref} from "vue";

const schema = ref(null)

onMounted(async () => {
  const response = await fetch('http://localhost:8000/api/db/')
  schema.value = await response.json()
})
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
