<script setup lang="ts">
const props = defineProps({
  items: {
    default: []
  },
  withActions: {
    default: true
  },
  colors: {
    default: { Gapping: '#FFA70B', Salmon: '#f47c70', Melanosis: '#D34053', Hematoma: '#e22e94', Cracking: '#ac5e17', Cicatriz: '#cbb79f', 'Salmon Inv': '#548f94' }
  },
  columns: {
    default: []
  },
  links: {
    default: []
  },
  current_page: {
    type: Number
  },
  prev_page: {
    type: String
  },
  next_page: {
    type: String
  },
  from: {
    type: Number
  },
  to: {
    type: Number
  },
  total: {
    type: Number
  },
  actions: {
    default: {
      edit: true,
      show: true,
      delete: true,
      downloadItem: true,
    }
  },
})

const getChildrenLabelsUniques = (childrens) => {
  let arrayLabels = []
  childrens.filter(item => {
    if (!arrayLabels.includes(item.class_label)) {
      arrayLabels.push(item.class_label)
    }
  })

  return arrayLabels
}

</script>

<template>
  <div
    class="col-span-12 rounded-sm border border-stroke bg-white px-5 pt-7.5 pb-5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:col-span-8">
    <div class="max-w-full overflow-x-auto">
      <div class="flex items-end my-5">
        <slot name="table-menu">
        </slot>
      </div>
      <table class="w-full table-auto">
        <thead>
          <tr class="bg-gray-2 text-left dark:bg-meta-4">
            <th class="min-w-[220px] py-4 px-4 font-medium text-black dark:text-white xl:pl-11"
              v-for="header in props.columns" :key="header.id">
              {{ header.text }}
            </th>
            <th class="py-4 px-4 font-medium text-black dark:text-white" v-if="withActions">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in items" :key="index">
            <td class="py-5 px-4 pl-9 xl:pl-11" v-for="header in props.columns" :key="header.id">
              <div v-if="header.type == 'multiple'">
                <p v-for="label in getChildrenLabelsUniques(item[header.key])"
                  class="inline-flex rounded-full bg-opacity-10 py-1 px-3 text-sm font-medium"
                  :style="{ backgroundColor: `${colors[label]}40`, color: colors[label] }" :key="label">{{ label }}</p>
              </div>
              <div v-else-if="header.type == 'image'">
                <div class="flex items-center">
                  <img :src="item[header.key]" alt="Image" width="60" class="rounded-full"
                    @click="$emit('imageClicked', item)" />
                </div>
              </div>
              <div v-else>
                <p class="text-sm">{{ item[header.key] }}</p>
              </div>
            </td>
            <td>
              <slot name="actions">
                <div class="flex items-center space-x-3.5">
                  <button class="hover:text-primary" @click="$emit('edit', item)" v-show="actions.edit">
                    <fa-icon icon="pencil" />
                  </button>
                  <button class="hover:text-primary" @click="$emit('show', item)" v-show="actions.show">
                    <fa-icon icon="eye" />
                  </button>
  
                  <button class="hover:text-primary" @click="$emit('delete', item)" v-show="actions.delete">
                    <fa-icon icon="trash" />
                  </button>
  
                  <button class="hover:text-primary" @click="$emit('download-item', item)" v-show="actions.downloadItem">
                    <fa-icon icon="download" />
                  </button>
                </div>
              </slot>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="py-5 flex flex-row" v-if="items.length">
      <div class="w-1/2 px-2 text-md text-gray-500">
        {{ from }} a {{ to }} de {{ total }}
      </div>
      <div class="w-1/2">
        <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px float-right" aria-label="Pagination">
          <button v-for="link in props.links" :key="link" aria-current="page" :disabled="!link.url" @click="$emit('navigate', link.url)"
            :class="`${link.active ? 'z-10 bg-primary shadow-default text-white' : 'bg-white dark:border-strokedark dark:bg-boxdark text-gray-500 hover:bg-gray-50'} relative inline-flex items-center px-4 py-2 border text-sm font-medium`">

            <span v-if="link?.label?.includes('Anterior')">
              <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"
                aria-hidden="true">
                <path fill-rule="evenodd"
                  d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                  clip-rule="evenodd" />
              </svg>
            </span>

            <svg v-if="link?.label?.includes('Siguiente')" class="h-5 w-5" xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd"
                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                clip-rule="evenodd" />
            </svg>

            <span v-if="!link?.label?.includes('Siguiente') && !link.label.includes('Anterior')">{{
              link.label
              }}</span>
          </button>
        </nav>
      </div>
    </div>
  </div>
</template>
