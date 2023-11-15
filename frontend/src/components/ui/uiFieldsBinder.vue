<template>
  <div class="main">
    <div class="fields-binder-container">
      <uiFieldsColumn type="source"/>
      <uiFieldsColumn type="target"/>
    </div>
  </div>
</template>

<script setup>
import {inject} from "vue";
import uiFieldsColumn from "./uiFieldsColumn.vue"

const fieldsStore = inject('fieldsStore')
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


</style>