from django.db import models


class FeedBackModel(models.Model):
    name = models.CharField('Имя',max_length=30)
    last_name = models.CharField('Фамилия',max_length=30)
    subject = models.CharField('Тема',max_length=50)
    text = models.TextField('Сообщение')
    date = models.DateTimeField('Дата заявки',auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'