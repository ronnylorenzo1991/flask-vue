<template>
    <div>
        <div class="relative">
            <div class="flex flex-row py-2">
                <div class="flex ml-auto">
                    <slot name="table-menu">
                    </slot>
                    <button v-if="hasFilters"
                        class="uppercase bg-gray-100 text-sm py-1 px-2 mx-2 hover:bg-slate-200 hover:dark:bg-slate-700 dark:border-strokedark dark:bg-boxdark dark:text-slate-300 text-boxdark"
                        type="button" @click="toggleOpenFilters">
                        filtros
                        <fa-icon icon="list" class="px-2" />
                    </button>
                    <slot name="add-new-button">
                        <button @click="emit('add')" v-if="showCreateNewButton"
                            class="bg-primary hover:bg-blue-500 border-primary hover:border-blue-500 text-sm border-4 text-white py-1 px-2"
                            type="button">
                            + Insertar Nuevo
                        </button>
                    </slot>
                </div>
            </div>
            <transition enter-active-class="duration-300 ease-out" enter-from-class="transform opacity-0"
                enter-to-class="opacity-100" leave-active-class="duration-200 ease-in" leave-from-class="opacity-100"
                leave-to-class="transform opacity-0">
                <div v-if="showFilters" class="z-20 text-sm sm:text-md">
                    <slot name="filters"></slot>
                    <div class="flex flex-row">
                        <div class="mx-auto py-4">
                            <button @click="emit('clearFilters')"
                                class="text-slate-700 hover:text-white hover:border-primary hover:border-2 text-sm py-1 px-2 hover:bg-primary hover:dark:bg-primary  dark:border-primary dark:text-slate-300 mx-2"
                                type="button"> Limpiar
                            </button>
                            <button @click="applyFilters"
                                class="bg-primary border-primary border-2 dark:border-primary text-sm py-1 px-2 hover:bg-blue-600 hover:dark:bg-slate-700  dark:bg-primary dark:text-slate-300 text-white"
                                type="button"> Aplicar
                            </button>
                        </div>
                    </div>
                </div>
            </transition>
            <div class="container">
                <table
                    class="w-full flex flex-row flex-no-wrap rounded-lg overflow-hidden sm:shadow-lg my-5">
                    <thead class="dark:text-white">
                        <tr v-for="(item, index) of items" :key="index" class="shadow-md flex flex-col flex-no wrap sm:table-row rounded-l-lg sm:rounded-none mb-2 sm:mb-0 sm:border-none border-slate-500"
                            scope="col">
                            <th class="p-2 text-start shadow-md text-sm sm:text-md w-full sm:w-10 sm:text-center">No.</th>
                            <th v-for="header in columns" :key="header.id" class="p-2 shadow-md text-sm sm:text-md text-start w-full sm:w-screen">
                                <a href="#" @click.prevent="changeSort(header)" class="flex flex-row"
                                    v-if="header.sortable && !isTableEmpty">
                                    <p>
                                        {{ header.text }}
                                    </p>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-5 h-5"
                                        v-if="sortBy !== header.value">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M8.25 15L12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9" />
                                    </svg>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-5 h-5"
                                        v-if="sortBy === header.value && !sortAsc">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M15.75 17.25L12 21m0 0l-3.75-3.75M12 21V3" />
                                    </svg>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-5 h-5"
                                        v-if="sortBy === header.value && sortAsc">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M8.25 6.75L12 3m0 0l3.75 3.75M12 3v18" />
                                    </svg>
                                </a>
                                <div v-else>
                                    {{ header.text }}
                                </div>
                            </th>
                            <th class="w-full sm:w-20 sm:text-center shadow-md text-sm sm:text-md text-start p-2" v-if="withActions">Acciones</th>
                        </tr>
                    </thead>
                    <tbody class="flex-1 sm:flex-none">
                        <tr v-if="isTableEmpty" class="flex flex-col flex-no wrap sm:table-row mb-2 sm:mb-0">
                            <td class="text-center py-4" :colspan="99" v-if="isTableEmpty">
                                No hay datos para mostrar
                            </td>
                        </tr>
                        <template v-for="(item, index) of items" :key="index">
                            <DataTableRow :item="item" :index="index" :columns="columns"
                                :children-columns="childrenColumns" :perPage="perPage" :childrens="childrens"
                                :with-actions="withActions" :actions="actions" :current-page="current_page"
                                :is-children-row="false" :expanded-rows="expandedRows" @expandRow="expandRow"
                                @edit="(value) => $emit('edit', value)" @complete="(value) => $emit('complete', value)"
                                @show_images="(value) => $emit('show_images', value)"
                                @show="(value) => $emit('show', value)"
                                @print_preview="(value) => $emit('print_preview', value)"
                                @review="(value) => $emit('review', value)" @remove="(value) => $emit('remove', value)">
                                <template v-for="column in columns" :key="column" v-slot:[`column-${column.value}`]>
                                    <slot :name="`column-${column.value}`" v-bind:item="item"
                                        :data-cy="`column-${column.value}`"></slot>
                                </template>
                                <template v-slot:actions-cell>
                                    <slot name="actionsMenu" v-bind:item="item" />
                                </template>
                            </DataTableRow>
                            <DataTableRow :item="item" :index="index" :columns="columns" v-if="hasChildren(item, childrens)"
                                :children-columns="childrenColumns" :childrens="childrens" :with-actions="false"
                                :is-children-row="true" :actions="childrenActions" :expanded-rows="expandedRows">
                            </DataTableRow>
                        </template>
                    </tbody>
                </table>
            </div>

        </div>
        <div class="py-5 flex flex-row" v-if="!isTableEmpty">
            <div class="w-1/2 px-2 text-md text-gray-500">
                {{ from }} a {{ to }} de {{ total }}
            </div>
            <div class="w-1/2">
                <nav class="relative inline-flex rounded-md shadow-sm -space-x-px float-right gap-1"
                    aria-label="Pagination">
                    <button :disabled="!prev_page"
                        :class="`${prev_page ? 'hover:bg-primary hover:text-white' : 'text-slate-600'} relative inline-flex items-center px-2 py-2 text-sm font-medium`"
                        @click="$emit('navigate', concatFilters(`${prev_page}&sortBy=${sortBy}&sortDir=${sortAsc ? 'asc' : 'desc'}&perPage=${perPage}`))">
                        <span>
                            <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
                                fill="currentColor" aria-hidden="true">
                                <path fill-rule="evenodd"
                                    d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                                    clip-rule="evenodd" />
                            </svg>
                        </span>
                    </button>
                    <button v-for="link in links" aria-current="page" :disabled="!link.url" :key="link"
                        @click="$emit('navigate', concatFilters(`${link.url}&sortBy=${sortBy}&sortDir=${sortAsc ? 'asc' : 'desc'}&perPage=${perPage}`))"
                        :class="`${link.active ? 'z-10 bg-primary  text-white' : 'text-gray-500 hover:bg-gray-50'} hover:bg-primary hover:text-white relative inline-flex items-center px-4 py-2 text-sm font-medium`">
                        <span>{{
                            link.label
                            }}</span>
                    </button>
                    <button :disabled="!next_page"
                        :class="`${next_page ? 'hover:bg-primary hover:text-white' : 'text-slate-600'} relative inline-flex items-center px-2 py-2 text-sm font-medium`"
                        @click="$emit('navigate', concatFilters(`${next_page}&sortBy=${sortBy}&sortDir=${sortAsc ? 'asc' : 'desc'}&perPage=${perPage}`))">
                        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"
                            aria-hidden="true">
                            <path fill-rule="evenodd"
                                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                clip-rule="evenodd" />
                        </svg>
                    </button>
                </nav>
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, computed } from 'vue'
import DataTableRow from './DataTableRow.vue'

