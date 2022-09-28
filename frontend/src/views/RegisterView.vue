<template>
  <div class="mask d-flex align-items-center h-100 gradient-custom-3 mt-5 mb-5">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-9 col-lg-7 col-xl-6">
          <div class="card" style="border-radius: 15px;">
            <div class="card-body p-5">
              <h2 class="text-uppercase text-center mb-5">Create an account</h2>

              <form @submit.prevent="submitForm">

                <div class="form-outline mb-4">
                  <input type="text" id="form3Example1cg" class="form-control form-control-lg" v-model="username"/>
                  <label class="form-label" for="form3Example1cg">Username</label>
                </div>

                <div class="form-outline mb-4">
<!--                  type="email"-->
                  <input  type="text" id="form3Example3cg" class="form-control form-control-lg" v-model="email"/>
                  <label class="form-label" for="form3Example3cg">Email</label>
                </div>

                <div class="form-outline mb-4">
                  <input type="password" id="form3Example4cg" class="form-control form-control-lg" v-model="password"/>
                  <label class="form-label" for="form3Example4cg">Password</label>
                </div>

                <div class="form-outline mb-4">
                  <input type="password" id="form3Example4cdg" class="form-control form-control-lg" v-model="password2"/>
                  <label class="form-label" for="form3Example4cdg">Repeat your password</label>
                </div>

                <div class="alert alert-danger" role="alert" v-if="errors.length">
                    <p v-for="error in errors" :key="error"> {{error}} </p>
                </div>

                <div class="d-flex justify-content-center">
                  <button type="submit"
                    class="btn btn-success btn-block btn-lg gradient-custom-4 text-body">Register</button>
                </div>



              </form>
              <p class="text-center text-muted mt-5 mb-0">Have already an account?
                  <RouterLink :to='{name: "login"}'><a class="fw-bold text-body"><u>Login here</u></a></RouterLink>
                </p>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "RegisterView",
  data() {
    return {
      username: '',
      email: '',
      password: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    submitForm() {
      this.errors = []

      if(this.username === '') {
        this.errors.push('The username field is empty!')
      }
      if(this.password === '') {
        this.errors.push('The password is too short')
      }
      if(this.password !== this.password2) {
        this.errors.push('The passwords doens\'t match')
      }
      if(this.email === '') {
        this.errors.push('The email field is empty!')
      }
      if(!this.email.includes('@') || !this.email.includes('.')) {
        this.errors.push('The email is wrong!')
      }

      if(!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios.post('http://127.0.0.1:8000/api/users/', formData)
            .then(response => {
              this.$router.push('/login')
            }).catch(error => {
              if(error.response) {
                for( const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
                console.log(JSON.stringify(error.response.data))
              } else if(error.message) {
                this.errors.push('Something went wrong. Please try again')

                console.log(JSON.stringify(error))
              }
        })
      }
    },
  }

}
</script>

<style scoped>

</style>