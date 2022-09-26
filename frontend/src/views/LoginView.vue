<template>
  <div class="container mt-5 w-25">
    <form>
      <div class="form-outline mb-4">
        <input type="email" id="form2Example1" class="form-control" v-model="login"/>
        <label class="form-label" for="form2Example1">Username</label>
      </div>
      <div class="form-outline mb-4">
        <input type="password" id="form2Example2" class="form-control" v-model="password"/>
        <label class="form-label" for="form2Example2">Password</label>
      </div>

      <!--  <div class="row mb-4">-->
      <!--    <div class="col d-flex justify-content-center">-->
      <!--      <div class="form-check">-->
      <!--        <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />-->
      <!--        <label class="form-check-label" for="form2Example31"> Remember me </label>-->
      <!--      </div>-->
      <!--    </div>-->

      <!--    <div class="col">-->
      <!--      <a href="#!">Forgot password?</a>-->
      <!--    </div>-->
      <!--  </div>-->

      <!-- Submit button -->
      <button type="button" class="btn btn-primary btn-block mb-4" @click="auth">Sign in</button>

      <div class="text-center">
        <p>Not a member? <a href="#">Register</a></p>

      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
  name: "LoginView",
  data() {
    return {
      login: "",
      password: "",
    }
  },
  methods: {
    auth() {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')
      axios.post('http://127.0.0.1:8000/api/token/login/', {username: this.login, password: this.password})
          .then(response => {
            const token = response.data.auth_token
            console.log(token)
            this.$store.commit('setToken', token)
            localStorage.setItem('token', token)
            this.$router.push({name: 'catalog'})
            axios.defaults.headers.common['Authorization'] = 'Token' + token
          }).catch(error => console.error(error.response.data) )
    }
  }
}
</script>

<style scoped>

</style>