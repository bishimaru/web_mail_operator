# Generated by Django 3.2.5 on 2024-07-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20240710_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcmax',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='名前'),
        ),
    ]
