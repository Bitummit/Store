<template>
  <div class="mask d-flex align-items-center h-100 gradient-custom-3 mt-5 mb-5">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-9">
          <div class="card" style="border-radius: 15px;">
            <div class="card-body p-5">
              <div>
                <h2 class="text-uppercase text-center mb-5">My account </h2>
                <div v-if="!editing">
                  <h5>
                    {{ user.username }}
                    <a class="ml-2 btn" style="cursor: pointer">
                      <img class="editButton" src="public/edit_button.png" title="Edit username"
                           @click="makeEditUsernameForm">
                    </a>
                  </h5>
                </div>
                <div v-else>
                  <input v-model="user.username">
                  <a class="ml-2 btn" style="cursor: pointer">
                    <img class="editButton" src="public/save_button.png" title="Save username" @click="saveUsername">
                  </a>
                  <a class=" btn" style="cursor: pointer">
                    <img class="editButton" src="public/cancel_button.png" title="Save username"
                         @click="makeEditUsernameForm">
                  </a>
                  <div class="alert alert-danger" role="alert" v-if="error.length">
                    <p> {{ error }} </p>
                  </div>
                </div>
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
      otherUsernames: [],
      editing: false,
      error: '',
      savedUsername: '',
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
          }).catch(error => console.error(error.response.data))
    },
    getUser() {
      axios.get(`http://127.0.0.1:8000/api/user/by/token/${this.token}/`)
          .then(response => {
            this.user = response.data
            this.savedUsername = this.user.username
          }).catch(error => console.error(error.response.data))
    },
    makeEditUsernameForm() {
      this.error = ''
      this.editing = !this.editing
    },
    saveUsername() {
      axios.get('http://localhost:8000/api/users/')
            .then(response => {
              let users = response.data

                // this.otherUsernames.push(users['username'])

              // console.log(this.otherUsernames)
            }).catch(error => console.error(error.response.data))

      if (this.savedUsername === this.user.username) {
        this.error = 'You haven\'t change username'

      } else {

        axios.patch(`http://localhost:8000/api/users/${this.user.id}/`, {username: this.user.username})
            .then(response => {
              this.editing = !this.editing
              this.savedUsername = this.user.username
            }).catch(error => {
              this.error = 'This username is in use. Please enter one more'
              console.error(error.response.data)
            }
        )
      }
    }
  },

}


</script>

<style scoped>

.editButton {
  width: 20px;
  height: 20px;
  transition: 0.5s;

}

.editButton:hover {
  transform: scale(1.1);
}

</style>