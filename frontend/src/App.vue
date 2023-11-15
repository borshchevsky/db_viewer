<template>
  <div>
    <div class="container">
      <addDbForm/>
      <div class="select-container">
        <div class="select-item">
          <label for="sourceDbs">Source db</label>
          <select name="" id="sourceDbs" v-model="selectedSourceDb" @change="fillSourceSchemas">
            <option v-for="key in sourceDbs" :value="key" :key="key">{{ key }}</option>
          </select>
        </div>
        <div class="select-item">
          <label for="sourceSchemas">Source schema</label>
          <select name="" id="sourceSchemas" v-model="selectedSourceSchema" @change="fillSourceTables">
            <option v-for="key in sourceSchemas" :value="key" :key="key">{{ key }}</option>
          </select>
        </div>
        <div class="select-item">
          <label for="sourceTables">Source table</label>
          <select name="" id="sourceTables" v-model="selectedSourceTable">
            <option v-for="key in sourceTables" :value="key" :key="key">{{ key }}</option>
          </select>
        </div>
      </div>
      <div class="select-container">
        <div class="select-item">
          <label for="targetDbs">Target db</label>
          <select name="" id="targetDbs" v-model="selectedTargetDb" @change="fillTargetSchemas">
            <option v-for="key in targetDbs" :value="key" :key="key">{{ key }}</option>
          </select>
        </div>
        <div class="select-item">
          <label for="targetSchemas">Target schema</label>
          <select name="" id="targetSchemas" v-model="selectedTargetSchema" @change="fillTargetTables">
            <option v-for="key in targetSchemas" :value="key" :key="key">{{ key }}</option>
          </select>
        </div>
        <div class="select-item">
          <label for="targetTables">Target table</label>
          <select name="" id="targetTables" v-model="selectedTargetTable">
            <option v-for="key in targetTables" :value="key" :key="key">{{ key }}</option>
          </select>
        </div>
      </div>
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
import uiFieldBinder from './components/ui/uiFieldBinder.vue'

const sourceServer = ref(null)
const targetServer = ref(null)
const messages = ref([])
const index = ref(-1)
const sourceDbs = ref(null)
const sourceSchemas = ref(null)
const sourceTables = ref(null)
const targetDbs = ref(null)
const targetSchemas = ref(null)
const targetTables = ref(null)

onMounted(async () => {
  updateServers()
})

const updateServers = () => {
  fetch('http://localhost:8000/api/db/')
      .then(response => response.json())
      .then(data => {
        sourceServer.value = data.filter((el) => el.type === 'source')[0]
        targetServer.value = data.filter((el) => el.type === 'target')[0]
        sourceDbs.value = Object.keys(sourceServer.value.schema)
        targetDbs.value = Object.keys(targetServer.value.schema)
      })
}
provide('updateServers', updateServers)

const selectedSourceDb = ref(null)
const selectedSourceSchema = ref(null)
const selectedSourceTable = ref(null)
const fillSourceSchemas = () => {
  sourceSchemas.value = Object.keys(sourceServer.value.schema[selectedSourceDb.value])
  selectedSourceSchema.value = null
  selectedSourceTable.value = null
}
const fillSourceTables = () => {
  sourceTables.value = Object.keys(sourceServer.value.schema[selectedSourceDb.value][selectedSourceSchema.value])
  selectedSourceTable.value = null
}

const selectedTargetDb = ref(null)
const selectedTargetSchema = ref(null)
const selectedTargetTable = ref(null)
const fillTargetSchemas = () => {
  targetSchemas.value = Object.keys(targetServer.value.schema[selectedTargetDb.value])
  selectedTargetSchema.value = null
  selectedTargetTable.value = null
}
const fillTargetTables = () => {
  targetTables.value = Object.keys(targetServer.value.schema[selectedTargetDb.value][selectedTargetSchema.value])
  selectedTargetTable.value = null
}


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
  justify-content: space-between;
  align-items: flex-start;
  width: 900px;
}

.select-container {
  margin: 0 10px;
  display: flex;
  flex-direction: column;
  width: 350px;
}

select {
  width: 200px;
}

.select-item {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

</style>
