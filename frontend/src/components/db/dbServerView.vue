<template>
  <div class="db-host-view">
    <div class="host" @click="toggleOpen">
      {{ data.name }}
    </div>
    <ul v-for="key in Object.keys(data.schema)" :key="key" v-show="opened">
      <li>
        <dbView :data=data.schema[key] :name=key />
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from "vue";

defineProps(
    {
      data: {
        type: Object,
        required: true
      }
    }
)

const opened = ref(false);
const toggleOpen = () => opened.value =!opened.value;

</script>

<style scoped>
.db-host-view {
  margin: 20px
}

.host:hover {
  cursor: default;
}

:deep ul {
  list-style-type: square;
}
</style>