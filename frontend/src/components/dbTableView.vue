<template>
  <div>
    <div class="table" @click="toggleOpen">
      {{ name }}
    </div>
    <ul v-for="key in Object.keys(data)" :key="key" v-show="opened">
      <li>
        <dbFieldView :name="key" :data="data[key]"/>
      </li>
    </ul>
  </div>
</template>

<script setup>
import {ref} from "vue";

defineProps(
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

const opened = ref(false)
const toggleOpen = () => opened.value = !opened.value
</script>

<style scoped>
.table:hover {
  cursor: default;
}
</style>