# Generated by Django 3.0.6 on 2020-06-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cerveza', '0003_auto_20200608_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compañia',
            name='tax_number',
            field=models.IntegerField(auto_created=True, max_length=5, unique=True, verbose_name='Tax_Number'),
        ),
    ]
