<template>
  <div>
    <div class="table" @click="toggleExpand">
      {{ name }}
    </div>
    <ul v-for="key in Object.keys(data)" :key="key" v-show="expanded">
      <li>
        <dbFieldView :name="key" :data="data[key]"/>
      </li>
    </ul>
  </div>
</template>

<script setup>
import {provide, ref} from "vue";

const props = defineProps(
    {
      name: {
        type: String,
        required: true
      },
      data: {
        type: Object,
        required: true
      }
    }
)

provide('tableName', props.name)

const expanded = ref(false)
const toggleExpand = () => expanded.value = !expanded.value
</script>

<style scoped>
.table:hover {
  cursor: default;
}
</style>