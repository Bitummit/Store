<script>
import {RouterLink, RouterView} from 'vue-router'
import axios from "axios";

export default {
  data() {
    return {
      categories: [],
      token: '',
      cart: {},
    }
  },
  beforeCreate() {
    this.$store.commit("initStore")

    this.token = this.$store.state.token

    if (this.token) {
      axios.defaults.headers.common['Authorization'] = 'Token'+this.token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted() {
    this.getCategories()
    this.cart = this.$store.state.cart
    console.log(this.$store.state.cart)
  },

  methods: {
    getCart() {

    },
    getCategories() {
      axios.get('http://127.0.0.1:8000/api/category/')
          .then(response => {
            this.categories = response.data
          })

    },
    logout() {
      this.$store.commit('removeToken')
      localStorage.setItem('token', '')
      this.$router.push({name: 'catalog'})
    }
  },
  computed: {
    cartTotalLength() {

      let totalLength = 0

      for(let i = 0; i < this.cart.length; i++) {
        totalLength += 1
      }
      return totalLength
    }
  }
}
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand">Shopper</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <RouterLink :to="{name: 'catalog'}"><a class="nav-link">Catalog</a></RouterLink>

          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
               aria-haspopup="true" aria-expanded="false">
              Category
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <RouterLink v-for="category in categories" :key="category.name"
                          :to="{name: 'view_by_category', params: {category: category.name}}"><a class="dropdown-item">
                {{ category.name }} </a></RouterLink>
            </div>
          </li>
        </ul>
        <span class="navbar-text mr-3">
          <span v-if="!$store.state.isAuth">
            <RouterLink :to='{name: "login"}'><button type="button" class="btn btn-info mr-3">Login </button></RouterLink>
            <RouterLink :to='{name: "register"}'><button type="button" class="btn btn-info mr-3">Register </button></RouterLink>
            </span>
          <span v-else>
            <RouterLink :to='{name: "account"}'><button type="button" class="btn btn-info mr-3">My account </button></RouterLink>
            <button @click="logout" type="button" class="btn btn-danger">Logout </button>
          </span>
        </span>
        <span class="navbar-text mr-5">
              <RouterLink :to='{name: "cart"}'><button type="button" class="btn btn-success">Cart ({{cartTotalLength}})</button></RouterLink>
        </span>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
  </header>

  <RouterView/>
</template>

<style scoped>

</style>
