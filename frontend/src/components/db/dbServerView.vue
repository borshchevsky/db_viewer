<template>
  <confirmModal
      @confirm="handleRemove"
      :text="`Remove ${data.type} server?`"
      v-if="showModal"
  />
  <div class="db-server-view">
    <div class="name-container">
      <button @click="toggleShowModal">Remove</button>
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
import {provide, inject, ref} from "vue";
import confirmModal from "@/components/confirmModal.vue";
import {toaster} from "@/toaster";

const showModal = ref(false);

const toggleShowModal = (value) => {
  showModal.value = !showModal.value
}

const props = defineProps(
    {
      data: {
        type: Object,
        required: true
      }
    }
)

provide('type', props.data.type)

const updateServers = inject('updateServers')
const expanded = ref(false);
const toggleExpand = () => expanded.value = !expanded.value;
const handleRemove = (value) => {
  toggleShowModal()
  if (value) {
    removeServer()
  }
}

const removeServer = async () => {
  const response = await fetch(`http://localhost:8000/api/db/${props.data.id}`, {
    method: 'DELETE'
  })
  updateServers()
  toaster.addAlert(response)
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