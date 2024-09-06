<script setup lang="ts">
import { onMounted, ref } from 'vue'
const props = defineProps({
  title: {
    default: 'Carousel'
  },
  images: {
    default: [],
  }
})

const active = ref(0)

onMounted(() => {
  let i = 0;
    setInterval(() => {
      if (i > props.images.length - 1) {
        i = 0;
      }
      active.value = i;
      i++;
    }, 2000);
})
</script>

<template>
  <div
    class="col-span-12 rounded-sm border border-stroke bg-white p-7.5 shadow-default dark:border-strokedark dark:bg-boxdark xl:col-span-4"
  >
    <div class="mb-4 justify-between gap-4 sm:flex">
      <div>
        <h4 class="text-xl font-bold text-black dark:text-white">{{ title }}</h4>
      </div>
    </div>

    <div>
      <div id="Carousel" class="-ml-5 -mb-9">
        <div class="relative slide">
          <div class="carousel-indicators absolute bottom-0 flex h-24 w-full justify-center items-center">
            <ol class="z-50 flex w-4/12 justify-center">
              <li v-for="(img, key) in images" :key="key"
                class="md:w-4 md:h-4 bg-gray-300 rounded-full cursor-pointer mx-2"></li>
            </ol>
          </div>
          <div class="carousel-inner relative overflow-hidden w-full">
            <div v-for="(img, key) in images" :id="`slide-${key}`" :key="key"
              :class="`${active === key ? 'active' : 'left-full'}`"
              class="carousel-item inset-0 relative w-full transform transition-all duration-500 ease-in-out">
              <img class="block w-full" :src="img" alt="First slide" />
            </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>
<style>
		.left-full {
			left: -100%;
		}

		.carousel-item {
			float: left;
			position: relative;
			display: block;
			width: 100%;
			margin-right: -100%;
			backface-visibility: hidden;
		}

		.carousel-item.active {
			left: 0;
		}
	</style>