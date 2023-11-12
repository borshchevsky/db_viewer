import {createApp} from 'vue'
import App from './App.vue'
import addDbForm from '@/components/addDbForm'
import dbHostView from '@/components/db/dbServerView'
import dbView from '@/components/db/dbView'
import dbSchemaView from '@/components/db/dbSchemaView'
import dbTableView from '@/components/db/dbTableView'
import dbFieldView from '@/components/db/dbFieldView'

const app = createApp(App)
app.mount('#app')
app.component('dbHostView', dbHostView)
    .component('dbView', dbView)
    .component('dbSchemaView', dbSchemaView)
    .component('dbTableView', dbTableView)
    .component('dbFieldView', dbFieldView)
    .component('addDbForm', addDbForm)
