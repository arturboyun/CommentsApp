import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import Vuelidate from 'vuelidate'
import VueNoty from 'vuejs-noty'

Vue.config.productionTip = false
Vue.use(Vuelidate)
Vue.use(VueNoty, {
  timeout: 3000,
  progressBar: true,
})
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
