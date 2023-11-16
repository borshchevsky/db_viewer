<template>
  <div class="main">
    <div class="fields-binder-container">
      <uiFieldsColumn type="source"/>
      <uiFieldsColumn type="target"/>
    </div>
  </div>
  <button @click="process">Process</button>
</template>

<script setup>
import {inject} from "vue";
import uiFieldsColumn from "./uiFieldsColumn.vue"
import {toaster} from "@/toaster";

const globalStore = inject('globalStore')
const process = async () => {
  let sourceFields = globalStore.source.value
  let targetFields = globalStore.target.value
  // if (sourceFields.length !== targetFields.length) {
  //   toaster.addAlert('Number of source and target fields must be equal')
  // }
  let sourceSql = 'select '
  sourceSql += sourceFields.map(field => `"${field.fieldName}"`).join(', ')
  sourceSql += ` from "${globalStore.sourceSchema.value}"."${globalStore.sourceTable.value}"`
  const response = await fetch('http://localhost:8000/api/db/process/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body:
        JSON.stringify({
          ...globalStore.json()
        })
  })
  const data = await response.json()
  console.log(data)
}
</script>

<style scoped>
.main {
  margin: 10px;
  width: 500px;
  height: 500px;
  border-color: black;
  border-style: solid;
  border-width: 1px;
}

.fields-binder-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

button {
  width: 70px;
  margin: 0 10px;
}

</style>