<template>
  <div class="relative inline-block w-12 mr-2 align-middle select-none">
    <input type="checkbox" @change="input" :name="`toggle_${label}`" :id="`toggle_${label}`" v-model="localValue"
      class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer" />
    <label :for="`toggle_${label}`"
      class="transition ease-in-out delay-150 toggle-label block overflow-hidden h-6 rounded-full bg-slate-300 cursor-pointer"></label>
  </div>
  <label for="toggle" class="text-xs text-gray-700">{{ label }}</label>
</template>       
<script setup>
import { ref } from 'vue'
const props = defineProps({
  label: String,
  modelValue: {
    default: false,
  }
})
const emit = defineEmits(['update:modelValue', 'change'])
const localValue = ref(props.modelValue)

const input = ($event) => {
  emit('update:modelValue', localValue.value)
  emit('change', $event.target.value)
}
</script>
<style scoped>
.toggle-checkbox:checked {
  transition: all 500ms ease;
  right: 0;
  @apply border-primary
}

.toggle-checkbox:checked+.toggle-label {
  transition: all 500ms ease;
  @apply bg-primary
}
</style>