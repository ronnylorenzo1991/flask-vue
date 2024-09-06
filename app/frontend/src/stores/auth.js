import { defineStore } from 'pinia'


export const authStore = defineStore('auth', {
  state: () => {
    return {
      token: '',
      authenticated: false,
      api: '',
      user_settings: [],
      active_classes: [],
      active_combined_classes: [],
      roles: [],
      permissions: [],
      user: Object,
      navs: [],
      theme: {
        sidebar: {
          open: true,
          visible: true,
          src: "./src/assets/images/sidebar/sidebar1.jpeg"
        },
        footer: {
          src: "./src/assets/images/footer.png"
        },
        color: {
          name: "blue",
          class: "bg-blue-700",
          gradient: "bg-gradient-to-r from-blue-700 to-blue-900",
          hover: "hover:bg-blue-600",
          link: "text-blue-700",
          ring: "ring-blue-700",
          input: "bg-blue-50"

        }
      },
    }
  },
  persist: true,
  actions: {
    setSession(data) {
      this.user = data.user
      this.token = data.token;
      this.authenticated = true;
      this.roles = data.roles
      // this.user_settings = data.user.settings
      this.permissions = data.permissions
      // this.active_classes = JSON.parse(data.user.settings.find(item => item.name == 'active_classes').value)
      // this.active_combined_classes = JSON.parse(data.user.settings.find(item => item.name == 'combined_classes').value)
    },
    setApi() {
      this.api = import.meta.env.VITE_API_URL
    },
    setTheme(t) {
      this.theme.color = t
    },
    collapseSidebar() {
      this.theme.sidebar.open = !this.theme.sidebar.open
    },
    hideSidebar() {
      this.theme.sidebar.visible = !this.theme.sidebar.visible
    },
    changeSrc(src) {
      this.theme.sidebar.src = src
    },
    logout() {
      this.token = null
      this.authenticated = false
      this.roles = []
      this.permissions = []
      this.user = new Object
      this.navs = []
    },
  },
})
