<script setup>
import { ref, onMounted, reactive } from 'vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import DataTable from '@/components/Tables/DataTableComponent.vue'
import Input from '@/components/Forms/InputComponent.vue'
import axios from 'axios'
import { authStore } from '@/stores/auth'
import Modal from '@/components/Modal/ModalComponent.vue'
import Loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css';
import Multiselect from '@vueform/multiselect'
import '@/assets/css/multiselect.css'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'

const pageTitle = ref('Usuarios')
const modulePath = ref('users')
const auth_store = authStore()
const config = reactive({
  headers: {
    Authorization: 'Bearer ' + auth_store.token,
  }
})
const lists = ref({
  roles: [],
})
const isLoading = ref(false)
const showModal = ref(false)
const validationErrors = ref([])
const items = ref([])
const newUser = ref({
  id: null,
  username: null,
  email: null,
  roles: [],
})
const columns = [
  {
    value: 'username',
    text: 'Usuario',
    sortable: true
  },
  {
    value: 'email',
    text: 'Email',
    sortable: true
  },
  {
    value: 'roles',
    text: 'Roles',
  },
]

const pagination = ref({
  'total': null,
  'pages': null,
  'current_page': null,
  'next_page': null,
  'prev_page': null,
  'links': [],
  'from': 1,
  'to': 10,
  'perPage': 10,
  'sortAsc': false,
  'sortBy': 'id',
})

const filters = ref({
  username: null,
  email: null,
})

const clearFilters = () => {
  filters.value = {
    username: null,
    email: null,
  }
  loadData()
}

onMounted(async () => {
  await loadData(null, true)
  await loadLists(['roles', 'users'])
})

const loadData = async (link = null) => {
  isLoading.value = true
  let url = link ? link : `${auth_store.api}${modulePath.value}?sortBy=${pagination.value.sortBy}&sortDir=${pagination.value.sortAsc ? 'asc' : 'desc'}&perPage=${pagination.value.perPage}`
  await axios.get(url, config)
    .then((response) => {
      isLoading.value = false
      items.value = response.data.users
      pagination.value.pages = response.data.pages
      pagination.value.total = response.data.total
      pagination.value.current_page = response.data.current_page
      pagination.value.next_page = response.data.next_page
      pagination.value.prev_page = response.data.prev_page
      pagination.value.links = response.data.links
      pagination.value.from = response.data.from
      pagination.value.to = response.data.to
    })
    .catch(({ response }) => {
      isLoading.value = false
      dialog.error(response.data.message)
    })
  isLoading.value = false
}

const sanitizeRoles = (item) => {
  let roles = []
  item.item.roles.forEach(role_id => {
    const role = lists.value.roles.find(role => role.id === role_id)
    if (role) {
      roles.push(role.name)
    }
  })

  return roles.join(', ')
}

const openCreateEditModal = (item = null) => {
  newUser.value = item ? item : newUser.value
  showModal.value = true
}

const resetValidationErrors = () => {
  validationErrors.value = []
}

const resetData = () => {
  resetValidationErrors()
  newUser.value = {
    id: null,
    username: null,
    email: null,
    roles: [],
  }
}

const closeModal = () => {
  resetData()
  showModal.value = false
}

const getValidationText = (key) => {
  return validationErrors.value[key] ? validationErrors.value[key].join(', ') : ''
}

const loadLists = async (list) => {
  let url = `${auth_store.api}lists?lists=${JSON.stringify(list)}`
  axios.get(url, config)
    .then(response => {
      if (response.status === 200) {
        lists.value = response.data
      } else {
        dialog.error(response.data.message)
      }
    }).catch(error => {
      if (!error.response) {
        dialog.error()
      } else {
        dialog.error()
      }
    })
}

const save = async () => {
  isLoading.value = true
  if (newUser.value.id) {
    const url = `${auth_store.api}${modulePath.value}/${newUser.value.id}`
    axios.put(url, newUser.value, config)
      .then(response => {
        isLoading.value = false
        dialog.success(response.data.message)
        closeModal()
        loadData()
      }).catch(({ response }) => {
        isLoading.value = false
        if (response.status === 422) {
          validationErrors.value = response.data.errors
        } else {
          console.log('error', response)
          dialog.error(response.data.message)
        }
      })
  } else {
    const url = `${auth_store.api}${modulePath.value}`
    axios.post(url, newUser.value, config)
      .then(response => {
        isLoading.value = false
        dialog.success(response.data.message)
        closeModal()
        loadData()
      }).catch(({ response }) => {
        isLoading.value = false
        if (response.status === 422) {
          validationErrors.value = response.data.errors
        } else {
          console.log('error', response)
          dialog.error(response.data.message)
        }
      })
  }
}

const remove = async (item) => {
  dialog.confirm('Seguro que desea eliminar este elemento?')
    .then((confirm) => {
      if (confirm) {
        if (item.id) {
          axios.delete(`${auth_store.api}${modulePath.value}/${item.id}`, config)
            .then(response => {
              dialog.success(response.data.message)
              loadData()
            }).catch(({ response }) => {
              dialog.error(response.data.message)
              console.log('error', response.data)
              return
            })
        }
      }
      loadData()
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
      <div
        class="overflow-hidden rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark p-2 sm:p-10">
        <DataTable :columns="columns" :items="items" :paginate="false" :links="pagination.links" :filters="filters"
          @edit="openCreateEditModal" @remove="remove" :showCreateNewButton="true" @clearFilters="clearFilters"
          :current_page="pagination.current_page" :prev_page="pagination.prev_page" :perPage="pagination.perPage"
          :next_page="pagination.next_page" @navigate="loadData" :from="pagination.from" :to="pagination.to"
          :total="pagination.total" @add="openCreateEditModal()">
          <template v-slot:filters>
            <div class="flex flex-wrap py-5 relative">
              <div class="w-full sm:w-1/2 md:w-1/4 p-4">
                <Input id="username" v-model="filters.username" type="text" placeholder="Nombre de usuario"
                  label="Usuario" />
              </div>
              <div class="w-full sm:w-1/2 md:w-1/4 p-4">
                <Input id="email" v-model="filters.email" type="text" placeholder="Correo electrónico" label="Email" />
              </div>
            </div>
          </template>
          <template #column-roles="item">
            <div class="flex items-center">{{ sanitizeRoles(item) }}</div>
          </template>
        </DataTable>
        <Modal v-if="showModal" @cancel="closeModal" @accept="save" title="Agregar Usuario" :show="showModal">
          <label class="mb-2.5 block text-black dark:text-white">
            Roles
            <span class="text-danger">*</span>
          </label>
          <Multiselect v-model="newUser.roles" placeholder="Seleccione los Roles" :close-on-select="true"
            :searchable="true" :options="lists.roles" mode="tags" value-prop="id" label="name" />
          <div class="absolute pb-6">
            <label class="text-danger text-xs" v-text="getValidationText('roles')"></label>
          </div>
          <Input label="Nombre" type="text" placeholder="Nombre" v-model="newUser.username" class="my-6"
            :validation="getValidationText('username')" required />
          <Input label="Email" type="text" placeholder="Email" v-model="newUser.email" class="my-6"
            :validation="getValidationText('email')" required />
        </Modal>
      </div>
      <!-- ====== Profile Section End -->
    </div>
  </DefaultLayout>
</template>