<script>
import {RouterLink, RouterView} from 'vue-router'
import axios from "axios";

export default {
  data() {
    return {
      categories: [],
    }
  },
  mounted() {
    this.getCategories()
  },

  methods: {
    getCategories() {
      axios.get('http://127.0.0.1:8000/api/category/')
          .then(response => {
            this.categories = response.data
          })

    }
  },
  watch: {

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
            <RouterLink :to='{name: "login"}'><a>Login/</a></RouterLink>
            <RouterLink :to='{name: "cart"}'><a>Register</a></RouterLink>
            </span>
          <span v-else>
            <a class="nav-link"></a>
            <RouterLink :to='{name: "login"}'><a>My account/</a></RouterLink>
            <RouterLink :to='{name: "cart"}'><a>Logout</a></RouterLink>
          </span>
        </span>
        <span class="navbar-text mr-5">
              <RouterLink :to='{name: "cart"}'><a class="nav-link">Cart</a></RouterLink>
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
