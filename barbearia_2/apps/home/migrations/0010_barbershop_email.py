# Generated by Django 3.2.6 on 2023-01-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20230116_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='email',
            field=models.EmailField(default='pedrohamorim2011@hotmail.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
