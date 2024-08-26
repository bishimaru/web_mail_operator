from django import forms
from django.core.exceptions import ValidationError
from .models import *

class HappymailForm(forms.ModelForm):
    class Meta:
        model = Happymail
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user_id")
        is_active = cleaned_data.get("is_active")

        # is_active が True であればチェックを行う
        if is_active and user and not user.is_superuser:
            active_count = Happymail.objects.filter(user_id=user, is_active=True).count()
            if active_count >= 8:
                raise ValidationError('You cannot have more than 8 active Happymail records.')

        return cleaned_data

class PcmaxForm(forms.ModelForm):
    class Meta:
        model = Pcmax
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user_id")
        is_active = cleaned_data.get("is_active")

        # is_active が True であればチェックを行う
        if is_active and user and not user.is_superuser:
            active_count = Pcmax.objects.filter(user_id=user, is_active=True).count()
            if active_count >= 8:
                raise ValidationError('You cannot have more than 8 active Pcmax records.')

        return cleaned_data
