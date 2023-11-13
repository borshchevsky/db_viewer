import {createApp} from "vue";
import theToaster from "./components/theToaster.vue";
export const toaster = createApp(theToaster).mount('#toaster')
