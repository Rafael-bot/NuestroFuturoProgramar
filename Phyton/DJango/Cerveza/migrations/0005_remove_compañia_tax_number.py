# Generated by Django 3.0.6 on 2020-06-08 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cerveza', '0004_auto_20200608_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compañia',
            name='tax_number',
        ),
    ]
