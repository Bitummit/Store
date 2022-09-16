<template>

  <div class="container">
<!--    <div class="row row-cols-1 row-cols-md-3 g-4">-->
<!--      <div class="col mt-5" v-for="item in items" :key="item.name">-->
<!--        <div class="card">-->

<!--          <img class="card-img-top" style="" :src="item.image">-->
<!--          <div class="card-body">-->
<!--            <p class="card-text">{{ item.price }}</p>-->
<!--            <h5 class="card-title">{{ item.name }}</h5>-->

<!--          </div>-->
<!--          <div class="card-footer">-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->

    <div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
</div>

  </div>





</template>

<script>
import axios from "axios";

export default {
  name: "Catalog",
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

<style scoped>

</style>