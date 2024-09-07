from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import timedelta
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Registration_subscribe_date = models.DateField(verbose_name="課金日", null=True, blank=True)
    lifted_account_number = models.BooleanField(default=False, verbose_name="アカウント数制限解除(16)")
    gmail_account = models.EmailField(null=True, blank=True, verbose_name="Gmailアドレス")
    gmail_account_password = models.CharField(max_length=30, blank=True, null=True, verbose_name="Gmailアプリパスワード")
    check_mail_happymail = models.BooleanField(default=False, verbose_name="ハッピー新着チェック")
    
    
    
    # このコードをDjangoの定期的なタスクスケジューラー
    # （例えばCeleryやDjango Q）を使用して、
    # 定期的に全てのUserProfileをチェックして、
    # is_activeフィールドを更新する。
    def check_and_update_is_active(self):
        """日付から1ヶ月経ったらis_activeをFalseにする"""
        if self.some_date and (self.some_date + timedelta(days=30)) < timezone.now().date():
            self.user.is_active = False
            self.save()

    def __str__(self):
        return self.user.username

class Happymail(models.Model):
  id = models.BigAutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=30, blank=True, null=True, verbose_name="名前")
  login_id = models.CharField(max_length=30, blank=True, null=True, verbose_name="ログインID")
  password = models.CharField(max_length=30, blank=True, null=True, verbose_name="パスワード")
  fst_message = models.TextField(blank=True, null=True, verbose_name="1stメール")
  return_foot_message = models.TextField(blank=True, null=True, verbose_name="足跡返し")
  conditions_message = models.TextField(blank=True, null=True, verbose_name="2stメール")
  post_title = models.CharField(max_length=20,blank=True, null=True, verbose_name="掲示板タイトル")
  post_contents = models.TextField(blank=True, null=True, verbose_name="掲示板内容文")
  is_active = models.BooleanField(default=True, verbose_name="アクティブ")
  chara_image = models.ImageField(upload_to='chara_images/', null=True, blank=True, verbose_name="送付画像")
  fst_message = models.TextField(blank=True, null=True, verbose_name="1stメール")
  second_message = models.TextField(blank=True, null=True, verbose_name="2stメール")
  def __str__(self):
    return self.name  # ここで表示したいフィールドを選択します

  class Meta:
    managed = True
    db_table = 'happymail'
    verbose_name = "ハッピーメール"
    verbose_name_plural = "ハッピーメール"

class Pcmax(models.Model):
  body_shape_list = [
    ("普通", "普通"),
    ("未設定","未設定"),
    ("スリム", "スリム"), 
    ("やや細め","やや細め"), 
    ("グラマー", "グラマー"), 
    ("ややぽっちゃり", "ややぽっちゃり"), 
    ("太め","太め"),
    ]
  blood_type_list = [("A","A"), ("B","B"), ("O","O"), ( "AB", "AB"), ("秘密","秘密")]
  activity_area_list = [
    ("東京都", "東京都")
    # "神奈川県", "埼玉県", "千葉県"
    ]
  detail_activity_area_tokyo = [
    ("千代田区","千代田区"), ( "中央区", "中央区"), ("港区","港区"), ( "新宿区", "新宿区"), ( "文京区", "文京区"),
    ("台東区","台東区"), ("品川区","品川区"), ( "目黒区", "目黒区"), ( "大田区", "大田区"), ( "世田谷区", "世田谷区"),
    ( "渋谷区", "渋谷区"), (  "中野区",  "中野区"), ( "杉並区" "杉並区"), ("豊島区","豊島区"), ( "北区", "北区"),
    ("荒川区","荒川区"), ( "板橋区", "板橋区"), ("練馬区","練馬区"), ("武蔵野市",  "武蔵野市"),   
  ]
  freetime_list = [
    ("不規則で決まってない","不規則で決まってない"), ("秘密","秘密"), ("平日の昼間","平日の昼間"), ("平日の夜","平日の夜")
      ]
  car_ownership_list = [("ない", "ない")]
  smoking_list = [("吸わない(喫煙は気にしない)", "吸わない(喫煙は気にしない)")]
  ecchiness_level_list = [
    ("積極的で好奇心旺盛","積極的で好奇心旺盛"), ("普通だけど刺激が欲しい","普通だけど刺激が欲しい"), ("普通だけど相性は大事","普通だけど相性は大事")
      ]
  sake_list = [
    ("たしなむ程度","たしなむ程度"), ("飲めない","飲めない"), ("飲めないが場は好き","飲めないが場は好き")
      ]
  process_before_meeting_list =[
    ("まずは会ってみたい","まずは会ってみたい"), ("気が合いそうなら会ってみたい","気が合いそうなら会ってみたい")
     ]
  first_date_cost_list = [
    ("相手と相談して決める", "相手と相談して決める"),
    ]

  name = models.CharField(max_length=30, blank=True, null=True, verbose_name="名前")
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)  
  login_id = models.CharField(max_length=30, blank=True, null=True, verbose_name="ログインID")
  password = models.CharField(max_length=30, blank=True, null=True, verbose_name="パスワード")
  fst_mail = models.TextField( blank=True, null=True, verbose_name="1stメール")
  mail_img = models.CharField(max_length=100, blank=True, null=True)
  post_title = models.CharField(max_length=30, blank=True, null=True, verbose_name="掲示板タイトル")
  post_content = models.TextField( blank=True, null=True, verbose_name="掲示板内容文")
  second_message = models.TextField(blank=True, null=True)
  condition_message = models.TextField(blank=True, null=True)
  return_foot_message = models.TextField(blank=True, null=True, verbose_name="足跡返し")
  date_of_birth = models.IntegerField(blank=True, null=True)
  self_promotion = models.TextField(blank=True, null=True)
  height = models.IntegerField(blank=True, null=True)
  body_shape = models.CharField(max_length=20, choices=body_shape_list, null=True, blank=True)
  blood_type = models.CharField(max_length=5, choices=blood_type_list, null=True, blank=True)
  activity_area = models.CharField(max_length=5, choices=activity_area_list, null=True, blank=True)
  detail_activity_area = models.CharField(max_length=10, blank=True, null=True)
  profession = models.TextField(blank=True, null=True)
  freetime = models.CharField(max_length=20, choices=freetime_list, null=True, blank=True)
  car_ownership = models.CharField(max_length=20, choices=car_ownership_list, null=True, blank=True)
  smoking = models.CharField(max_length=20, choices=smoking_list, null=True, blank=True)
  ecchiness_level = models.CharField(max_length=20, choices=ecchiness_level_list, null=True, blank=True)
  sake = models.CharField(max_length=20, choices=sake_list, null=True, blank=True)
  process_before_meeting = models.CharField(max_length=20, choices=process_before_meeting_list, null=True, blank=True)
  first_date_cost = models.CharField(max_length=20, choices=first_date_cost_list, null=True, blank=True)
  is_active = models.BooleanField(default=True, verbose_name="アクティブ")
  
  def __str__(self):
    return self.name  # ここで表示したいフィールドを選択します
  
  class Meta:
    managed = True
    db_table = 'pcmax'
    verbose_name = "PCMAX"
    verbose_name_plural = "PCMAX"