const props = defineProps({
    withActions: {
        type: Boolean,
        default: true,
    },
    columns: Array,
    filters: {
        default: {}
    },
    items: {},
    excludeCompleted: {
        type: Boolean,
        default: false,
    },
    onlyPendants: {
        type: Boolean,
        default: false,
    },
    paginate: {
        type: Boolean,
        default: false,
    },
    store: Object,
    links: Array,
    current_page: Number,
    current_url: Object,
    prev_page: String,
    next_page: String,
    from: Number,
    to: Number,
    total: Number,
    perPage: Number,
    childrenColumns: {
        default: []
    },
    actions: {
        default: [
            {
                event: 'edit',
                text: 'Editar',
                icon: 'edit',
                color: 'yellow',
            },
            {
                event: 'remove',
                text: 'Eliminar',
                icon: 'trash',
                color: 'red',
            }
        ]
    },
    childrenActions: {
        default: []
    },
    childrens: {
        type: String,
        default: ''
    },
    showCreateNewButton: {
        type: Boolean,
        default: true,
    },
})

const sortAsc = ref(false)
const sortBy = ref('id')
const itemsData = ref({})
const expandedRows = ref([])
const emit = defineEmits(['navigate', 'clearFilters', 'add', 'edit', 'remove'])
const showFilters = ref(false)

const hasFilters = computed(() => {
    return Object.keys(props.filters).length > 0
})
const isTableEmpty = computed(() => {
    return !helpers.nativeGet(props.items, 'length', 0)
})

const applyFilters = () => {
    let link = `${getActiveLinkUrl()}&sortBy=${sortBy.value}&sortDir=${sortAsc.value ? 'asc' : 'desc'}`

    link = concatFilters(link)

    emit('navigate', link)
}

const hasChildren = (item, childrens) => {
    return helpers.nativeGet(item, childrens, []).length > 0
}

const concatFilters = (link) => {
    Object.keys(props.filters).forEach(item => {
        if (props.filters[item] !== null) {
            link += `&${item}=${props.filters[item] || ''}`
        }
    })

    return link
}

const toggleOpenFilters = () => {
    showFilters.value = !showFilters.value
}

const expandRow = (index) => {
    if (expandedRows.value.includes(index)) {
        expandedRows.value = expandedRows.value.filter(item => item !== index)
    } else {
        expandedRows.value.push(index)
    }
}

function changeSort(header) {
    if (sortBy.value === header.value) {
        sortAsc.value = !sortAsc.value
    } else {
        sortBy.value = header.value
        sortAsc.value = true
    }
    const link = `${getActiveLinkUrl()}&sortBy=${sortBy.value}&sortDir=${sortAsc.value ? 'asc' : 'desc'}`
    emit('navigate', link)
}

const getActiveLinkUrl = () => {
    const link = props.links.filter(item => item.active)

    return link[0].url
}

Object.assign(itemsData.value, props.items)
</script>
<style>
@media (min-width: 640px) {
    table {
        display: inline-table !important;
    }

    thead tr:not(:first-child) {
        display: none;
    }
}
</style>