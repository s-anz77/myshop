<script>
import { RouterView } from 'vue-router';

export default {
  data() {
    return {
      basket: [],
    };
  },
  methods: {
    addToBasket(item) {
      let found = false;
      this.basket.forEach((el) => {
        if (el.slug === item.slug) {
          found = true;
          return
        }
      });
      if (found) return;
      this.basket.push(item);
      localStorage.setItem('basket', JSON.stringify(this.basket));
    },
    deleteFromBasket(slug) {
      this.basket = this.basket.filter((el) => el.slug !== slug);
      localStorage.setItem('basket', JSON.stringify(this.basket));
    },
    clearBasket() {
      this.basket = [];
      localStorage.setItem('basket', JSON.stringify([]));
    }
  },
  created() {
    if(this.basket.length == 0 && localStorage.getItem('basket') != null)
      this.basket = [...JSON.parse(localStorage.getItem('basket'))]
  }
}
</script>

<template>
  <div class="container">
    <RouterView :basket="basket" :addToBasket="addToBasket" :deleteFromBasket="deleteFromBasket" :clearBasket="clearBasket"/>
  </div>
</template>

<style scoped>

</style>
