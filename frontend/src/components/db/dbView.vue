<template>
  <div>
    <div class="db" @click="toggleExpand">
      <div>
        <img src="../../assets/db/db.svg" alt="">
        {{ name }}
      </div>
    </div>
    <ul v-for="key in Object.keys(data)" :key="key" v-show="expanded">
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

const expanded = ref(false)
const toggleExpand = () => expanded.value = !expanded.value
</script>

<style scoped>
.db:hover {
  cursor: default;
}

</style>