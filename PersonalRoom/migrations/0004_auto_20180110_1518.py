# Generated by Django 2.0.1 on 2018-01-10 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalRoom', '0003_auto_20171228_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionaluser',
            options={'verbose_name': 'Дополнительная информация о пользователе', 'verbose_name_plural': 'Дополнительная информация о пользователе'},
        ),
        migrations.AlterModelOptions(
            name='favoritesproducts',
            options={'verbose_name': 'Избранный товар', 'verbose_name_plural': 'Избранные товары'},
        ),
    ]
