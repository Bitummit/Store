<template>
  <div class="container mt-5 w-25">
<form>
  <div class="form-outline mb-4">
    <input type="email" id="form2Example1" class="form-control" v-model="login"/>
    <label class="form-label" for="form2Example1">Email address</label>
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
  <button type="button" class="btn btn-primary btn-block mb-4" @click="consoleText">Sign in</button>

  <div class="text-center">
    <p>Not a member? <a href="#">Register</a></p>

  </div>
</form>
    </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      login: "",
      password: "",
    }
  },
  methods: {
    consoleText() {
      console.log(this.password)
      console.log(this.login)
    }
  }
}
</script>

<style scoped>

</style>