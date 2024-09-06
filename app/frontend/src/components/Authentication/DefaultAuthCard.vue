<script setup>
const props = defineProps(['subTitle', 'title', 'customClasses'])
</script>

<template>
  <!-- ====== Forms Section Start -->
  <div
    class="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark"
  >
    <div class="flex flex-wrap items-center">
      <div class="hidden w-full xl:block xl:w-1/2">
        <div class="py-17.5 px-26 text-center">
          <router-link class="mb-5.5 inline-block" to="/">
           <div class="flex">
            <img class="hidden dark:block" src="@/assets/images/logo.png" alt="Logo" width="60"/>
            <img class="dark:hidden" src="@/assets/images/logo.png" alt="Logo" width="60"/>
            <p class="text-xl mb-2 my-3 px-5">{{ props.title }}</p>
           </div>
          </router-link>

          <p class="font-medium 2xl:px-20">
            {{ props.subTitle }}
          </p>

          <span class="mt-15 inline-block">
            <img src="@/assets/images/illustration/illustration-03.svg" alt="illustration" />
          </span>
        </div>
      </div>
      <div class="w-full border-stroke dark:border-strokedark xl:w-1/2 xl:border-l-2">
        <div class="w-full p-4 sm:p-12.5 xl:p-17.5">
          <span class="mb-1.5 block font-medium"> Para acceder al sistema</span>
          <h2 class="mb-9 text-2xl font-bold text-black dark:text-white sm:text-title-xl2">
            Ingrese sus credenciales
          </h2>

          <slot></slot>
        </div>
      </div>
    </div>
  </div>
  <!-- ====== Forms Section End -->
</template>
