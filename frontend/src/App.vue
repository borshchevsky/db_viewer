<template>
  <addDbForm/>
  <dbServerView v-for="server in servers" :data="server" :key="server.name"/>
</template>

<script setup>
import {onMounted, provide, ref} from "vue";
import dbServerView from './components/db/dbServerView.vue'
import addDbForm from './components/addDbForm.vue'

const servers = ref(null)
const messages = ref([])
const index = ref(-1)

onMounted(async () => {
  updateServers()
})

const updateServers = () => {
  fetch('http://localhost:8000/api/db/')
  .then(response => response.json())
  .then(data => servers.value = data)
}

provide('updateServers', updateServers)
</script>

<style>
#app >>> ul {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}
</style>
