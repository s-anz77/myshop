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
    <h1>Про нас</h1>
    <p>Интернет магазин на Django. На этом сайте есть система добавления товаров в корзину, удаление из неё, а также симуляция оформления заказа.</p>
    <p>Сайт реализован с помощью Django Rest Framework.</p>
    <p>Вся серверная часть построена на Django, а за клиентскую сторону отвечает VueJS.</p>
    <p>Остальные проекты смотрите в моём <a href="https://portfolio-anzore.up.railway.app/" target="_blank">портфолио</a>.</p>
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

@media (max-width:700px) {
    h1 {
        font-size: 60px;
        margin-top: 50px;
    }
}
</style>