<template>
    <div class="wrapper">
        <img src="/img/main-image.svg" alt="">
        <div>
            <img src="/img/asterics.svg" alt="">
            <h1>Shop</h1>
            <h2>online</h2>
            <h3>now</h3>
            <p>Приветствую Вас на одном из моих проектов.</p>
            <p><a href="/about">Подробнее</a></p>
            <button><a href="/items">Начать покупки</a></button>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.wrapper {
    display: flex;
    justify-content: start;
    align-items: center;
    margin: 150px 0;
    gap: 20%;
}

.wrapper > div {
    display: flex;
    flex-direction: column;
    align-items: start;
    color: #373845;
}

.wrapper > div h1 {
    font-weight: 400;
    font-size: 90px;
}

.wrapper > div h2, .wrapper > div h3 {
    font-weight: 400;
    font-size: 70px;
}

.wrapper > div h3 {color: #5CDDBC;}

.wrapper > div p {
    font-size: 18px;
    margin: 20px 0;
}

.wrapper > div button {
    font-weight: 600;
    font-size: 18px;
    color: #2F323A;
    background: #5CDDBC;
    border-radius: 25px;
    border: 0;
    padding: 15px 25px;
    cursor: pointer;
}

.wrapper > div button:hover {
    transform: translateY(-5px);
}

.wrapper > img {
    max-width: 40%;
    height: auto;
}

.wrapper > div img {
    height: 50px;
    width: auto;
}

p a {
    color: #009872;
}

p a:hover {
    color: #004e3a;
}

@media (max-width: 1265px) {
    .wrapper {
        justify-content: space-between;
        gap: 0;
        flex-wrap: wrap;
    }

    .wrapper > div {
        zoom: 0.8;
    }
}

@media (max-width: 900px) {
    .wrapper > div {
        zoom: 0.6;
    }
}

@media (max-width: 600px) {
    .wrapper > div {
        zoom: 0.6;
        margin-top: 50px;
    }

    .wrapper {
        flex-direction: column;
        justify-content: start;
        align-items: center;
        margin: 50px 0;
        gap: 0;
    }

    .wrapper > img {
        max-width: 60%;
        height: auto;
    }
}

@media (max-width: 460px) {
    .wrapper > img {
        max-width: 80%;
        height: auto;
    }
}
</style>