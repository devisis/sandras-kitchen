# Generated by Django 3.2 on 2022-07-25 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20220716_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='limited_integer_Field',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]