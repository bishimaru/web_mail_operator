from rest_framework import serializers
from .models import *

class HappymailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happymail
        fields = '__all__'

class PcmaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pcmax
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
