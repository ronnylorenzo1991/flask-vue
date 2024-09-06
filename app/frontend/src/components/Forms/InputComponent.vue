<script setup>
import { ref, computed, watch } from 'vue'

const emit = defineEmits(['update:modelValue'])

const props = defineProps({
  label: String,
  type: String,
  placeholder: String,
  customClasses: String,
  required: {
    type: Boolean,
    default: false
  },
  modelValue: {
    default: null,
  },
  validation: {
    default: ''
  }
})

const validationText = ref('');

watch(() => props.validationError, (newValue) => {
  validationText.value = newValue
})

const getDynamicClass = computed(() => {
  return props.validation ? 'border-primary' : 'border-stroke'
})

const input = ($event) => {
  validationText.value = ''
  emit('update:modelValue', $event.target.value)
}
</script>

<template>
  <div :class="customClasses">
    <label class="mb-2.5 block text-black dark:text-white">
      {{ label }}
      <span v-if="required" class="text-danger">*</span>
    </label>
    <input :type="type ? type : 'text'" :placeholder="placeholder" @input="input" :value="modelValue"
      class="w-full rounded border-[1.5px] text-black bg-transparent py-3 px-5 font-normal outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:text-white dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary"
      :class="getDynamicClass" />
    <div class="absolute pb-6">
      <label class="text-danger text-xs" v-text="validation"></label>
    </div>
  </div>
</template>
