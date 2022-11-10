<template>
  <div class="card mt-5 ml-5 mr-5">
    <img class="card-img-top" :src="item.image">
    <div class="card-body card-text">
      <h5 class=" text-center">{{ item.name }} </h5>
      <p class="text-center">{{ item.price }} $</p>
      <p class="text-center mt-5">{{ item.desc }}</p>
      <p class="card-text ml-5 mt-5"> Materials: <span v-for="material in item.material" :key="material.name">{{ material }}</span></p>
      <div class="ml-5">
          <ul class="size">
            <li v-for="size_in_stock in item.sizes_in_stock" :key='size_in_stock.size'>
              <input type="radio"  :id=size_in_stock :value=size_in_stock v-model="checked_size"/>
              <label :for=size_in_stock>{{size_in_stock}}</label>
            </li>
          </ul>
        </div>
      <button type="button" class="btn btn-dark" :disabled="checkSize===''" @click="addToCart">Add to cart</button>
    </div>
  </div>

</template>

<script>
import axios from "axios";


export default {
  name: "CatalogView",
  data() {
    return {
      item: {},
      cart: this.$store.state.cart,
      checked_size: '',
    }
  },
  props: ['name'],

  mounted() {
    this.getItem()

  },

  methods: {
    getItem() {
      axios.get(`http://127.0.0.1:8000/api/items/detail/${this.name}/`, )
          .then(response => {
            this.item = response.data

          })

    },
    addToCart() { // to store
      axios.post('http://localhost:8000/api/cartProduct/', {
        item: this.item.id,
        size: this.checked_size,
        qty: 1,
        final_price: this.item.price
      }).then(response => {
            let cartProduct = response.data
            this.cart.items.push(cartProduct)
            this.$store.commit('setCart', this.cart)
          })
          .catch(error => console.error(error.response.data))

      this.updateCart(this.cart)

    },
    updateCart(cart) {
      axios.put(`http://localhost:8000/api/cart/${cart.id}/`, cart)
          .then(response => {
                this.$store.state.cart = response.data
              }).catch(error => console.error(error.response.data))
    },
  },

}

</script>

<style scoped>
.size {
  list-style-type: none;
  margin: 25px 0 0 0;
  padding: 0;
}

.size li {
  float: left;
  margin: 0 5px 0 0;
  width: 100px;
  height: 40px;
  position: relative;
}

.size label,
.size input {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.size input[type="radio"] {
  opacity: 0.01;
  z-index: 100;
}

.size input[type="radio"]:checked+label,
.Checked+label {
  background: yellow;
}

.size label {
  padding: 5px;
  border: 1px solid #CCC;
  cursor: pointer;
  z-index: 90;
}

.size label:hover {
  background: #DDD;
}
</style>