<script>

import Items from '@/components/Items.vue'
import axios from "axios";

export default {
  name: "CatalogView",
  components: {Items},
  data() {
    return {
      items: [],
    }
  },

  mounted() {
    this.getItems()

  },

  methods: {
    getItems() {
      let headers = {
        'Content-Type': 'application/json'
      }
      if (this.$store.state.isAuth) {
        headers['Authorization'] = 'Token' + this.$store.state.token
      }
      axios.get('http://127.0.0.1:8000/api/items/', {headers})
          .then(response => {
            this.items = response.data
          })
    }
  },

}

</script>

<template>
  <body>
  <Items :items="items"/>
  </body>


</template>

<style scoped>

</style>