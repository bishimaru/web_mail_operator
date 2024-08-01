# Generated by Django 3.2.5 on 2024-07-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240710_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcmax',
            name='activity_area',
            field=models.CharField(blank=True, choices=[('東京都', '東京都')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB'), ('秘密', '秘密')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='body_shape',
            field=models.CharField(blank=True, choices=[('普通', '普通'), ('未設定', '未設定'), ('スリム', 'スリム'), ('やや細め', 'やや細め'), ('グラマー', 'グラマー'), ('ややぽっちゃり', 'ややぽっちゃり'), ('太め', '太め')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='car_ownership',
            field=models.CharField(blank=True, choices=[('ない', 'ない')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='ecchiness_level',
            field=models.CharField(blank=True, choices=[('積極的で好奇心旺盛', '積極的で好奇心旺盛'), ('普通だけど刺激が欲しい', '普通だけど刺激が欲しい'), ('普通だけど相性は大事', '普通だけど相性は大事')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='first_date_cost',
            field=models.CharField(blank=True, choices=[('相手と相談して決める', '相手と相談して決める')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='freetime',
            field=models.CharField(blank=True, choices=[('不規則で決まってない', '不規則で決まってない'), ('秘密', '秘密'), ('平日の昼間', '平日の昼間'), ('平日の夜', '平日の夜')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='process_before_meeting',
            field=models.CharField(blank=True, choices=[('まずは会ってみたい', 'まずは会ってみたい'), ('気が合いそうなら会ってみたい', '気が合いそうなら会ってみたい')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='sake',
            field=models.CharField(blank=True, choices=[('たしなむ程度', 'たしなむ程度'), ('飲めない', '飲めない'), ('飲めないが場は好き', '飲めないが場は好き')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='smoking',
            field=models.CharField(blank=True, choices=[('吸わない(喫煙は気にしない)', '吸わない(喫煙は気にしない)')], max_length=20, null=True),
        ),
    ]
