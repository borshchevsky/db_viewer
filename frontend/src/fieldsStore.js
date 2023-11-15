import {ref} from "vue";

const checkIncludes = (obj, arr) => {
    for (let item of arr) {
        for (let [key, value] of Object.entries(obj)) {
            if (!(key) in item) {
                break
            }
            if (item[key] !== value) {
                break
            }
            return true
        }
    }
    return false
}

export class FieldsStore {
    constructor() {
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
        console.log(JSON.stringify(this[type]))
    }

    removeField(id) {
        this.source.value = this.source.value.filter((el) => el.id !== id)
        this.target.value = this.target.value.filter((el) => el.id !== id)
    }
}
