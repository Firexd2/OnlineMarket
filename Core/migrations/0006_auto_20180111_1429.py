# Generated by Django 2.0 on 2018-01-11 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_remove_visitation_go_pages_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitation',
            options={'verbose_name': 'Посещение', 'verbose_name_plural': 'Посещения'},
        ),
    ]
