<template>
    <component :is="tr" :class="getRowColor" class="z-10 shadow-md sm:shadow-none rounded-r-lg flex flex-col flex-no wrap sm:table-row mb-2 sm:mb-0 sm:border-none text-sm sm:text-md">
        <template v-if="!isChildrenRow">
            <td @click="$emit('expandRow', index)" class="p-2 sm:py-5">
                <div class="w-full mx-auto sm:px-4 font-semibold dark:text-white" :class="hasChildren() ? 'cursor-pointer' : null" :data-cy="`${index}-${currentPage}-${perPage}`">
                    {{ (index + 1) + (currentPage * perPage) - perPage }}
                    <fa-icon icon="caret-right" v-if="hasChildren() && !isExpanded(index)" />
                    <fa-icon icon="caret-down" v-if="hasChildren() && isExpanded(index)" />
                </div>
            </td>
            <td v-for="header in columns" :key="header.id" class="p-2 truncate overflow-hidden max-w-60 sm:max-w-full sm:text-wrap" :data-cy="`column-${header.value}`">
                <slot :name="`column-${header.value}`" v-bind:item="item">
                    {{ helpers.nativeGet(item, header.value) }}
                </slot>
            </td>
            <td v-if="withActions" class="p-[3px] sm:p-0 w-[10%] text-center">
                <slot name="actions-cell">
                    <actions>
                        <template v-slot:menu-items>
                            <MenuItems v-slot="{ active }" v-for="action in actions" :key="action" class="flex dark:hover:bg-zinc-500 hover:bg-zinc-200">
                                <a href="#" @click.stop.prevent="$emit(action.event, item)" :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'px-4 py-2 text-xs flex dark:hover:bg-zinc-500 hover:bg-zinc-200']">
                                <fa-icon :icon="action.icon" class="pr-4 text-xs"/>
                                {{ action.text }}</a>
                            </MenuItems>
                        </template>
                    </actions>
                </slot>
            </td>
        </template>
        <template v-else>
            <td colspan="99" v-if="hasChildren()" class="p-2" v-show="isExpanded(index)">
                <table class="w-full text-xs text-left">
                    <thead>
                        <tr class="border-2 bg-gray-200 py-3 px-6 w-[50%]">
                            <td v-for="header in childrenColumns" class="p-2" :key="header.id">
                                {{ header.text }}
                            </td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(children, index) of helpers.nativeGet(item, childrens)" :key="index">
                            <td v-for="header in childrenColumns" :key="header.id" class="p-2">
                                <span>{{ helpers.nativeGet(children, header.value) || "-" }}</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </template>
    </component>
</template>

<script setup>
import helpers from '../../libs/helpers'
import { computed } from 'vue'
import {MenuItems} from '@headlessui/vue'
import Actions from './ActionsComponent.vue'

const tr = 'tr'
const props = defineProps({
    item: {
        default: null,
    },
    index: {
        type: Number,
        default: 0
    },
    withActions: {
        type: Boolean,
        default: false,
    },
    isChildrenRow: {
        type: Boolean,
        default: false,
    },
    columns: {
        default: [],
    },
    childrenColumns: {
        default: [],
    },
    expandedRows: {
        default: [],
    },
    actions: {
        default: [],
    },
    childrens: {
        default: ''
    },
    currentPage: {
        default: 1
    },
    perPage: {
        default: 10
    },
})

const hasChildren = () => {
    return helpers.nativeGet(props.item, props.childrens, []).length > 0
}

const isExpanded = (index) => {
    return props.expandedRows.includes(index)
}

const getRowColor = computed(() => {
    if (props.isChildrenRow) {
        return 'bg-gray-50'
    }

    return props.index % 2 == 0 ? 'dark:hover:bg-slate-800' : 'dark:hover:bg-slate-700'
})
</script>

<style scoped></style>
