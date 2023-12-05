# Generated by Django 4.2.7 on 2023-12-03 12:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('+?[0-9]{7,}', 'Incorrect Phone number')], verbose_name='telephone'),
        ),
    ]
