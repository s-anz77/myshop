<template>
    <div class="items">
        <div class="item" v-for="item in items" :key="item.id">
            <img :src="'/img/' + item.image" :alt="item.title"/>
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
            <div class="bottom">
                <span class="price">{{ item.price }} ₽</span>
                <img v-if="isInBasket(item.slug)" src="/img/remove-from-basket.svg" alt="Убрать из корзины" @click="deleteFromBasket(item.slug)"/>
                <img v-else src="/img/add-to-basket.svg" alt="Добавить в корзину" @click="addToBasket(item)"/>
            </div>
            <div>
                <button class="editBut" @click="isEditingToggle(item.slug)">Редактировать</button>
                <div v-if="this.editingSlug === item.slug">
                    <OrderEditForm :item="item" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import OrderEditForm from './OrderEditForm.vue'

export default {
    components: {
        OrderEditForm,
    },
    props: ['addToBasket', 'basket', "deleteFromBasket"],
    data() {
        return {
            items: [],
            editingSlug: null,
        };
    },
    methods: {
        isEditingToggle(slug) {
            this.editingSlug = this.editingSlug === slug ? null : slug;
        },
        isInBasket(slug) {
            return this.basket.some(item => item.slug === slug);
        },
    },
    async mounted() {
        try {
            const res = await axios.get('https://anzore-shop-api.up.railway.app/api/items/?format=json');
            this.items = res.data;
        } catch (error) {
            console.log('Ошибка при получении данных:', error);
        }
    },
};
</script>

<style scoped>
.items {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.items .item {
    margin-bottom: 100px;
    width: 350px;
    padding: 15px;
    background: #F4F4F4;
}

.items .item img:first-child {width: 100%;}

.items .item h3 {
    margin: 12px 0;
    font-size: 20px;
}

.items .item p {
    margin: 10px 0;
    font-size: 15px;
    width: 90%;
}

.items .item .bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.items .item .bottom span {
    font-weight: 600;
    color: #216E5B;
}

.items .item .bottom img {
    cursor: pointer;
    transition: transform 500ms ease;
}

.items .item .bottom img:hover {
    transform: scale(1.3);
}

.editBut {
    border: 0;
    background: rgb(43, 186, 114);
    border-radius: 5px;
    padding: 7px 12px;
    cursor: pointer;
    color: #fff;
}

.editBut:hover {
    background: rgb(22, 94, 58);
}

@media (max-width: 1000px) {
    .items {
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
    }

    .items .item {
        margin-bottom: 30px;
    }
}

@media (max-width:480px) {
    .items .item {
        zoom: 0.7;
    }
}
</style>