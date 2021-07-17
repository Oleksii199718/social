import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store';

Vue.config.productionTip = false

//new Vue({
//    router,
//    store,
//    render: h => h(App)
//}).$month(elementOrSelector: '#app')

createApp(App).use(router, store).mount('#app')
