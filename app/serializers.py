from rest_framework import serializers
from .models import Happymail, Pcmax

class HappymailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happymail
        fields = '__all__'

class PcmaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pcmax
        fields = '__all__'
