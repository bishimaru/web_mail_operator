from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField  # PostgreSQLの場合



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_subscribe_date = models.DateField(verbose_name="課金日", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="アクティブ")
    lifted_account_number = models.BooleanField(default=False, verbose_name="アカウント数制限解除(16)")
    gmail_account = models.EmailField(null=True, blank=True, verbose_name="Gmailアドレス")
    gmail_account_password = models.CharField(max_length=30, blank=True, null=True, verbose_name="Gmailアプリパスワード")
    check_mail_happymail = models.BooleanField(default=False, verbose_name="ハッピー新着チェック")
    recieve_mailaddress = models.EmailField(null=True, blank=True, verbose_name="受信用メールアドレス")
    h_schedule_time = ArrayField(models.CharField(max_length=15), blank=True, null=True, verbose_name="ハッピー予約時間") 
    class Meta:
      managed = True
      verbose_name = "ユーザーオプション"
      verbose_name_plural = "ユーザーオプション"

    def __str__(self):
        return self.user.username

class Happymail(models.Model):
  age_list = [
    ("ナイショ","ナイショ"),
    ("18～19歳", "18～19歳"), 
    ("20代前半", "20代前半"),
    ("20代半ば","20代半ば"), 
    ("20代後半", "20代後半"), 
  ]
  activity_area_list = [
    ("東京都", "東京都")
    # "神奈川県", "埼玉県", "千葉県"
    ]
  blood_type_list = [
    ("指定しない","指定しない"), ("Ａ型","Ａ型"), 
    ("Ｂ型","Ｂ型"), ("Ｏ型","Ｏ型"), ( "ＡＢ型", "ＡＢ型"), 
    ("わからない","わからない"), ("ナイショ","ナイショ")
    ]
  height_list = [
    ("150～154","150～154"), ("155～159","155～159"), 
    ("160～164","160～164"), ("165～169","165～169"), ("ナイショ", "ナイショ")
  ]
  sake_list = [
    ("たしなむ程度","たしなむ程度"), ("飲まない","飲まない"), ("ときどき飲む","ときどき飲む"), ("ナイショ","ナイショ"),
      ]
  car_ownership_list = [("ない", "ない"), ("ナイショ", "ナイショ")]
  brothers_and_sisters_list = [("長女", "長女"), ("間っ子", "間っ子"), ("末っ子", "末っ子"), ("一人っ子", "一人っ子"),  ("その他", "その他"), ]
  until_we_met_list = [("まずは会いたい", "まずは会いたい"), ("気が合えば会いたい", "気が合えば会いたい"), ]
  date_expenses_list = [("男性が全て払う", "男性が全て払う"), ("男性が多めに払う", "男性が多めに払う"), ("割り勘", "割り勘"), ("持っている人が払う", "持っている人が払う"),  ("相手と相談して決める", "相手と相談して決める"), ]
  
  
  id = models.BigAutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=30, blank=True, null=True, verbose_name="名前")
  login_id = models.CharField(max_length=30, blank=True, null=True, verbose_name="ログインID")
  password = models.CharField(max_length=30, blank=True, null=True, verbose_name="パスワード")
  fst_message = models.TextField(blank=True, null=True, verbose_name="1stメール")
  return_foot_message = models.TextField(blank=True, null=True, verbose_name="足跡返し")
  conditions_message = models.TextField(blank=True, null=True, verbose_name="2stメール")
  post_title = models.CharField(max_length=30,blank=True, null=True, verbose_name="掲示板タイトル")
  post_contents = models.TextField(blank=True, null=True, verbose_name="掲示板内容文")
  is_active = models.BooleanField(default=True, verbose_name="アクティブ")
  chara_image = models.ImageField(upload_to='chara_images/', null=True, blank=True, verbose_name="送付画像")
  fst_message = models.TextField(blank=True, null=True, verbose_name="1stメール")
  second_message = models.TextField(blank=True, null=True, verbose_name="2stメール")
  age = models.CharField(max_length=6, choices=age_list, blank=True, null=True, verbose_name="年齢")
  activity_area = models.CharField(max_length=5, choices=activity_area_list, null=True, blank=True, verbose_name="居住地")
  detail_activity_area = models.CharField(max_length=10, blank=True, null=True, verbose_name="詳細エリア")
  birth_place  = models.CharField(max_length=10, blank=True, null=True, verbose_name="出身地")
  blood_type = models.CharField(max_length=5, choices=blood_type_list, null=True, blank=True, verbose_name="血液型")
  constellation = models.CharField(max_length=6,  null=True, blank=True, verbose_name="星座")
  height = models.CharField(max_length=10,  choices=height_list, null=True, blank=True, verbose_name="身長")
  style = models.CharField(max_length=10,  null=True, blank=True, verbose_name="スタイル")
  looks = models.CharField(max_length=10,  null=True, blank=True, verbose_name="ルックス")
  cup = models.CharField(max_length=10,  null=True, blank=True, verbose_name="カップ")
  job = models.CharField(max_length=25,  null=True, blank=True, verbose_name="職業")
  education  = models.CharField(max_length=25,  null=True, blank=True, verbose_name="学歴")
  holiday = models.CharField(max_length=20,  null=True, blank=True, verbose_name="休日")
  relationship_status = models.CharField(max_length=20,  null=True, blank=True, verbose_name="交際ステータス")
  having_children = models.CharField(max_length=10,  null=True, blank=True, verbose_name="子ども")
  intention_to_marry = models.CharField(max_length=20,  null=True, blank=True, verbose_name="結婚に対する意思")
  smoking = models.CharField(max_length=20, null=True, blank=True, verbose_name="たばこ")
  sake = models.CharField(max_length=20, choices=sake_list, null=True, blank=True, verbose_name="お酒")
  car_ownership = models.CharField(max_length=20, choices=car_ownership_list, null=True, blank=True, verbose_name="クルマ")
  roommate = models.CharField(max_length=20,  null=True, blank=True, verbose_name="同居人")
  brothers_and_sisters = models.CharField(max_length=20, choices=brothers_and_sisters_list, null=True, blank=True, verbose_name="兄弟姉妹")
  until_we_met = models.CharField(max_length=20, choices=until_we_met_list, null=True, blank=True, verbose_name="出会うまでの希望")
  date_expenses = models.CharField(max_length=20, choices=date_expenses_list, null=True, blank=True, verbose_name="初回デート費用")
  memo = models.CharField(max_length=30,blank=True, null=True, verbose_name="メモ")

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
  mail_img = models.CharField(max_length=100, blank=True, null=True, verbose_name="画像送付")
  post_title = models.CharField(max_length=30, blank=True, null=True, verbose_name="掲示板タイトル")
  post_content = models.TextField( blank=True, null=True, verbose_name="掲示板内容文")
  second_message = models.TextField(blank=True, null=True, verbose_name="2stメール")
  condition_message = models.TextField(blank=True, null=True, verbose_name="アドレス内1stメール")
  return_foot_message = models.TextField(blank=True, null=True, verbose_name="足跡返し")
  mail_address = models.EmailField(blank=True, null=True, verbose_name="Gmaliアドレス")
  gmail_password = models.CharField(max_length=20,blank=True, null=True, verbose_name="Gmailパスワード")
  date_of_birth = models.IntegerField(blank=True, null=True, verbose_name="誕生日(８桁の数字)")
  self_promotion = models.TextField(blank=True, null=True, verbose_name="自己紹介")
  height = models.IntegerField(blank=True, null=True, verbose_name="身長")
  body_shape = models.CharField(max_length=20, choices=body_shape_list, null=True, blank=True, verbose_name="体重")
  blood_type = models.CharField(max_length=5, choices=blood_type_list, null=True, blank=True, verbose_name="血液型")
  activity_area = models.CharField(max_length=5, choices=activity_area_list, null=True, blank=True, verbose_name="活動地域")
  detail_activity_area = models.CharField(max_length=10, blank=True, null=True)
  profession = models.CharField(blank=True, null=True, verbose_name="職業")
  freetime = models.CharField(max_length=20, choices=freetime_list, null=True, blank=True, verbose_name="ヒマな時間帯")
  car_ownership = models.CharField(max_length=20, choices=car_ownership_list, null=True, blank=True, verbose_name="車の所有")
  smoking = models.CharField(max_length=20, choices=smoking_list, null=True, blank=True, verbose_name="喫煙")
  ecchiness_level = models.CharField(max_length=20, choices=ecchiness_level_list, null=True, blank=True, verbose_name="エッチ度")
  sake = models.CharField(max_length=20, choices=sake_list, null=True, blank=True, verbose_name="お酒")
  process_before_meeting = models.CharField(max_length=20, choices=process_before_meeting_list, null=True, blank=True, verbose_name="会うまでのプロセス")
  first_date_cost = models.CharField(max_length=20, choices=first_date_cost_list, null=True, blank=True, verbose_name="初回デート費用")
  is_active = models.BooleanField(default=True, verbose_name="アクティブ")
  memo = models.CharField(max_length=30,blank=True, null=True, verbose_name="メモ")

  
  def __str__(self):
    return self.name  # ここで表示したいフィールドを選択します
  
  class Meta:
    managed = True
    db_table = 'pcmax'
    verbose_name = "PCMAX"
    verbose_name_plural = "PCMAX"