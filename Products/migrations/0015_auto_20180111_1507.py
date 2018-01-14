# Generated by Django 2.0 on 2018-01-11 12:07

import Products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_merge_20180111_0829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageproduct',
            options={'verbose_name': 'Фотографии продукта', 'verbose_name_plural': 'Фотографии продуктов'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_url',
            field=models.CharField(default='', max_length=50, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(help_text='Можно выбрать несколько (Ctrl или выделение)', upload_to=Products.models.directory_path, verbose_name='Файлы'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.Product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.PositiveIntegerField(verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.SettingsProduct', verbose_name='Характеристики'),
        ),
    ]