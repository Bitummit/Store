<template>
  <div class="mask d-flex align-items-center h-100 gradient-custom-3 mt-5 mb-5">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-9">
          <div class="card" style="border-radius: 15px;">
            <div class="card-body p-5">
              <div style="display: inline-block" class="mb-5">
                <h2 class="text-uppercase">My account </h2>
                <h5>{{ user.username }}</h5>
              </div>


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
  name: "MyAccountView",
  data() {
    return {
      customer: {},
      user: {},
      token: '',
    }
  },
  mounted() {
    this.token = this.$store.state.token
    this.getCustomer()
    this.getUser()
  },
  methods: {
    getCustomer() {

      axios.get(`http://127.0.0.1:8000/api/customer/profile/${this.token}/`)
          .then(response => {
            this.customer = response.data
            console.log(this.customer)
          }).catch(error => console.error(error.response.data))
    },
    getUser() {
      axios.get(`http://127.0.0.1:8000/api/user/by/token/${this.token}/`)
          .then(response => {
            this.user = response.data
            console.log(this.user)
          }).catch(error => console.error(error.response.data))
    },
  },

}


</script>

<style scoped>

</style>