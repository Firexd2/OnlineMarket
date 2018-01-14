# Generated by Django 2.0 on 2018-01-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0014_auto_20180111_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processed', 'Обрабатывается'), ('preparation', 'Подготовка к отправке'), ('road', 'В дороге'), ('delivered', 'Доставлен')], default='processed', max_length=30, verbose_name='Статус'),
        ),
    ]