<script>
import Header from '../components/Header.vue';

export default {
    props: ['basket', 'deleteFromBasket', 'addToBasket'],
    components: {
        Header,
    },
};
</script>

<template>
    <Header :basket="basket" :deleteFromBasket="deleteFromBasket" :addToBasket="addToBasket"/>
    <h1>Доставка</h1>
    <p>На сайте не подключена система онлайн-оплаты. При нажатии кнопки «Купить» заказ формируется и сохраняется в базе данных, но оплата не производится. Сайт создан для <a href="https://portfolio-anzore.up.railway.app/" target="_blank">портфолио</a> и не является интернет-магазином — он лишь симулирует его функциональность.
    </p>
</template>

<style scoped>
h1 {
    font-size: 90px;
    font-weight: 400;
    margin-top: 150px;
}

p {
    font-size: 18px;
    margin: 20px 0;
}

p a {
    color: #009872;
}

p a:hover {
    color: #004e3a;
}
</style>