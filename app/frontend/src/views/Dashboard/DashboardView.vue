<script setup>
import { ref, onMounted, reactive } from 'vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import axios from 'axios'
import { authStore } from '@/stores/auth'
import Loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css';
import '@/assets/css/multiselect.css'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import StatsSection from './StatsSection.vue'
import LineChartComponent from '@/components/Charts/LineChartComponent.vue'
const pageTitle = ref('Dashboard')
const modulePath = ref('dashboard')
const auth_store = authStore()
const lineChartLabels = ref()
const lineChartSeries = ref()
const config = reactive({
  headers: {
    Authorization: 'Bearer ' + auth_store.token,
  }
})

const isLoading = ref(false)
const statsCardItems = ref([
  {
    icon: 'user',
    title: 'Cantidad de Usuarios',
    total: 0,
    percent: false
  },
  {
    icon: 'vcard',
    title: 'Cantidad de Roles',
    total: 0,
    percent: false
  },
  {
    icon: 'lock',
    title: 'Permisos',
    total: 0,

    percent: false
  },
])

onMounted(async () => {
  await getStatsCardData()
  await getTotals()
})

const getStatsCardData = async () => {
  let url = `${auth_store.api}${modulePath.value}/stats`
  await axios.get(url, config).then(response => {
    statsCardItems.value[0].total = response.data.users_qty
    statsCardItems.value[1].total = response.data.roles_qty
    statsCardItems.value[2].total = response.data.permissions_qty
  }).catch(response => {
    console.log(response)
    dialog.error(response.data.message)
  })
}

const getTotals = async () => {
  let url = `${auth_store.api}${modulePath.value}/totals?by=week`
  await axios.get(url, config).then(response => {
    lineChartSeries.value = [
      {
        name: 'Roles',
        data: response.data.roles_count,
        color: '#ff5ce4'
      },
      {
        name: 'Users',
        data: response.data.users_count,
        color: '#f21862'
      },
      {
        name: 'Permissions',
        data: response.data.permissions_count,
        color: '#fff'
      },
    ]
    lineChartLabels.value = response.data.labels
  }).catch(e => {
    console.log(e)
  })
}
</script>
<template>
  <DefaultLayout>
    <div class="mx-auto max-w-screen">
      <Loading :active="isLoading" v-if="isLoading" :is-full-page="true" background-color="rgba(0, 0, 0, 0.8)" />
      <!-- Breadcrumb Start -->
      <BreadcrumbDefault :pageTitle="pageTitle" />
      <!-- Breadcrumb End -->
      <div class="overflow-hidden rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark p-2 sm:p-10">
        <div class="grid grid-cols-1 gap-5 md:gap-6 2xl:gap-7.5 sm:grid-cols-3 py-10">
          <StatsSection :card-items="statsCardItems" />
        </div>
        <div class="py-5">
          <LineChartComponent :labels="lineChartLabels" :series="lineChartSeries" v-if="lineChartLabels" />
        </div>
      </div>
      <!-- ====== Profile Section End -->
    </div>
  </DefaultLayout>
</template>