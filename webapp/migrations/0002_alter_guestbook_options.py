# Generated by Django 5.0.6 on 2024-07-06 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestbook',
            options={'ordering': ['-date_added'], 'verbose_name': 'Запись в гостевой книге', 'verbose_name_plural': 'Записи в гостевой книге'},
        ),
    ]
