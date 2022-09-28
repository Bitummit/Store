<template>
  <div class="mask d-flex align-items-center h-100 gradient-custom-3 mt-5 mb-5">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-9 col-lg-7 col-xl-6">
          <div class="card" style="border-radius: 15px;">
            <div class="card-body p-5">
              <h2 class="text-uppercase text-center mb-5">Sign in</h2>

              <form>

                <div class="form-outline mb-4">
                  <input type="text" id="form3Example1cg" class="form-control form-control-lg" v-model="login"/>
                  <label class="form-label" for="form3Example1cg">Username</label>
                </div>

                <div class="form-outline mb-4">
                  <input type="password" id="form3Example4cg" class="form-control form-control-lg" v-model="password"/>
                  <label class="form-label" for="form3Example4cg">Password</label>
                </div>

                <div class="d-flex justify-content-center">
                  <button type="button"
                          class="btn btn-success btn-block btn-lg gradient-custom-4 text-body" @click="auth">Sign in
                  </button>
                </div>
                <div class="text-center mt-3">
                  <p>Not a member?
                    <RouterLink :to='{name: "register"}'><a class="fw-bold text-body" ><u>Register now</u></a>
                    </RouterLink>
                  </p>

                </div>

              </form>

            </div>
          </div>
        </div>
      </div>
    </div>
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
            this.$store.commit('setToken', token)
            localStorage.setItem('token', token)
            this.$router.push({name: 'catalog'})
            axios.defaults.headers.common['Authorization'] = 'Token' + token
          }).catch(error => console.error(error.response.data))

    },
    // getOrCreateCart() {
    //   let token = localStorage.getItem('token')
    //   axios.get(`http://127.0.0.1:8000/api/cart/`,)
    //       .then(response => {
    //         this.item = response.data
    //
    //       })
    // }
  }
}
</script>

<style scoped>

</style>