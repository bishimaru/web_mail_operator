# Generated by Django 5.1 on 2024-10-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_happymail_activity_area_happymail_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='happymail',
            name='brothers_and_sisters',
            field=models.CharField(blank=True, choices=[('長女', '長女'), ('間っ子', '間っ子'), ('末っ子', '末っ子'), ('一人っ子', '一人っ子'), ('その他', 'その他')], max_length=20, null=True, verbose_name='兄弟姉妹'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='car_ownership',
            field=models.CharField(blank=True, choices=[('ない', 'ない'), ('ナイショ', 'ナイショ')], max_length=20, null=True, verbose_name='クルマ'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='date_expenses',
            field=models.CharField(blank=True, choices=[('男性が全て払う', '男性が全て払う'), ('男性が多めに払う', '男性が多めに払う'), ('割り勘', '割り勘'), ('持っている人が払う', '持っている人が払う'), ('相手と相談して決める', '相手と相談して決める')], max_length=20, null=True, verbose_name='初回デート費用'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='education',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='学歴'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='having_children',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='子ども'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='holiday',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='休日'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='intention_to_marry',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='結婚に対する意思'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='job',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='職業'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='relationship_status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='交際ステータス'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='roommate',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='同居人'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='sake',
            field=models.CharField(blank=True, choices=[('たしなむ程度', 'たしなむ程度'), ('飲まない', '飲まない'), ('ときどき飲む', 'ときどき飲む'), ('ナイショ', 'ナイショ')], max_length=20, null=True, verbose_name='お酒'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='smoking',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='たばこ'),
        ),
        migrations.AddField(
            model_name='happymail',
            name='until_we_met',
            field=models.CharField(blank=True, choices=[('まずは会いたい', 'まずは会いたい'), ('気が合えば会いたい', '気が合えば会いたい')], max_length=20, null=True, verbose_name='出会うまでの希望'),
        ),
    ]
