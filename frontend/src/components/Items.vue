<template>
<body>
  <div class="container px-4 px-lg-5 mt-5">

    <div class="card-columns">
      <div class="card text-center h-50" v-for="item in items" :key="item.name">
        <img class="card-img-top" :src="item.image">
        <div class="card-body">
          <p class="card-text">{{ item.price }} $</p>
          <h5 class="card-title">{{ item.name }}</h5>
          <RouterLink :to="{name: 'detail-item-view', params: {name: item.name}}"><button type="button" class="btn btn-info">View details</button></RouterLink>
        </div>
      </div>


    </div>
  </div>
</body>
</template>

<script>
export default {
  name: "Items",
  props: ['items'],
}
</script>

<style scoped>

</style>