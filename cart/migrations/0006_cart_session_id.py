# Generated by Django 3.2.9 on 2021-12-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_cart_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
