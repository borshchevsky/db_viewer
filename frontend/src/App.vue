<template>
  <theToaster :messages="messages"/>
  <addDbForm/>
  <dbHostView v-for="host in hosts" :data="host" :key="host.name"/>
</template>

<script setup>
import {onMounted, ref, computed, provide} from "vue";
import dbHostView from './components/db/dbServerView.vue'
import addDbForm from './components/addDbForm.vue'
import theToaster from './components/theToaster.vue'

const hosts = ref(null)
const messages = ref([])
const index = ref(-1)
const addAlert = (message, type) => {
  messages.value.push({
    index: ++index.value,
    message,
    type
  })
  let i = index.value
  setTimeout(() => messages.value = messages.value.filter((el) => el.index !== i), 1000)
}
provide('addAlert', addAlert)

onMounted(async () => {
  const response = await fetch('http://localhost:8000/api/db/')
  hosts.value = await response.json()

})
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
