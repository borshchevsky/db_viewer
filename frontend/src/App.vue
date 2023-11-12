<template>
  <dbHostView v-for="host in hosts" :data="host" :key="host.name"/>
</template>

<script setup>
import {onMounted, ref} from "vue";
import dbHostView from "./components/dbHostView.vue";

const hosts = ref(null)

onMounted(async () => {
  const response = await fetch('http://localhost:8000/api/db/')
  hosts.value = await response.json()
})
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}
body {
  list-style-type: none;
}
</style>
