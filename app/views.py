from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class IndexView(TemplateView):
    template_name = 'index.html'

def how_to_use_view(request):
    template_name = 'how_to_use.html'
    return render(request, template_name)

def terms_of_service_view(request):
    template_name = 'terms_of_service.html'
    return render(request, template_name)



class UserDataView(APIView):
    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
       

        try:
            user = User.objects.get(username=name)
            user_email = user.email
            if not user.is_active:
                return Response({'error': '有効期限が切れています。'}, status=status.HTTP_204_NO_CONTENT)

            if user.check_password(password):
                userprofile_data = UserProfile.objects.filter(user=user)
                userprofile_serializer = UserProfileSerializer(userprofile_data, many=True)
                happymail_data = Happymail.objects.filter(user_id=user.id, is_active=True)
                # happymail_serializer = HappymailSerializer(happymail_data, many=True)
                # リクエストコンテキストをシリアライザに渡す
                happymail_serializer = HappymailSerializer(happymail_data, many=True, context={'request': request})
                
                pcmax_data = Pcmax.objects.filter(user_id=user.id, is_active=True)
                pcmax_serializer = PcmaxSerializer(pcmax_data, many=True)
                
                userprofile_serializer.data[0]["username"] = name
                userprofile_serializer.data[0]["password"] = password
                userprofile_serializer.data[0]["user_email"] = user_email
                # print(userprofile_serializer.data,)
                return Response({
                    'happymail': happymail_serializer.data,
                    'pcmax': pcmax_serializer.data,
                    "user":userprofile_serializer.data,

                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
