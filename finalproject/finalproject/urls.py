"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),
    path('menu/', views.menu_view),
    path('location/', views.location_view),
    path('feedback/', views.feedback_view),
    path('table/', views.table_view),
    path('submit/', views.submit_view),
    path('download/', views.download_view),
    path('register/', views.register_view),
    path('list/', views.list_view),
    path('scoups/', views.scoups_view),
    path('salads/', views.salads_view),
    path('deserts/', views.deserts_view),
    path('smooth/', views.smooth_view),
]
