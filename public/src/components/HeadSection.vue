<template>
    <div class="wrapper">
        <div class="leftPart">
            <h1>Все товары</h1>
            <h2>Лучшие товары для Вас</h2>
        </div>
        <div>
            <img src="/img/main-image.svg" alt="">
        </div>
    </div>
</template>

<style scoped>
.wrapper {
    background: #5CDDBC;
    width: 104%;
    position: relative;
    right: 13%;
    display: flex;
    padding: 0 12%;
    justify-content: space-between;
    align-items: center;
    height: 240px;
    color: #216F5B;
    margin: 60px 0;
}

.wrapper h1 {
    font-size: 70px;
}

.wrapper h2 {
    font-size: 30px;
    font-weight: 400;
    margin-top: 15px;
}

.wrapper img {
    height: 230px;
    position: relative;
    top: 8px;
    right: 30px;
}

@media (max-width: 900px) {
    .leftPart {
        zoom: 0.8;
    }

    .wrapper img {
        height: 200px;
        right: 20px;
    }

    .wrapper {
        height: 210px;
    }
}

@media (max-width: 750px) {
    .leftPart {
        zoom: 0.6;
    }

    .wrapper img {
        height: 160px;
        right: 10px;
    }

    .wrapper {
        height: 170px;
    }
}

@media (max-width: 600px) {
    .leftPart {
        zoom: 0.5;
    }

    .wrapper img {
        height: 130px;
        right: 0;
    }

    .wrapper {
        height: 140px;
    }
}

@media (max-width: 500px) {
    .leftPart {
        zoom: 0.4;
    }

    .wrapper img {
        height: 100px;
    }

    .wrapper {
        height: 110px;
    }
}
</style>