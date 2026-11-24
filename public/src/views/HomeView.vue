<script>
import Header from '../components/Header.vue';
import MainSection from '../components/MainSection.vue';

export default {
    props: ['basket', 'addToBasket', 'deleteFromBasket'],
    components: {
        Header,
        MainSection,
    },
};
</script>

<template>
    <Header :basket="basket" :addToBasket="addToBasket" :deleteFromBasket="deleteFromBasket"/>
    <MainSection />
</template>
