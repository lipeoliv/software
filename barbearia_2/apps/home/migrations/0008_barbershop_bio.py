# Generated by Django 3.2.6 on 2023-01-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_barbershopimage_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='bio',
            field=models.TextField(default='Bio da barbearia', verbose_name='Bio'),
            preserve_default=False,
        ),
    ]