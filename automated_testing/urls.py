"""automated_testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from apitest import apitest_views
from product import product_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', apitest_views.test),
    path('login/', apitest_views.login),
    path('home/',apitest_views.home),
    path('logout/',apitest_views.logout),  # 退出登录
    path('product_manage/', product_views.product_manage),

]
