# Generated by Django 3.2.5 on 2024-08-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20240710_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='happymail',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]