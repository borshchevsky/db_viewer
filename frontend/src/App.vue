<template>
  <div>
    <div class="container">
      <addDbForm/>
      <div class="mega-container">
        <div class="select-mega-container">
          <div class="select-container">
            <div class="select-item">
              <label for="sourceDbs">Source db</label>
              <select name="" id="sourceDbs" v-model="selectedSourceDb" @change="selectSourceDb">
                <option v-for="key in sourceDbs" :value="key" :key="key">{{ key }}</option>
              </select>
            </div>
            <div class="select-item">
              <label for="sourceSchemas">Source schema</label>
              <select name="" id="sourceSchemas" v-model="selectedSourceSchema" @change="selectSourceSchema">
                <option v-for="key in sourceSchemas" :value="key" :key="key">{{ key }}</option>
              </select>
            </div>
            <div class="select-item">
              <label for="sourceTables">Source table</label>
              <select name="" id="sourceTables" v-model="selectedSourceTable" @change="selectSourceTable">
                <option v-for="key in sourceTables" :value="key" :key="key" @change="">{{ key }}</option>
              </select>
            </div>
          </div>
          <div class="select-container">
            <div class="select-item">
              <label for="targetDbs">Target db</label>
              <select name="" id="targetDbs" v-model="selectedTargetDb" @change="selectTargetDb">
                <option v-for="key in targetDbs" :value="key" :key="key">{{ key }}</option>
              </select>
            </div>
            <div class="select-item">
              <label for="targetSchemas">Target schema</label>
              <select name="" id="targetSchemas" v-model="selectedTargetSchema" @change="selectTargetSchema">
                <option v-for="key in targetSchemas" :value="key" :key="key">{{ key }}</option>
              </select>
            </div>
            <div class="select-item">
              <label for="targetTables">Target table</label>
              <select name="" id="targetTables" v-model="selectedTargetTable" @change="selectTargetTable">
                <option v-for="key in targetTables" :value="key" :key="key">{{ key }}</option>
              </select>
            </div>
          </div>
        </div>
        <uiFieldsBinder/>
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
import dbServerView from '@/components/db/dbServerView.vue'
import addDbForm from '@/components/ui/addDbForm.vue'
import uiFieldsBinder from '@/components/ui/uiFieldsBinder.vue'
import {GlobalStore} from "@/globalStore";

const globalStore = new GlobalStore()

provide('globalStore', globalStore)

const sourceServer = ref(null)
const targetServer = ref(null)
const sourceDbs = ref(null)
const sourceSchemas = ref(null)
const sourceTables = ref(null)
const targetDbs = ref(null)
const targetSchemas = ref(null)
const targetTables = ref(null)
const dialogIsOpened = ref(true)
const toggleDialog = () => {
  dialogIsOpened.value = false
}

onMounted(async () => {
  updateServers()
})

const updateServers = () => {
  fetch('http://localhost:8000/api/db/')
      .then(response => response.json())
      .then(data => {
        let source = data.filter((el) => el.type === 'source')[0]
        let target = data.filter((el) => el.type === 'target')[0]
          sourceServer.value = source
          targetServer.value = target

        if (source) {
          globalStore.sourceServerId.value = sourceServer.value.id
          sourceDbs.value = Object.keys(sourceServer.value.schema)
        }

        if (target) {
          globalStore.targetServerId.value = targetServer.value.id
          targetDbs.value = Object.keys(targetServer.value.schema)
        }
      })
}
provide('updateServers', updateServers)

const selectedSourceDb = ref(null)
const selectedSourceSchema = ref(null)
const selectedSourceTable = ref(null)
const selectedTargetDb = ref(null)
const selectedTargetSchema = ref(null)
const selectedTargetTable = ref(null)

const fillSourceSchemas = () => {
  sourceSchemas.value = Object.keys(sourceServer.value.schema[selectedSourceDb.value])
  selectedSourceSchema.value = null
  selectedSourceTable.value = null
}
const fillSourceTables = () => {
  sourceTables.value = Object.keys(sourceServer.value.schema[selectedSourceDb.value][selectedSourceSchema.value])
  selectedSourceTable.value = null
}

const fillTargetSchemas = () => {
  targetSchemas.value = Object.keys(targetServer.value.schema[selectedTargetDb.value])
  selectedTargetSchema.value = null
  selectedTargetTable.value = null
}
const fillTargetTables = () => {
  targetTables.value = Object.keys(targetServer.value.schema[selectedTargetDb.value][selectedTargetSchema.value])
  selectedTargetTable.value = null
}

const selectSourceDb = () => {
  fillSourceSchemas()
  globalStore.sourceDb.value = selectedSourceDb.value
}

const selectTargetDb = () => {
  fillTargetSchemas()
  globalStore.targetDb.value = selectedTargetDb.value
}

const selectSourceSchema = () => {
  fillSourceTables()
  globalStore.sourceSchema.value = selectedSourceSchema.value
}

const selectTargetSchema = () => {
  fillTargetTables()
  globalStore.targetSchema.value = selectedTargetSchema.value
}

const selectSourceTable = () => globalStore.sourceTable.value = selectedSourceTable.value
const selectTargetTable = () => globalStore.targetTable.value = selectedTargetTable.value

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

.mega-container {
  display: flex;
  flex-direction: column;
}

.select-mega-container {
  display: flex;
  flex-direction: row;
}
</style>
