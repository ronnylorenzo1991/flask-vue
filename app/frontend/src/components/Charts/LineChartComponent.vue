<script setup lang="ts">
import { ref, watch } from 'vue'
import VueApexCharts from 'vue3-apexcharts'

const props = defineProps({
  showMenuBar: {
    default: false
  },
  series: {
    default: [],
  },
  labels: {
    default: [],
  },
  colors: {
    default: ['#ffa6a6', '#cf00ff'],
  },
  selectedMenuKey: {
    default: '',
  },
  menuOptions: {
    default: [
      {
        key: 'day',
        label: 'dia'
      }, 
      {
        key: 'week',
        label: 'semana'
      }, 
      {
        key: 'month',
        label: 'mes'
      }, 
    ],
  },
})

const selectedOption = ref(props.selectedMenuKey)
const chart = ref()

watch(() => props.selectedMenuKey, (newValue) => {
  selectedOption.value = newValue
})

const isSelectedOption = (key) => {
  return selectedOption.value === key
}

const selectOption = (key) => {
  selectedOption.value = key
}

const apexOptions = {
  legend: {
    show: false,
    position: 'top',
    horizontalAlign: 'left'
  },
  colors: props.colors,
  chart: {
    fontFamily: 'Satoshi, sans-serif',
    height: 335,
    type: 'area',

    toolbar: {
      show: false
    }
  },
  responsive: [
    {
      breakpoint: 1024,
      options: {
        chart: {
          height: 300
        }
      }
    },
    {
      breakpoint: 1366,
      options: {
        chart: {
          height: 350
        }
      }
    }
  ],
  stroke: {
    width: [2, 2],
    curve: 'straight'
  },

  labels: {
    show: false,
    position: 'top'
  },
  grid: {
    xaxis: {
      lines: {
        show: true
      }
    },
    yaxis: {
      lines: {
        show: true
      }
    }
  },
  dataLabels: {
    enabled: false
  },
  markers: {
    size: 4,
    colors: '#fff',
    strokeColors: props.colors,
    strokeWidth: 3,
    strokeOpacity: 0.9,
    strokeDashArray: 0,
    fillOpacity: 1,
    discrete: [],
    hover: {
      size: undefined,
      sizeOffset: 5
    }
  },
  xaxis: {
    type: 'category',
    categories: props.labels,
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false
    }
  },
  yaxis: {
    title: {
      style: {
        fontSize: '0px'
      }
    },
  }
}

</script>

<template>
  <div
    class="col-span-12 rounded-sm border border-stroke bg-white px-5 pt-7.5 pb-5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:col-span-8">
    <div class="flex flex-wrap items-start justify-between gap-3 sm:flex-nowrap" v-if="showMenuBar">
      <div class="flex w-full flex-wrap gap-3 sm:gap-5">
        <div class="flex min-w-47.5">
          <span
            class="mt-1 mr-2 flex h-4 w-full max-w-4 items-center justify-center rounded-full border border-primary">
            <span class="block h-2.5 w-full max-w-2.5 rounded-full bg-primary"></span>
          </span>
          <div class="w-full">
            <p class="font-semibold text-primary">Total Revenue</p>
            <p class="text-sm font-medium">12.04.2022 - 12.05.2022</p>
          </div>
        </div>
        <div class="flex min-w-47.5">
          <span
            class="mt-1 mr-2 flex h-4 w-full max-w-4 items-center justify-center rounded-full border border-secondary">
            <span class="block h-2.5 w-full max-w-2.5 rounded-full bg-secondary"></span>
          </span>
          <div class="w-full">
            <p class="font-semibold text-secondary">Total Sales</p>
            <p class="text-sm font-medium">12.04.2022 - 12.05.2022</p>
          </div>
        </div>
      </div>
      <div class="flex w-full max-w-45 justify-end">
        <div class="inline-flex items-center rounded-md bg-whiter p-1.5 dark:bg-meta-4">
          <button v-for="option in menuOptions" @click="selectOption(option.key)" :key="option.label"
            class="rounded py-1 px-3 text-xs font-medium text-black shadow-card hover:bg-white hover:shadow-card dark:text-white dark:hover:bg-boxdark" :class="{'dark:bg-boxdark bg-primary text-white': isSelectedOption(option.key)}">
            {{ option.label }}
          </button>
        </div>
      </div>
    </div>
    <div>
      <div id="chartOne" class="-ml-5">
        <VueApexCharts type="area" height="350" :options="apexOptions" :series="series" ref="chart"/>
      </div>
    </div>
  </div>
</template>
