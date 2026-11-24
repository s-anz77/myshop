from django.db import models

class Item(models.Model):
    slug = models.SlugField('Уникальное название', unique=True)
    title = models.CharField('Название товара', max_length=100)
    image = models.CharField('Фото товара', max_length=200)
    description = models.TextField('Описание товара', blank=True)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

class Order(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    items = models.TextField('Товары')
    total = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Заказ от {self.name} {self.surname} ({self.phone}) на ${self.total}'