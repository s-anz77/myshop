<script>
import Header from '../components/Header.vue';
import HeadSection from '../components/HeadSection.vue';
import ItemsSection from '../components/ItemsSection.vue';

export default {
    props: ['basket', 'addToBasket', 'deleteFromBasket'],
    components: {
        Header,
        HeadSection,
        ItemsSection,
    },
};
</script>

<template>
    <Header :basket="basket" :addToBasket="addToBasket" :deleteFromBasket="deleteFromBasket"/>
    <HeadSection />
    <ItemsSection :basket="basket" :addToBasket="addToBasket" :deleteFromBasket="deleteFromBasket"/>
</template>
