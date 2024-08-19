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
from .serializers import HappymailSerializer


def manipulate_browser(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(url)
            # ここで必要な操作を実行する

    return render(request, 'manipulate_browser.html')

class IndexView(TemplateView):
    template_name = 'index.html'

def task_management(request):
    user = request.user
    happymail_entries = Happymail.objects.filter(user_id=user)
    print(777)
    print(happymail_entries)
    # pcmax_entries = Pcmax.objects.filter(user_id=user)
    # return render(request, 'task_management.html', {'happymail_entries': happymail_entries, 'pcmax_entries': pcmax_entries})
    return render(request, 'task_management.html', {'happymail_entries': happymail_entries})


def login_view(request):
    if request.user.is_authenticated:
        print(7777777)
        return redirect('task_management')  # ユーザーがログインしている場合はリダイレクト
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_management')  # ログイン成功時のリダイレクト先
        else:
            return redirect('invalid_login')  # ログイン失敗時のメッセージ
    return render(request, 'login.html')  # GETリクエストの場合はログインフォームを表示

def invalid_login_view(request):
    return render(request, 'invalid_login.html')

class HappymailViewSet(viewsets.ModelViewSet):
    queryset = Happymail.objects.all()
    serializer_class = HappymailSerializer