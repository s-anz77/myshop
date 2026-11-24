<script>
import axios from 'axios';

export default {
    props: ['item'],
    data() {
        return {
            title: this.item.title,
            image: this.item.image,
            description: this.item.description,
            price: this.item.price,
            error: '',
        };
    },

    methods: {
        editData(slug) {
            if (this.title == '' || this.image == '' || this.description == '' || this.price == '')
            this.error = 'Заполните все поля';
            else {
            this.error = '';
            const newData = {
                slug: slug,
                title: this.title,
                description: this.description,
                price: this.price,
                };

                axios.put(`https://anzore-shop-api.up.railway.app/api/edit/${slug}/`, newData)
                    .then(response => console.log(response.data.result));
            }
        }
    }
}
</script>

<template>
    <div>
        <form>
            <p class="error">{{ error }}</p>
            <input type="text" v-model="title" placeholder="Наименование">
            <input type="text" v-model="description" placeholder="Описание">
            <input type="number" v-model="price" placeholder="Цена">
            <button class='editBut' type="submit" @click="editData(this.item.slug)">Обновить</button>
        </form>
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

form button.editBut {
    border: 0;
    background: rgb(43, 186, 114);
    border-radius: 5px;
    padding: 7px 12px;
    cursor: pointer;
    color: #fff;
}

form button.editBut:hover {
    background: rgb(22, 94, 58);
}
</style>