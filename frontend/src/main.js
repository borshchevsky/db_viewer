import {createApp} from 'vue'
import App from './App.vue'
import {toaster} from "@/toaster.js";
import addDbForm from '@/components/ui/addDbForm.vue'
import dbServerView from '@/components/db/dbServerView.vue'
import dbView from '@/components/db/dbView.vue'
import dbSchemaView from '@/components/db/dbSchemaView.vue'
import dbTableView from '@/components/db/dbTableView.vue'
import dbFieldView from '@/components/db/dbFieldView.vue'
import uiFieldBinder from './components/ui/uiFieldBinder.vue'

const app = createApp(App)
app.mount('#app')
app.provide('toaster', toaster)
app.component('dbServerView', dbServerView)
    .component('dbView', dbView)
    .component('dbSchemaView', dbSchemaView)
    .component('dbTableView', dbTableView)
    .component('dbFieldView', dbFieldView)
    .component('addDbForm', addDbForm)
    .component('uiFieldBinder', uiFieldBinder)
