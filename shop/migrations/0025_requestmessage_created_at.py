# Generated by Django 4.0.6 on 2022-07-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_requestmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания заявки'),
        ),
    ]