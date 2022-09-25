<template>
  <body>
  <Items :items="items"/>
  </body>

</template>

<script>
import Items from '@/components/Items.vue'
import axios from "axios";

export default {
  name: "Category",
  components: {Items},
  props: ['category'],
  data() {
    return {
      items: [],
    }
  },
  mounted() {
    this.getItemsByCategory()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'view_by_category') {
        this.getItemsByCategory()
      }
    }
  },

  methods: {
    getItemsByCategory() {
      let headers = {
        'Content-Type': 'application/json'
      }
      if (this.$store.state.isAuth) {
        headers['Authorization'] = 'Token' + this.$store.state.token
      }

      axios.get(`http://127.0.0.1:8000/api/items/by/category/${this.category}/`, {headers})
          .then(response => {
            this.items = response.data
          })
    }
  }
}
</script>

<style scoped>

</style>