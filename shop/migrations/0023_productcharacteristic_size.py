# Generated by Django 4.0.6 on 2022-07-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_typecharacteristic_productcharacteristic_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcharacteristic',
            name='size',
            field=models.CharField(max_length=64, null=True, verbose_name='Величина (мм, см и.т.п)'),
        ),
    ]
