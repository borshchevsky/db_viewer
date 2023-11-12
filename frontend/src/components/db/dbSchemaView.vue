<template>
  <div>
    <div class="schema" @click="toggleOpen">
      {{ name }}
    </div>
    <ul v-for="key in Object.keys(data)" :key="key" v-show="opened">
      <li>
        <dbTableView :name="key" :data="data[key]"/>
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
.schema:hover {
  cursor: default;
}
</style>