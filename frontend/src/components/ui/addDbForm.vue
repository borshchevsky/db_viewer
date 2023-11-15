<template>
  <div>
    <div class="host-form">
      <div class="input-item">
        <label for="server_type">Type</label>
        <select name="" id="server_type" v-model="type">
          <option value="source">source</option>
          <option value="target">target</option>
        </select>
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
      <button @click="addServer">Add server</button>
    </div>
  </div>
</template>

<script setup>
import {inject, ref} from "vue";
import {toaster} from "@/toaster";

const type = ref('source');
const host = ref('localhost')
const port = ref(5432)
const username = ref('postgres')
const password = ref('postgres')
const updateServers = inject('updateServers')

const addServer = async () => {
  const response = await fetch('http://localhost:8000/api/db/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      type: type.value,
      host: host.value,
      port: port.value,
      username: username.value,
      password: password.value
    })
  })
  const json = await response.json()
  toaster.addAlert(json['message'], json['type'])

  if (response.status === 201) {
    updateServers()
  }
}
</script>

<style scoped>
.host-form {
  display: flex;
  flex-direction: column;
  width: 15em;
  justify-content: space-between;
}

.input-item {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

input {
  width: 150px;
}

select {
  width: 158px;
}

button {
  width: 100px;
  margin: 5px 0;
}
</style>