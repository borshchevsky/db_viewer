<template>
  <div class="db-server-view">
    <div class="name-container">
      <button @click="removeServer">Remove</button>
      <div class="server" @click="toggleExpand">
        {{ data.type }}
      </div>
    </div>
    <ul v-for="key in Object.keys(data.schema)" :key="key" v-show="expanded">
      <li>
        <dbView :data=data.schema[key] :name="key"/>
      </li>
    </ul>
  </div>
</template>

<script setup>
import {inject, ref} from "vue";

const props = defineProps(
    {
      data: {
        type: Object,
        required: true
      }
    }
)

const updateServers = inject('updateServers')
const expanded = ref(false);
const toggleExpand = () => expanded.value = !expanded.value;
const removeServer = async () => {
  await fetch(`http://localhost:8000/api/db/${props.data.id}`, {
    method: 'DELETE'
  })
  updateServers()
}
</script>

<style scoped>
button {
  margin: 0 5px;
}

.db-server-view {
  margin: 20px
}

.server:hover {
  cursor: default;
}

:deep ul {
  list-style-type: square;
}

.name-container {
  display: flex;
  flex-direction: row;
}
</style>