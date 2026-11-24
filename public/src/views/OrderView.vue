<script>
import Header from '../components/Header.vue';
import OrderForm from '../components/OrderForm.vue';

export default {
    props: ['basket', 'addToBasket', 'deleteFromBasket'],
    components: {
        Header,
        OrderForm,
    },
};
</script>
    
<template>
    <Header :basket="basket" :addToBasket="addToBasket" :deleteFromBasket="deleteFromBasket"/>
    <OrderForm :basket="basket" :deleteFromBasket="deleteFromBasket"/>
</template>
