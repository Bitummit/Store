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
      if(to.name === 'view_by_category') {
        this.getItemsByCategory()
      }
    }
  },

  methods: {
    getItemsByCategory() {
      axios.get(`http://127.0.0.1:8000/api/items/by/category/${this.category}/`)
          .then(response => {
            this.items = response.data
          })
    }
  }
}
</script>

<style scoped>

</style>