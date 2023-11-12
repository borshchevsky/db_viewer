import {createApp} from 'vue'
import App from './App.vue'
import dbHostView from '@/components/dbHostView'
import dbView from '@/components/dbView'
import dbSchemaView from '@/components/dbSchemaView'
import dbTableView from '@/components/dbTableView'
import dbFieldView from '@/components/dbFieldView'

const app = createApp(App)
app.mount('#app')
app.component('dbHostView', dbHostView)
    .component('dbView', dbView)
    .component('dbSchemaView', dbSchemaView)
    .component('dbTableView', dbTableView)
    .component('dbFieldView', dbFieldView)
