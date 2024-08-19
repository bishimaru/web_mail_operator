from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from app import views
from django.urls import path, include


router = DefaultRouter()
router.register(r'happymail', views.HappymailViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manipulate/', views.manipulate_browser, name='manipulate_browser'),
    path('', views.IndexView.as_view(), name='index'),
    path('task_management/', views.task_management, name='task_management'),  
    path('login/', views.login_view, name='login'), 
    path('invalid_login/', views.invalid_login_view, name='invalid_login'), 
    path('api/', include(router.urls)),
]
