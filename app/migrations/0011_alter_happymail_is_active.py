# Generated by Django 3.2.5 on 2024-08-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_happymail_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happymail',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='アクティブ'),
        ),
    ]