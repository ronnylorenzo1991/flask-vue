<script setup>
import { ref, computed } from 'vue'
const emit = defineEmits(['update:modelValue', 'change'])

const changed = ($event) => {
  emit('update:modelValue', localValue.value)
  emit('change', $event.target.value)
  isOptionSelected.value = true
}

const isOptionSelected = ref(false)

const props = defineProps({
  icon: {
    default: "user",
  },
  placeholder: {
    default: "Seleccione un elemento",
  },
  label: {
    default: "Opciones",
  },
  options: {
    default: {},
  },
  modelValue: {
    default: false,
  },
  validation: {
    default: ''
  }
})
const getDynamicClass = computed(() => {
  return props.validation ? 'border-primary' : 'border-stroke'
})
const localValue = ref(props.modelValue)
</script>

<template>
  <div>
    <label class="mb-3 block text-sm font-medium text-black dark:text-white">
      {{ label }}
    </label>
    <div class="relative z-20 bg-white dark:bg-form-input">
      <span class="absolute top-1/2 left-4 z-30 -translate-y-1/2">
        <fa-icon :icon="icon" />
      </span>
      <select
        v-model="localValue"
        :class="[{ 'text-black dark:text-white': isOptionSelected }, getDynamicClass]"
        @change="changed"
        class="relative z-20 w-full appearance-none rounded border bg-transparent py-3 px-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input"
      >
        <option value="-1" disabled>{{ placeholder }}</option>
        <option :value="key" class="text-body dark:text-bodydark" v-for="(option, key) in options" :key="key">{{ option }}</option>
      </select>
      <span class="absolute top-1/2 right-4 z-20 -translate-y-1/2">
        <fa-icon icon="chevron-down" />
      </span>
      <div class="absolute pb-6 mb-5">
        <label class="text-[#ff309e] text-xs" v-text="validation"></label>
      </div>
    </div>
  </div>
</template>
