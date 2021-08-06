from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Название категории', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField('Название товара', max_length=50)
    description = models.TextField('Описание товара')
    image = models.ImageField('Фото', upload_to='images/')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# Имя телефон почта комментарий

class Zakaz(models.Model):
    product = models.CharField('Название товара',max_length=50)
    name = models.CharField('Ваше имя', max_length=30)
    phone = models.IntegerField('Номер телефона', max_length=25)
    email = models.EmailField(null=True, blank=True)
    comment = models.CharField('Ваш комментарий',max_length=200,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



