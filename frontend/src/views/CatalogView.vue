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

      axios.get('http://127.0.0.1:8000/api/items/')
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