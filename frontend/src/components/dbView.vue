<template>
  <div>
    <div class="db" @click="toggleOpened">
      <div>
        <img src="../assets/db/db.svg" alt="">
        {{ name }}
      </div>
    </div>
    <ul v-for="key in Object.keys(data)" :key="key" v-show="opened">
      <li>
        <dbSchemaView :name="key" :data="data[key]"/>
      </li>
    </ul>
  </div>
</template>

<script setup>
import {ref} from "vue";

defineProps({
  name: {
    type: String,
    required: true
  },
  data: {
    type: Object,
    required: true
  }
})

const opened = ref(false)
const toggleOpened = () => opened.value = !opened.value
</script>

<style scoped>
.db:hover {
  cursor: default;
}
</style>