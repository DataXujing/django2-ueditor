"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import xadmin
from django.urls import path,include
import DjangoUeditor 

from blog_list import views as views_ueditor

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),

    path('ueditor-test/',views_ueditor.ueditor_test),
    path('ueditor-blog/',views_ueditor.ueditor_blog),


]
