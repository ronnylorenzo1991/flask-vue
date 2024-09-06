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
import VToggle from '@/components/Forms/VToggle.vue'

const pageTitle = ref('Roles')
const modulePath = ref('roles')
const auth_store = authStore()
const currentPermissionModule = ref([])
const currentRolePermissions = ref([])
const permissionModules = ref([])
const config = reactive({
  headers: {
    Authorization: 'Bearer ' + auth_store.token,
  }
})
const lists = ref({
  permissions: [],
})
const isLoading = ref(false)
const showModal = ref(false)
const validationErrors = ref([])
const items = ref([])
const newRole = ref({
  id: null,
  name: null,
})
const columns = [
  {
    value: 'name',
    text: 'Rol',
    sortable: true
  },
  {
    value: 'permissions',
    text: 'Permisos',
    sortable: false
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
  name: null,
})

const clearFilters = () => {
  filters.value = {
    name: null,
  }
  loadData()
}

onMounted(async () => {
  await loadData(null, true)
  await loadLists(['permissions'])
})

const loadData = async (link = null) => {
  isLoading.value = true
  let url = link ? link : `${auth_store.api}${modulePath.value}?sortBy=${pagination.value.sortBy}&sortDir=${pagination.value.sortAsc ? 'asc' : 'desc'}&perPage=${pagination.value.perPage}`
  await axios.get(url, config)
    .then((response) => {
      isLoading.value = false
      items.value = response.data.items
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



const openCreateEditModal = (item = null) => {
  if (item) {
    newRole.value = item
    lists.value.permissions.forEach(permission => {
      currentRolePermissions.value[permission.id] = item.permissions.some(rolePermission => rolePermission.id === permission.id)
    })
  }

  showModal.value = true
}

const resetValidationErrors = () => {
  validationErrors.value = []
}

const resetData = () => {
  resetValidationErrors()
  newRole.value = {
    id: null,
    name: null,
  }

  currentPermissionModule.value = []
  currentRolePermissions.value = []
}

const closeModal = () => {
  resetData()
  showModal.value = false
}

const getValidationText = (key) => {
  return validationErrors.value[key] ? validationErrors.value[key].join(', ') : ''
}

const save = async () => {
  isLoading.value = true
  if (newRole.value.id) {
    const url = `${auth_store.api}${modulePath.value}/${newRole.value.id}`
    axios.put(url, newRole.value, config)
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
    axios.post(url, newRole.value, config)
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

const loadLists = async (list) => {
  let url = `${auth_store.api}lists?lists=${JSON.stringify(list)}`
  axios.get(url, config)
    .then(response => {
      if (response.status === 200) {
        lists.value = response.data
        preparePermissionsModules()
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

const hasCurrentModule = (permission) => {
  return permission.module_name === currentPermissionModule.value
}

const togglePermission = (permission) => {
  if (newRole.value.id) {
    isLoading.value = true
    let value = currentRolePermissions.value[permission.id]
    const url = `${auth_store.api}${modulePath.value}/toggle_permission/${newRole.value.id}`
    axios.post(url, { permission_name: permission.name, permission_value: value.toString() }, config)
      .then(response => {
        isLoading.value = false
        if (response.status === 200) {
          dialog.success(response.data.message)
        } else {
          dialog.error()
        }
      }).catch(({ response }) => {
        isLoading.value = false
        if (response.status === 422) {
          validationErrors.value = response.data.errors
        } else {
          dialog.error(response.data.message)
          console.log('error', response)
        }
      })

    return
  }
  newRole.value.permissions = !newRole.value.permissions ? [] : newRole.value.permissions
  newRole.value.permissions.push(permission.id)
}


const preparePermissionsModules = () => {
  lists.value.permissions.forEach(item => {
    if (!permissionModules.value.includes(item.module_name)) {
      permissionModules.value.push(item.module_name)
    }
  })
}

const sanitizePermissions = (item) => {
  let permissions = []
  item.item.permissions.forEach(rolePermission => {
    const permission = lists.value.permissions.find(listPermission => listPermission.id === rolePermission.id)
    if (permission) {
      permissions.push(permission.display_name)
    }
  })

  return permissions.join(', ')
}
</script>
<template>
  <DefaultLayout>
    <div class="mx-auto max-w-screen">
      <!-- Breadcrumb Start -->
      <BreadcrumbDefault :pageTitle="pageTitle" />
      <!-- Breadcrumb End -->
      <div
        class="overflow-hidden rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark p-2 sm:p-10">
        <Loading :active="isLoading" v-if="isLoading" :is-full-page="true" background-color="rgba(0, 0, 0, 0.8)" />

        <DataTable :columns="columns" :items="items" :paginate="false" :links="pagination.links" :filters="filters"
          @edit="openCreateEditModal" @remove="remove" :showCreateNewButton="true" @clearFilters="clearFilters"
          :current_page="pagination.current_page" :prev_page="pagination.prev_page" :perPage="pagination.perPage"
          :next_page="pagination.next_page" @navigate="loadData" :from="pagination.from" :to="pagination.to"
          :total="pagination.total" @add="openCreateEditModal()">
          <template v-slot:filters>
            <div class="flex flex-wrap py-5 relative">
              <div class="w-full sm:w-1/2 md:w-1/4 p-4">
                <Input id="name" v-model="filters.name" type="text" placeholder="Nombre del Rol" label="Usuario" />
              </div>
            </div>
          </template>
          <template #column-permissions="item">
            <div class="flex items-center">{{ sanitizePermissions(item) }}</div>
          </template>
        </DataTable>
        <Modal v-if="showModal" @cancel="closeModal" @accept="save" title="Agregar Rol" :show="showModal">
          <Input label="Nombre" type="text" placeholder="Nombre" v-model="newRole.name" class="my-6"
            :validation="getValidationText('name')" required />
          <label> Permisos</label>
          <div class="w-full my-3 px-2">
            <Multiselect v-model="currentPermissionModule" placeholder="Seleccione el Modulo" :close-on-select="true"
              :searchable="true" :options="permissionModules" />
            <div class="absolute pb-6">
              <label class="text-red-500 text-xs" v-text="getValidationText('permissions')"></label>
            </div>
          </div>
          <div class="flex flex-col ml-5">
            <div v-for="permission in lists.permissions" :key="permission.id">
              <div v-if="hasCurrentModule(permission)" class="py-1">
                <v-toggle :label="permission.display_name" v-model="currentRolePermissions[permission.id]"
                  @change="togglePermission(permission)"></v-toggle>
              </div>
            </div>
          </div>
        </Modal>
      </div>
      <!-- ====== Profile Section End -->
    </div>
  </DefaultLayout>
</template>