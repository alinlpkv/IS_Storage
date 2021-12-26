from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from datetime import datetime

# Таблица поставщиков
class Provider(models.Model):
    provider_name = models.CharField('Название фирмы', max_length=255)
    inn = models.BigIntegerField('ИНН')
    phone = models.CharField('Телефон', max_length=12)
    address = models.CharField('Адрес', max_length=255)

    def __str__(self):
        return self.provider_name

    def get_absolute_url(self):
        return '/providers'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

# Таблица клиентов
class Client(models.Model):
    client_name = models.CharField('Название фирмы', max_length=255)
    inn = models.BigIntegerField('ИНН')
    phone = models.CharField('Телефон', max_length=12)
    address = models.CharField('Адрес', max_length=255)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return '/clients'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Unit(models.Model):
    unit = models.CharField('Единица измерения', max_length=20, primary_key=True)

    def __str__(self):
        return self.unit


    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

class Place(models.Model):
    place_for_store = models.CharField('Место хранения', max_length=50, blank=True, primary_key=True)

    def __str__(self):
        return self.place_for_store

    def get_absolute_url(self):
        return '/place'

    class Meta:
        verbose_name = 'Место хранения'
        verbose_name_plural = 'Места хранения'


# Таблица товаров
class Product(models.Model):
    product_name = models.CharField('Наименование', max_length=255)
    amount = models.PositiveSmallIntegerField('Количество')
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    price_for_one = models.DecimalField('Цена за единицу', max_digits=6, decimal_places=2)
    place_for_store = models.ForeignKey(Place,  on_delete=models.PROTECT)
    valid = models.CharField('Годен до', max_length=10, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    description = models.CharField('Описание', max_length=255, default=' - ', blank=True)
    certificate = models.PositiveSmallIntegerField('№ сертификата')

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return '/products'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

# Таблица для хранения номера Акта
class NumAct(models.Model):
    numact = models.PositiveSmallIntegerField('')

    def __str__(self):
        return str(self.numact)

# Таблица для хранения номера Описи
class NumOpis(models.Model):
    numopis = models.PositiveSmallIntegerField('')

    def __str__(self):
        return str(self.numopis)

# Таблица для заполнения акта
class ProductsInAct(models.Model):
    numact = models.ForeignKey(NumAct,  on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveSmallIntegerField('Количество')

# Таблица для заполнения описи
class ProductsInOPis(models.Model):
    numopis = models.ForeignKey(NumOpis,  on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveSmallIntegerField('Фактическое количество')


#Таблица бланков заказов
class Blank(models.Model):
    NEW = 'new'
    BEGIN = 'begin'
    END = 'end'

    STATUS_CHOICES = (
        ('Новый', 'Новый'),
        ('Начат', 'Начат'),
        ('Закончен', 'Закончен'),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    docfile = models.FileField()
    client = models.ForeignKey(Client,  on_delete=models.PROTECT)
    date = models.CharField('Дата загрузки', max_length=50, blank=True)

    def __str__(self):
        return self.docfile.name

    class Meta:
         verbose_name = 'Бланк'
         verbose_name_plural = 'Бланки заказа'




#Таблица Инвентаризационных описей
class Opis(models.Model):
    docfile = models.FileField()
    date = models.CharField(max_length=255, blank=True)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    numopis = models.ForeignKey(NumOpis, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Опись'
        verbose_name_plural = 'Описи'

#Таблица Актов приема-передач
class ActDoc(models.Model):
    docfile = models.FileField()
    date = models.CharField(max_length=255, blank=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    numact = models.ForeignKey(NumAct, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Акт приема-передачи'
        verbose_name_plural = 'Акты приема-передачи'


















