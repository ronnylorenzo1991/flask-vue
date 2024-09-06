<script setup>
import DefaultAuthCard from "@/components/Authentication/DefaultAuthCard.vue"
import InputGroup from "@/components/Authentication/InputGroup.vue"
import { ref } from "vue"
import { authStore } from "@/stores/auth"
import { useRouter } from "vue-router"
import axios from "axios"
const isLoading = ref(false)
const router = useRouter()
const flashOption = ref({})
const auth_store = authStore()

const username = ref("")
const password = ref("")
const title = import.meta.env.VITE_APP_NAME
const subTitle = import.meta.env.VITE_APP_TITLE

const getFirstRouteWithPermission = () => {
 
  const route = "/login";
  if (!auth_store.permissions) {
    return route;
  }

  if (auth_store.permissions.includes("dashboard")) {
    return "/dashboard";
  }

  if (!auth_store.permissions.includes("dashboard")) {
    return "/dashboard";
  }

  return route;
};

if (auth_store.user != null) {
  router.push(getFirstRouteWithPermission());
}

async function login() {
  isLoading.value = true;

  const credentials = {
    username: username.value,
    password: password.value,
  };
  await axios
    .post(`${auth_store.api}/login`, credentials)
    .then((response) => {
      auth_store.setSession(response.data);
      if (auth_store.user != null) {
        router.push(getFirstRouteWithPermission());
      }
    })
    .catch((error) => {
      isLoading.value = false;
      if (typeof error.response.data !== "undefined")
        flashOption.value = {
          open: true,
          title: "Atencion",
          message: error.response.data.message,
        };
    });
}

</script>

<template>
  <div class="my-36 mx-36">
    <DefaultAuthCard :subTitle="subTitle" :title="title">
      <InputGroup label="Nombre de usuario o teléfono" placeholder="Nombre de usuario o teléfono" v-model="username">
        <fa-icon icon="user" />
      </InputGroup>

      <InputGroup label="Contraseña" type="password" placeholder="Contraseña" v-model="password">
        <fa-icon icon="lock" />
      </InputGroup>

      <div class="mb-5 mt-6">
        <button @click="login"
          class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90">
          Acceder
        </button>
      </div>
    </DefaultAuthCard>
  </div>
</template>
