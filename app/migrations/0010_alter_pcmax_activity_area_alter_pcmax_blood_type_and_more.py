# Generated by Django 5.1 on 2024-09-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_happymail_second_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcmax',
            name='activity_area',
            field=models.CharField(blank=True, choices=[('東京都', '東京都')], max_length=5, null=True, verbose_name='活動地域'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB'), ('秘密', '秘密')], max_length=5, null=True, verbose_name='血液型'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='body_shape',
            field=models.CharField(blank=True, choices=[('普通', '普通'), ('未設定', '未設定'), ('スリム', 'スリム'), ('やや細め', 'やや細め'), ('グラマー', 'グラマー'), ('ややぽっちゃり', 'ややぽっちゃり'), ('太め', '太め')], max_length=20, null=True, verbose_name='体重'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='condition_message',
            field=models.TextField(blank=True, null=True, verbose_name='アドレス内1stメール'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='date_of_birth',
            field=models.IntegerField(blank=True, null=True, verbose_name='誕生日'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='height',
            field=models.IntegerField(blank=True, null=True, verbose_name='身長'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='mail_img',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='画像送付'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='second_message',
            field=models.TextField(blank=True, null=True, verbose_name='2stメール'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='self_promotion',
            field=models.TextField(blank=True, null=True, verbose_name='自己紹介'),
        ),
    ]