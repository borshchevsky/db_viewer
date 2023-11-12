<template>
  <div class="host-form">
    <div class="input-item">
      <label for="name">Name</label>
      <input id="name" type="text" v-model="name">
    </div>
    <div class="input-item">
      <label for="host">Host</label>
      <input id="host" type="text" v-model="host">
    </div>
    <div class="input-item">
      <label for="port">Port</label>
      <input id="port" type="text" v-model="port">
    </div>
    <div class="input-item">
      <label for="username">Username</label>
      <input id="username" type="text" v-model="username">
    </div>
    <div class="input-item">
      <label for="password">Password</label>
      <input id="password" type="password" v-model="password">
    </div>
  </div>
  <button @click="addServer">Add server</button>
</template>

<script setup>
import {inject, ref} from "vue";

const name = ref('asd')
const host = ref('localhost')
const port = ref(5432)
const username = ref('postgres')
const password = ref('postgres')
const addAlert = inject('addAlert')

const addServer = async () => {
  const response = await fetch('http://localhost:8000/api/db/',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: name.value,
      host: host.value,
      port: port.value,
      username: username.value,
      password: password.value
    })
  })
  const json = await response.json()
  addAlert(json.message, json.type)
}
</script>

<style scoped>
.host-form {
  display: flex;
  flex-direction: column;
  width: 20%;
  justify-content: space-between;
}
.input-item {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>