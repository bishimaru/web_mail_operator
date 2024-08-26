from django.contrib import admin
from .models import Pcmax, Happymail
from .forms import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse

class PcmaxAdmin(admin.ModelAdmin):
    # form = PcmaxForm
    list_display = ('name', 'login_id', 'post_title')  # 表示するフィールドを指定
    # 編集可能なフィールドを指定（必要に応じて）
    fields = ('user_id', 'name', 'login_id', 'password',   'post_title', 'post_content', 'return_foot_message',
              # 'mail_img','fst_mail',
              # 'second_message', 'condition_message',  'date_of_birth', 'self_promotion', 
              # 'height', 'body_shape', 'blood_type', 'activity_area', 'detail_activity_area', 'profession', 
              # 'freetime', 'car_ownership', 'smoking', 'ecchiness_level', 'sake', 'process_before_meeting', 
              # 'first_date_cost'
              )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        return qs.filter(user_id=request.user)
    
    
    def get_fields(self, request, obj=None):
        # スーパーユーザーでない場合、idとuser_idを表示しない
        fields = super().get_fields(request, obj)
        if not request.user.is_superuser:
            fields = [field for field in fields if field not in ('id', 'user_id')]
        return fields
    
    def get_list_display(self, request):
        # スーパーユーザーのみ user_id を表示
        if request.user.is_superuser:
            # return ['user_id'] + self.list_display
            return ['user_id'] + list(self.list_display) 
            
        return self.list_display
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # 新しいオブジェクトの場合のみ
            obj.user_id = request.user
        
        # is_activeがTrueの場合に制限を適用
        if obj.is_active and not obj.user_id.is_superuser:
            active_count = Happymail.objects.filter(user_id=obj.user_id, is_active=True).count()
            if active_count >= 8:
                messages.error(request, 'You cannot have more than 8 active Happymail records.')
                return
admin.site.register(Pcmax, PcmaxAdmin)


class HappymailAdmin(admin.ModelAdmin):
    # form = HappymailForm
    list_display = ['name', 'post_title', 'is_active']
    fields = ['user_id', 'name', 'login_id', 'password', 'post_title', 'post_contents', 'return_foot_message', 'is_active']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_id=request.user)

    def response_add(self, request, obj, post_url_continue=None):
        if not obj.pk:  # 新しいオブジェクトの場合のみ
            obj.user_id = request.user
        
        # is_activeがTrueの場合に制限を適用
        if obj.is_active and not obj.user_id.is_superuser:
            active_count = Happymail.objects.filter(user_id=obj.user_id, is_active=True).count()
            if active_count >= 8:
                messages.error(request, 'アクティブな Happymail キャラを 8 つ以上持つことはできません。')
                # 成功メッセージを削除
                messages.set_level(request, messages.WARNING)  # メッセージのレベルを一時的に変更
                response = super().response_add(request, obj, post_url_continue)
                messages.set_level(request, messages.SUCCESS)  # メッセージのレベルを元に戻す
                return HttpResponseRedirect(reverse('admin:app_happymail_changelist'))
        return super().response_add(request, obj, post_url_continue)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # 新しいオブジェクトの場合のみ
            obj.user_id = request.user
        
        # is_activeがTrueの場合に制限を適用
        if obj.is_active and not obj.user_id.is_superuser:
            active_count = Happymail.objects.filter(user_id=obj.user_id, is_active=True).count()
            if active_count >= 8:
                return  # データの保存をキャンセル

        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_superuser:
            fields = [field for field in fields if field not in ('id', 'user_id')]
        return fields

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ['user_id'] + self.list_display
        return self.list_display


admin.site.register(Happymail, HappymailAdmin)