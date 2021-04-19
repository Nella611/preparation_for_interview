from django.db import models


class GoodItem(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_created=True,
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        verbose_name='Изменено',
        auto_created=True,
        auto_now_add=True
    )

    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена',
        default=0
    )

    vendor = models.CharField(
        verbose_name='Поставщик',
        max_length=255
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'

