# Generated by Django 2.0 on 2018-01-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20180111_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitation',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
