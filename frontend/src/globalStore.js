import {ref} from "vue";

const checkIncludes = (obj, arr) => {
    for (let item of arr) {
        for (let [key, value] of Object.entries(obj)) {
            if ((!(key) in item) || (item[key] !== value)) {
                break
            }
            return true
        }
    }
    return false
}

export class GlobalStore {
    constructor() {
        this.sourceServerId = ref(null)
        this.targetServerId = ref(null)
        this.sourceDb = ref(null)
        this.targetDb = ref(null)
        this.sourceSchema = ref(null)
        this.targetSchema = ref(null)
        this.sourceTable = ref(null)
        this.targetTable = ref(null)
        this.index = -1
        this.source = ref([])
        this.target = ref([])
    }

    addField(type, schemaName, tableName, fieldName) {
        let obj = {
            fieldName,
            tableName,
            schemaName
        }
        if (!checkIncludes(obj, this[type].value)) {
            obj['id'] = ++this.index
            this[type].value.push(obj)
        }
    }

    removeField(id) {
        this.source.value = this.source.value.filter((el) => el.id !== id)
        this.target.value = this.target.value.filter((el) => el.id !== id)
    }
}
