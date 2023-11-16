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
const process = () => {
  let sourceFields = globalStore.source.value
  let targetFields = globalStore.target.value
  // if (sourceFields.length !== targetFields.length) {
  //   toaster.addAlert('Number of source and target fields must be equal')
  // }
  let sourceSql = sourceFields.join('')
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