<script setup lang="ts">
import { ref, computed } from 'vue'
// @ts-ignore
import VueApexCharts from 'vue3-apexcharts'

const props = defineProps({
  series: {
    default: []
  },
  labels: {
    default: []
  },
  colors: {
    default: ['#FFA70B', '#f47c70', '#D34053', '#e22e94', '#ac5e17', '#cbb79f', '#548f94']
  },
  labelsColors: {
    default: { Gapping: '#FFA70B', Salmon: '#f47c70', Melanosis: '#D34053', Hematoma: '#e22e94', Cracking: '#ac5e17', Cicatriz: '#cbb79f', 'Salmon Inv': '#548f94' }
  },
  title: {
    default: 'Donut Chart Component'
  },
  rangeOptions: {
    default: [
      {
        title: 'Este Dia',
        value: 'day'
      },
      {
        title: 'Esta Semana',
        value: 'week'
      },
      {
        title: 'Este Mes',
        value: 'month'
      },
    ]
  },
})

const chart = ref(null)
const orderedLabelsColors = {}
const orderedColors = []

props.labels.forEach(label => {
  orderedLabelsColors[label] = props.labelsColors[label]
  orderedColors.push(orderedLabelsColors[label])
})


const apexOptions = {
  chart: {
    type: 'donut',
    width: 380
  },
  colors: orderedColors,
  labels: props.labels,
  legend: {
    show: false,
    position: 'bottom'
  },
  plotOptions: {
    pie: {
      donut: {
        size: '65%',
        background: 'transparent'
      }
    }
  },
  dataLabels: {
    enabled: false
  },
  responsive: [
    {
      breakpoint: 640,
      options: {
        chart: {
          width: 200
        }
      }
    }
  ]
}
</script>

<template>
  <div
    class="col-span-12 rounded-sm border border-stroke bg-white p-7.5 shadow-default dark:border-strokedark dark:bg-boxdark xl:col-span-4">
    <div class="mb-3 justify-between gap-4 sm:flex">
      <div>
        <h4 class="text-xl font-bold text-black dark:text-white">{{ title }}</h4>
      </div>
      <div>
        <div class="relative z-20 inline-block">
          <select name="selectRange" id="selectRange"
            class="relative z-20 inline-flex appearance-none bg-transparent py-1 pl-3 pr-8 text-sm font-medium outline-none">
            <option :value="option.value" v-for="option in rangeOptions">{{ option.title }}</option>
          </select>
          <span class="absolute top-1/2 right-3 z-10 -translate-y-1/2">
            <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M0.47072 1.08816C0.47072 1.02932 0.500141 0.955772 0.54427 0.911642C0.647241 0.808672 0.809051 0.808672 0.912022 0.896932L4.85431 4.60386C4.92785 4.67741 5.06025 4.67741 5.14851 4.60386L9.09079 0.896932C9.19376 0.793962 9.35557 0.808672 9.45854 0.911642C9.56151 1.01461 9.5468 1.17642 9.44383 1.27939L5.50155 4.98632C5.22206 5.23639 4.78076 5.23639 4.51598 4.98632L0.558981 1.27939C0.50014 1.22055 0.47072 1.16171 0.47072 1.08816Z"
                fill="#637381" />
              <path fill-rule="evenodd" clip-rule="evenodd"
                d="M1.22659 0.546578L5.00141 4.09604L8.76422 0.557869C9.08459 0.244537 9.54201 0.329403 9.79139 0.578788C10.112 0.899434 10.0277 1.36122 9.77668 1.61224L9.76644 1.62248L5.81552 5.33722C5.36257 5.74249 4.6445 5.7544 4.19352 5.32924C4.19327 5.32901 4.19377 5.32948 4.19352 5.32924L0.225953 1.61241C0.102762 1.48922 -4.20186e-08 1.31674 -3.20269e-08 1.08816C-2.40601e-08 0.905899 0.0780105 0.712197 0.211421 0.578787C0.494701 0.295506 0.935574 0.297138 1.21836 0.539529L1.22659 0.546578ZM4.51598 4.98632C4.78076 5.23639 5.22206 5.23639 5.50155 4.98632L9.44383 1.27939C9.5468 1.17642 9.56151 1.01461 9.45854 0.911642C9.35557 0.808672 9.19376 0.793962 9.09079 0.896932L5.14851 4.60386C5.06025 4.67741 4.92785 4.67741 4.85431 4.60386L0.912022 0.896932C0.809051 0.808672 0.647241 0.808672 0.54427 0.911642C0.500141 0.955772 0.47072 1.02932 0.47072 1.08816C0.47072 1.16171 0.50014 1.22055 0.558981 1.27939L4.51598 4.98632Z"
                fill="#637381" />
            </svg>
          </span>
        </div>
      </div>
    </div>
    <div class="mb-2">
      <div id="chartThree" class="mx-auto flex justify-center">
        <VueApexCharts type="donut" width="340" :options="apexOptions" :series="series" ref="chart" />
      </div>
    </div>

    <div class="-mx-8 flex flex-wrap items-center justify-center gap-y-3">
      <div class="w-full px-8 sm:w-1/3" v-for="(label, key) in labels">
        <div class="flex w-full items-center">
          <span class="mr-2 block h-3 w-full max-w-3 rounded-full"
            :style="{ backgroundColor: orderedLabelsColors[label] }"></span>
          <p class="flex w-full justify-between text-sm font-medium text-black dark:text-white">
            <span> {{ label }} </span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
