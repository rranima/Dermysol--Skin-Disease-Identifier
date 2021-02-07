"""dermysol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from uimage import views as uimage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.homepage,name='home'),
    path('dashboard/',user_views.dashboard,name='dashboard'),
    path('register/', user_views.registeruser,name='register'),
    path('login/', user_views.loginuser,name='login'),
    path('logout/', user_views.logoutuser,name='logout'),
    path('predictimage', uimage_views.predictimage,name='predictimage'),
    path('doctor/', user_views.doctor,name='doctor'),
    path('diseaseinfo/',user_views.diseaseinfo,name='diseaseinfo'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)