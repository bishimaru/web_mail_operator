# Generated by Django 5.1 on 2024-10-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_userprofile_check_mail_pcmax'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcmax',
            name='annual_income',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('200万円未満', '200万円未満'), ('200万円以上～400万円未満', '200万円以上～400万円未満'), ('400万円以上～600万円未満', '400万円以上～600万円未満'), ('600万円以上～800万円未満', '600万円以上～800万円未満'), ('800万円以上～1000万円未満', '800万円以上～1000万円未満'), ('1000万円以上～1500万円未満', '1000万円以上～1500万円未満'), ('1500万円以上～2000万円未満', '1500万円以上～2000万円未満'), ('2000万円以上', '2000万円以上')], max_length=20, null=True, verbose_name='年収'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='birth_place',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='出身地'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='child',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('絶対に子供が欲しい', '絶対に子供が欲しい'), ('どちらかというと子供が欲しい', 'どちらかというと子供が欲しい'), ('子供は欲しくない', '子供は欲しくない'), ('相手と相談して決めたい', '相手と相談して決めたい'), ('同居中の子供がいる', '同居中の子供がいる'), ('別居中の子供がいる', '別居中の子供がいる'), ('子供だけ欲しい（パートナー不要）', '子供だけ欲しい（パートナー不要）')], max_length=20, null=True, verbose_name='子供'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='education',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('高卒', '高卒'), ('短大/専門学校', '短大/専門学校'), ('大学', '大学'), ('大学院', '大学院'), ('その他', 'その他')], max_length=20, null=True, verbose_name='学歴'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='housework',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('積極的に参加したい', '積極的に参加したい'), ('できれば参加したい', 'できれば参加したい'), ('できれば相手に任せたい', 'できれば相手に任せたい'), ('相手に任せたい', '相手に任せたい'), ('相手と相談して決めたい', '相手と相談して決めたい')], max_length=20, null=True, verbose_name='家事・育児'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='marry',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('すぐにでもしたい', 'すぐにでもしたい'), ('2～3年のうちに', '2～3年のうちに'), ('良い人がいればしたい', '良い人がいればしたい'), ('今のところ結婚は考えていない', '今のところ結婚は考えていない'), ('相手と相談して決めたい', '相手と相談して決めたい'), ('以前結婚していた', '以前結婚していた'), ('未婚だけどパートナーが居る', '未婚だけどパートナーが居る'), ('既婚者です', '既婚者です')], max_length=20, null=True, verbose_name='結婚'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='roommate',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('一人暮らし', '一人暮らし'), ('友達と一緒', '友達と一緒'), ('家族と一緒', '家族と一緒'), ('兄弟姉妹と一緒', '兄弟姉妹と一緒'), ('ペットと一緒', 'ペットと一緒'), ('その他', 'その他')], max_length=20, null=True, verbose_name='同居人'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='sociability',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('大人数が好き', '大人数が好き'), ('小人数が好き', '小人数が好き'), ('ひとりが好き', 'ひとりが好き'), ('すぐに仲良くなる', 'すぐに仲良くなる'), ('徐々に仲良くなる', '徐々に仲良くなる')], max_length=20, null=True, verbose_name='社交性'),
        ),
        migrations.AddField(
            model_name='pcmax',
            name='travel',
            field=models.CharField(blank=True, choices=[('未回答', '未回答'), ('仲良くなってからなら', '仲良くなってからなら'), ('予定が合えば', '予定が合えば'), ('雰囲気で決める', '雰囲気で決める'), ('宿泊は無理', '宿泊は無理'), ('むしろ泊めて欲しい', 'むしろ泊めて欲しい')], max_length=20, null=True, verbose_name='旅行・宿泊'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='ハッピー再投稿、足跡返し'),
        ),
    ]
