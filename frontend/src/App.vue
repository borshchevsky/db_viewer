<template>
  <div>
    <div class="container">
      <addDbForm/>
      <select name="" id="">
        <option v-for="key in sourceServer" value="">{{ key }}</option>
      </select>
      <select name="" id=""></select>
    </div>
    <div class="server-container">
      <dbServerView :data="sourceServer" v-if="sourceServer"/>
      <dbServerView :data="targetServer" v-if="targetServer"/>
    </div>
  </div>
</template>

<script setup>
import {onMounted, provide, ref} from "vue";
import dbServerView from './components/db/dbServerView.vue'
import addDbForm from './components/ui/addDbForm.vue'

const sourceServer = ref(null)
const targetServer = ref(null)
const messages = ref([])
const index = ref(-1)

onMounted(async () => {
  updateServers()
})

const updateServers = () => {
  fetch('http://localhost:8000/api/db/')
      .then(response => response.json())
      .then(data => {
        sourceServer.value = data.filter((el) => el.type === 'source')[0]
        targetServer.value = data.filter((el) => el.type === 'target')[0]
      })
}
provide('updateServers', updateServers)

const fields = ref({})
provide('fields', fields)
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

.server-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: stretch;
}

.container {
  display: flex;
  flex-direction: row;
  justify-content: stretch;
  align-items: flex-start;
}
</style>
