# Generated by Django 3.2.8 on 2021-12-20 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, verbose_name='Название фирмы')),
                ('inn', models.BigIntegerField(verbose_name='ИНН')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='NumAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True,  primary_key=True, serialize=False, verbose_name='ID')),
                ('numact', models.PositiveSmallIntegerField(unique=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='NumOpis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numopis', models.PositiveSmallIntegerField(unique=True,  verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_for_store', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Место хранения')),
            ],
            options={
                'verbose_name': 'Место хранения',
                'verbose_name_plural': 'Места хранения',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Количество')),
                ('price_for_one', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена за единицу')),
                ('valid', models.CharField(blank=True, max_length=10, verbose_name='Годен до')),
                ('description', models.CharField(blank=True, default=' - ', max_length=255, verbose_name='Описание')),
                ('certificate', models.CharField(verbose_name='№ сертификата', max_length=30)),
                ('place_for_store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.place')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=255, verbose_name='Название фирмы')),
                ('inn', models.BigIntegerField(verbose_name='ИНН')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='ProductsInOPis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Фактическое количество')),
                ('numopis', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.numopis')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsInAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Количество')),
                ('numact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.numact')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.provider'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.unit'),
        ),
        migrations.CreateModel(
            name='Opis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='')),
                ('date', models.CharField(blank=True, max_length=255)),
                ('numopis', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.numopis')),
            ],
            options={
                'verbose_name': 'Опись',
                'verbose_name_plural': 'Описи',
            },
        ),
        migrations.CreateModel(
            name='Blank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Новый', 'Новый'), ('Начат', 'Начат'), ('Закончен', 'Закончен')], max_length=10)),
                ('docfile', models.FileField(upload_to='')),
                ('date', models.CharField(blank=True, max_length=50, verbose_name='Дата загрузки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.client')),
            ],
            options={
                'verbose_name': 'Бланк',
                'verbose_name_plural': 'Бланки заказа',
            },
        ),
        migrations.CreateModel(
            name='ActDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='')),
                ('date', models.CharField(blank=True, max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.client')),
                ('numact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.numact')),
            ],
            options={
                'verbose_name': 'Акт приема-передачи',
                'verbose_name_plural': 'Акты приема-передачи',
            },
        ),
    ]
