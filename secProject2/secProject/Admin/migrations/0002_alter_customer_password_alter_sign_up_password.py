# Generated by Django 4.0.3 on 2022-06-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='password',
            field=models.IntegerField(),
        ),
    ]
