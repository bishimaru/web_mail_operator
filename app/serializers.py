from rest_framework import serializers
from .models import Happymail

class HappymailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happymail
        fields = '__all__'
