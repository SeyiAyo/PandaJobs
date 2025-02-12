import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './assets/main.css'

// Import views
import Home from './views/Home.vue'
import Jobs from './views/Jobs.vue'
import JobDetail from './views/JobDetail.vue'
import AddJob from './views/AddJob.vue'
import About from './views/About.vue'

// Create router
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: Home },
    { path: '/jobs', name: 'jobs', component: Jobs },
    { path: '/jobs/:id', name: 'job-detail', component: JobDetail },
    { path: '/jobs/add', name: 'add-job', component: AddJob },
    { path: '/about', name: 'about', component: About },
  ],
})

// Create app
const app = createApp(App)

// Use plugins
app.use(router)

// Mount app
app.mount('#app')
