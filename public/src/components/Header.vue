<script>
export default {
    name: 'Header',
    props: ['basket', 'addToBasket', "deleteFromBasket"],
    data() {
        return {
            showBasket: false,
        };
    },
};
</script>

<template>
    <header>
        <img src="/img/logo.svg" alt="">
        <ul class="wideNavBar">
            <li><RouterLink to="/" active-class="active">Главная</RouterLink></li>
            <li><RouterLink to="/items" active-class="active">Товары</RouterLink></li>
            <li><RouterLink to="/shipping" active-class="active">Доставка</RouterLink></li>
            <li><RouterLink to="/about" active-class="active">Про нас</RouterLink></li>
            <li><img src="/img/purchase.svg" alt="" @click="showBasket = !showBasket"></li>
        </ul>
        <ul class="hiddenNavBar">
            <li><img src="/img/purchase.svg" alt="" @click="showBasket = !showBasket"></li>
        </ul>
        <div class="basket" v-if="showBasket">
            <div class="box"></div>
            <h3 v-if="basket.length == 0">Товаров нет</h3>
            <div class="items" v-else>
                <div class="item" v-for="el in basket" :key="el.slug">
                    <img :src="'/img/' + el.image" :alt="el.title">
                    <h3>{{ el.title }}</h3>
                    <span>{{ el.price }}$</span>
                    <img class='remove-from-basket' src="/img/remove-from-basket.svg" alt="Убрать из корзины" @click="deleteFromBasket(el.slug)"/>
                </div>
                <RouterLink to="/order"><button>Перейти к оплате</button></RouterLink>
            </div>
        </div>
    </header>
    <ul class="belowNavBar">
            <li><RouterLink to="/" active-class="active">Главная</RouterLink></li>
            <li><RouterLink to="/items" active-class="active">Товары</RouterLink></li>
            <li><RouterLink to="/shipping" active-class="active">Доставка</RouterLink></li>
            <li><RouterLink to="/about" active-class="active">Про нас</RouterLink></li>
        </ul>
</template>

<style scoped>
.basket {
    position: absolute;
    top: 50px;
    right: 0;
    padding: 20px;
    background: #B2BAC1;
    border-radius: 2px;
    z-index: 100;
    box-shadow: 0px 2px 5px 0px rgba(128,128,128,0.4);
}

.basket .box {
    background: #B2BAC1;
    position: absolute;
    top: -7px;
    right: 11px;
    width: 15px;
    height: 15px;
    transform: rotate(45deg);
}

.basket h3 {color: #616569}

.basket .item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    gap: 10px;
}

.basket .item img {
    width: 60px;
}

.basket .item h3 {
    color: #52585c;
    font-size: 15px;
    text-align: center;
}

.basket .item span {
    font-weight: 600;
    color: #323232;
    margin-left: auto;
}

.basket button {
    cursor: pointer;
    width: 100%;
    border: 0;
    height: 50px;
    background: #919191;
    color: #52585c;
    font-weight: 600;
    font-size: 14px;
    transition: all 500ms ease;
}

.basket button:hover {
    background: #757575;
    color: #2f3336;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 50px;
    position: relative;
    width: 100%;
}

ul {
    display: flex;
    gap: 25px;
    list-style: none;
    align-items: center;
}

ul li a.active {
    font-weight: bold;
    padding: 5px 15px;
    background-color: #B2BAC1;
    border-radius: 20px;
}

ul li a.active:hover {
    color: #fff;
    background: #616569;
}

.remove-from-basket {
    transform: scale(0.5);
    cursor: pointer;
    transition: transform 500ms ease;
}

.remove-from-basket:hover {
    transform: scale(0.7);
}

.hiddenNavBar {
    display: none;
}

.belowNavBar {
    display: none;
}

@media (max-width: 720px) {
    .wideNavBar {
        display: none;
    }

    .hiddenNavBar {
        display: block;
    }

    .belowNavBar {
        display: flex;
        margin-top: 10px;
        justify-content: space-between;
    }
}

@media (max-width: 460px) {
    .belowNavBar {
        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
        margin-top: 50px;
        justify-content: center;
    }

    .belowNavBar > li {
        flex: 0 0 50%;
        box-sizing: border-box;
    }
}
</style>