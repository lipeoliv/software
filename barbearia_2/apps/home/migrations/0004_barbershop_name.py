# Generated by Django 3.2.6 on 2023-01-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230113_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='name',
            field=models.CharField(default='Barbearia Dom Barbudo', max_length=255, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]