<script>
import axios from 'axios';

export default {
    props: ['basket', 'deleteFromBasket', "clearBasket"],
    data() {
        return {
            error: '',
            name: '',
            surname: '',
            email: '',
            phone: '',
        };
    },
    computed: {
        getSumma() {
            return this.basket.reduce((total, next) => total + parseFloat(next.price), 0);
        }
    },
    methods: {
        sendData() {
            if (this.basket.length == 0 || this.getSumma == 0) {
                this.error = 'Ваша корзина пуста';
                return;
            }
            else if (this.name == '' || this.surname == '' || this.email == '' || this.phone == '') {
                this.error = 'Заполните все поля';
                return;
            }
            else
                this.error = '';

                const orderData = {
                    name: this.name,
                    surname: this.surname,
                    email: this.email,
                    phone: this.phone,
                    items: JSON.stringify(this.basket),
                    total: this.getSumma
                };

                axios.post('https://anzore-shop-api.up.railway.app/api/order/', orderData)
                    .then(response => {
                        this.error = response.data.result;
                        if (response.data.result === "Заказ успешно оформлен!") {
                            this.clearBasket();
                            this.name = '';
                            this.surname = '';
                            this.email = '';
                            this.phone = '';
                        }
                    }
            );
        }
    }
}
</script>

<template>
    <div>
        <h1>Оформление заказа</h1>
        <div class="data">
            <div class="basket" v-if="basket.length > 0">
                <div class="item" v-for="el in basket" :key="el.slug">
                    <img :src="'/img/' + el.image" :alt="el.title">
                    <h3>{{ el.title }}</h3>
                    <span>{{ el.price }}$</span>
                    <button @click="deleteFromBasket(el.slug)">Удалить</button>
                </div>
                <span>Итого: ${{ getSumma }}</span>
            </div>
            <div v-else>
                <h2>Ваша корзина пуста</h2>
            </div>
            <form>
                <p class="error">{{ error }}</p>
                <input type="text" v-model="name" placeholder="Ваше имя">
                <input type="text" v-model="surname" placeholder="Ваша фамилия">
                <input type="email" v-model="email" placeholder="Email">
                <input type="phone" v-model="phone" placeholder="Телефон">
                <button type="button" @click="sendData">Купить</button>
            </form>
        </div>
    </div>
</template>

<style scoped>
.data {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 50px 0;
}

.data > div {
    width: 40%;
}

h1 {
    margin-top: 150px;
    font-weight: 400;
    font-size: 90px;
    text-align: center;
}

h2 {
    text-align: center;
}

.item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.item img {
    width: 60px;
}
.item h3 {
    color: #52585c;
    font-size: 15px;
    text-align: center;
}
.item span {
    font-weight: 600;
    color: #323232;
}

.item button, form button {
    border: 0;
    background: rgb(186, 43, 43);
    border-radius: 5px;
    padding: 7px 12px;
    cursor: pointer;
    color: #fff;
}

.item button:hover {
    background: rgb(133, 28, 28);
}

.items > span {
    font-weight: 600;
    color: #206E5B;
}

form input {
    width: 300px;
    padding: 10px 15px;
    border: 1.5px solid #575d61;
    border-radius: 2px;
    background: #81898e;
    margin-bottom: 20px;
    display: block;
    color: #fff;
    outline: none;
    font-size: 15px;
}

form input::placeholder {
    color: rgba(64, 64, 64, 0.531);
}

form input:focus {
    border-color: #242424;
}

form button {
    background: #206E5B;
}

form button:hover {
    background: #134438;
}

.error {
    margin-bottom: 10px;
    color: rgb(181, 46, 46);
}

@media (max-width:1050px) {
    .data {
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
        margin: 50px 0;
        gap: 50px;
    }

    .data > div {
        width: 80%;
    }

    h1 {
        margin-top: 50px;
        font-weight: 400;
        font-size: 70px;
    }
}

@media (max-width:560px) {
    h1 {
        font-size: 60px;
    }
}

@media (max-width:460px) {
    h1 {
        font-size: 50px;
    }
}

@media (max-width:380px) {
    .data > div {
        width: 90%;
    }

    h1 {
        font-size: 40px;
    }

    form input {
        width: 250px;
    }
}

</style>