from rest_framework import serializers
from .models import *

class HappymailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happymail
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class PcmaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pcmax
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
