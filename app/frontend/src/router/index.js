import { createRouter, createWebHistory } from 'vue-router'
import { authStore } from '@/stores/auth'
import LoginView from '../views/Authentication/LoginView.vue'
import UsersView from '../views/Security/UsersView.vue'
import RolesView from '../views/Security/RolesView.vue'
import DashboardView from '@/views/Dashboard/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/:pathMatch(.*)*', redirect: '/login', },
    { path: '/', name: 'index', component: DashboardView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/dashboard', name: 'dashboard', component: DashboardView },
    { path: '/users', name: 'users', component: UsersView },
    { path: '/roles', name: 'roles', component: RolesView },
  ]
})

const protected_routes = [
  'dashboard', 
  'users', 
  'roles', 
]

router.beforeEach((to, from, next) => {
  const auth_store = authStore();
  if (to.name !== 'login' && !auth_store.authenticated && protected_routes.some(route => to.name.includes(route))) return next({ name: 'login' })
  if (to.name === 'login' && auth_store.authenticated) return next({ name: 'dashboard' })
  else return next()
})

export default router
