<script setup>
import { ref } from 'vue'
const props = defineProps({
  icon: {
    default: "user",
  },
  labelsColors: {
    default: { Gapping: '#FFA70B', Salmon: '#f47c70', Melanosis: '#D34053', Hematoma: '#e22e94', Cracking: '#ac5e17', Cicatriz: '#cbb79f', 'Salmon Inv': '#548f94' }
  },
  title: {
    default: "title",
  },
  label: {
    default: "",
  },
  total: {
    default: 0,
  },
  percent: {
    default: 0,
  },
})
</script>

<template>
  <!-- Card Item Start -->
  <div
    class="rounded-sm border border-stroke bg-white py-6 px-5 shadow-default dark:border-strokedark dark:bg-boxdark">
    <div class="flex">
      <div class="text-black text-lg dark:text-white w-full">
        {{ title }}
      </div>
       <div class="flex h-8 w-8 items-center justify-center rounded-full bg-meta-2 dark:bg-meta-4 ml-auto" :style="{backgroundColor: `${labelsColors[label]}50`, color: labelsColors[label]}" v-if="!Array.isArray(icon)">
        <fa-icon :icon="icon"/>
      </div>
      <div v-else v-for="ico in icon" class="flex h-8 w-8 items-center justify-center rounded-full bg-meta-2 dark:bg-meta-4 text-right -mr-3" :style="{backgroundColor: `${labelsColors[label]}50`, color: labelsColors[label]}" :key="ico">
        <fa-icon :icon="ico"/>
      </div>
    </div>

    <div class="mt-4 flex items-end justify-between">
      <div>
        <h4 class="text-title-md font-bold" :class="{'text-red blink': total <= 0, 'text-black dark:text-white': total > 0}">{{ total }}</h4>
      </div>

      <span class="flex items-center gap-1 text-sm font-medium" v-if="percent"
        :class="{ 'text-meta-3': percent > 0, 'text-meta-5': percent < 0 }">
        {{ percent }}%
        <svg v-if="percent > 0" class="fill-meta-3" width="10" height="11" viewBox="0 0 10 11" fill="none"
          xmlns="http://www.w3.org/2000/svg">
          <path
            d="M4.35716 2.47737L0.908974 5.82987L5.0443e-07 4.94612L5 0.0848689L10 4.94612L9.09103 5.82987L5.64284 2.47737L5.64284 10.0849L4.35716 10.0849L4.35716 2.47737Z"
            fill="" />
        </svg>

        <svg v-if="percent < 0" class="fill-meta-5" width="10" height="11" viewBox="0 0 10 11" fill="none"
          xmlns="http://www.w3.org/2000/svg">
          <path
            d="M5.64284 7.69237L9.09102 4.33987L10 5.22362L5 10.0849L-8.98488e-07 5.22362L0.908973 4.33987L4.35716 7.69237L4.35716 0.0848701L5.64284 0.0848704L5.64284 7.69237Z"
            fill="" />
        </svg>
      </span>
    </div>
  </div>
  <!-- Card Item End -->
</template>
<style>
.blink {
  animation: blink 1s ease-in-out infinite;
}

@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}
</style>