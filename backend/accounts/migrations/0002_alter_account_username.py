# Generated by Django 3.2.9 on 2021-12-01 08:36

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(error_messages={'unique': 'Username already exists'}, help_text='Username is required. Fewer than 256 character', max_length=255, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
