<template>
  <TransitionRoot as="template" :show="show">
      <Dialog as="div" class="relative z-50" @close="cancel">
          <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                           leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
              <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"/>
          </TransitionChild>

          <div class="fixed inset-0 z-50 overflow-y-auto">
              <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                  <TransitionChild as="template" enter="ease-out duration-300"
                                   enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                                   enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                                   leave-from="opacity-100 translate-y-0 sm:scale-100"
                                   leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                      <DialogPanel
                          class="relative transform rounded-lg bg-white text-left shadow-xl transition-all my-8 dark:border-strokedark dark:bg-boxdark" :class="sizeClass">
                          <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900 py-4 pl-10 bg-gray-100  dark:border-strokedark dark:bg-boxdark">
                              {{ title }}
                          </DialogTitle>
                          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4  dark:border-strokedark dark:bg-boxdark">
                              <div class="sm:flex sm:items-start">
                                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left w-full">
                                      <div class="mt-2">
                                          <slot></slot>
                                      </div>
                                  </div>
                              </div>
                          </div>
                          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6" v-if="!hiddenFooter">
                              <slot name="footer">
                                  <button type="button"
                                          v-if="!hiddenCancelButton"
                                          class="inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:ml-3 sm:w-auto"
                                          @click="cancel">{{ cancelText }}
                                  </button>
                                  <button type="button"
                                          v-if="!hiddenAcceptButton"
                                          :disabled="acceptButtonDisabled" :class="acceptButtonDisabled?'bg-gray-500':'bg-white dark:border-strokedark dark:bg-boxdark hover:bg-gr'"
                                          class="mt-3 inline-flex w-full justify-center rounded-md px-3 py-2 text-sm font-semibold text-white shadow-sm border-teal-600 hover:border-teal-800 sm:mt-0 sm:w-auto"
                                          @click="accept" ref="cancelButtonRef">{{ acceptText }}
                                  </button>
                              </slot>
                          </div>
                      </DialogPanel>
                  </TransitionChild>
              </div>
          </div>
      </Dialog>
  </TransitionRoot>
</template>

<script setup>
import {computed} from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'

const props = defineProps({
  show: {
      type: Boolean,
      default: false,
  },
  size: {
      type: [String, Boolean],
      required: false,
      default: '1'
  },
  title: {
      type: String,
      default: '',
  },
  hiddenCancelButton: {
      type: Boolean,
      default: false,
  },
  hiddenAcceptButton: {
      type: Boolean,
      default: false,
  },
  hiddenFooter: {
      type: Boolean,
      default: false,
  },
  acceptButtonDisabled: {
      type: Boolean,
      default: false,
  },
  cancelText: {
      type: String,
      default: 'Cancelar',
  },
  acceptText: {
      type: String,
      default: 'Aceptar',
  },
})

const emit = defineEmits(['customChange', 'cancel', 'accept'])

const cancel = () => {
  emit('cancel')
}

const accept = () => {
  emit('accept')
}

const sizeClass = computed(() => {
  return `max-w-${props.size}xl`
})
</script>
