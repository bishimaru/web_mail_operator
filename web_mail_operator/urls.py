from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from app import views
from django.urls import path, include


router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.IndexView.as_view(), name='index'),
    path('how_to_use/', views.how_to_use_view, name='how_to_use'), 
    path('api/', include(router.urls)),
    path('api/user-data/', views.UserDataView.as_view(), name='user-data'),

]
