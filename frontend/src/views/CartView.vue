<template>

  <UnloginCart v-if="!login"/>
  <LoginCart v-else/>

</template>

<script>
import UnloginCart from '@/components/UnloginCart.vue';
import LoginCart from '@/components/LoginCart.vue';
import axios from "axios";

export default {
  name: "CartView",
  components: {UnloginCart, LoginCart},
  data() {
    return {
      login: false
    }
  },
  mounted() {
    if (localStorage.getItem('token') !== '') {
      this.login = true
    } else {
      this.login = false
    }
  },
  methods: {
    getItems() {
      axios.get('http://127.0.0.1:8000/order/', )
          .then(response => {
            this.items = response.data
          })
    },
  }

}
</script>

<style scoped>

</style>