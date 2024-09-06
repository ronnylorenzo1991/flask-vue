import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { authStore } from '@/stores/auth'
import App from './App.vue'
import router from './router'
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import dialog from './libs/dialog';
import helpers from './libs/helpers';

const app = createApp(App)
library.add(fas)
app.component('fa-icon', FontAwesomeIcon)
app.use(router)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
window.dialog = dialog;
window.helpers = helpers;
const auth_store = authStore()
app.config.globalProperties.$filters = {
    can(permission) {
        return auth_store.user.permissions.some(userPermission => userPermission.name  == permission)
      }
}

app.mount('#app')
