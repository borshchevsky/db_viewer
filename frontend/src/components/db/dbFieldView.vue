<template>
  <div class="field" @click="fieldsStore.addField(type, schemaName, tableName, name)">
    {{ name }}: {{ data }}
  </div>
</template>

<script setup>
import {inject} from "vue";

const props = defineProps(
    {
      name: {
        type: String,
        required: true
      },
      data: {
        type: String,
        required: true
      }
    }
)

const fieldsStore = inject('fieldsStore')
const type = inject('type')
const schemaName = inject('schemaName')
const tableName = inject('tableName')

</script>

<style scoped>
.field:hover {
  cursor: default;
}
</style>