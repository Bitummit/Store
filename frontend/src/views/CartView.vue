<template>

  <UnloginCart v-if="!login"/>
  <LoginCart v-else cart=cart />

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
      login: false,
      cart: this.$store.state.cart
    }
  },
  mounted() {
    if (localStorage.getItem('token') !== '') {
      this.login = true
      this.getCart()
    } else {
      this.login = false
    }
  },
  methods: {
    getCart() {
      // axios.get(`http://127.0.0.1:8000/api/cart/${this.cart.id}/`)
      //     .then(response => {
      //       this.items = response.data
      //     })
    },
  }

}
</script>

<style scoped>

</style>