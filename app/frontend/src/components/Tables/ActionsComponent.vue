<template>
    <Menu as="div" class="inline-block text-left z-9999">
        <div>
            <MenuButton
                class="inline-flex w-full justify-center rounded-xl px-2 py-2 text-sm bg-inherit font-semibold text-gray-900 hover:bg-primary hover:text-white">
                <fa-icon icon="bars"/>
            </MenuButton>
        </div>

        <transition enter-active-class="transition ease-out duration-100"
                    enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                    leave-active-class="transition ease-in duration-75"
                    leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
            <MenuItems
                class="absolute z-50 sm:right--5 mt-2 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none dark:bg-boxdark">
                <div class="py-1">
                    <slot name="menu-items">

                    </slot>
                </div>
            </MenuItems>
        </transition>
    </Menu>
</template>

<script setup>
import {Menu, MenuButton, MenuItems} from '@headlessui/vue'
</script>
