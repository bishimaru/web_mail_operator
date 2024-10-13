# Generated by Django 5.1 on 2024-10-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_userprofile_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='happymail',
            name='memo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='メモ'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='memo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='メモ'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='car_ownership',
            field=models.CharField(blank=True, choices=[('ない', 'ない')], max_length=20, null=True, verbose_name='車の所有'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='ecchiness_level',
            field=models.CharField(blank=True, choices=[('積極的で好奇心旺盛', '積極的で好奇心旺盛'), ('普通だけど刺激が欲しい', '普通だけど刺激が欲しい'), ('普通だけど相性は大事', '普通だけど相性は大事')], max_length=20, null=True, verbose_name='エッチ度'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='first_date_cost',
            field=models.CharField(blank=True, choices=[('相手と相談して決める', '相手と相談して決める')], max_length=20, null=True, verbose_name='初回デート費用'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='freetime',
            field=models.CharField(blank=True, choices=[('不規則で決まってない', '不規則で決まってない'), ('秘密', '秘密'), ('平日の昼間', '平日の昼間'), ('平日の夜', '平日の夜')], max_length=20, null=True, verbose_name='ヒマな時間帯'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='process_before_meeting',
            field=models.CharField(blank=True, choices=[('まずは会ってみたい', 'まずは会ってみたい'), ('気が合いそうなら会ってみたい', '気が合いそうなら会ってみたい')], max_length=20, null=True, verbose_name='会うまでのプロセス'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='sake',
            field=models.CharField(blank=True, choices=[('たしなむ程度', 'たしなむ程度'), ('飲めない', '飲めない'), ('飲めないが場は好き', '飲めないが場は好き')], max_length=20, null=True, verbose_name='お酒'),
        ),
        migrations.AlterField(
            model_name='pcmax',
            name='smoking',
            field=models.CharField(blank=True, choices=[('吸わない(喫煙は気にしない)', '吸わない(喫煙は気にしない)')], max_length=20, null=True, verbose_name='喫煙'),
        ),
    ]