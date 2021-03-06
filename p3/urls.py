"""p3 URL Configuration

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
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', view.index, name='index'),
    path('home', view.home, name='home'),
    path('second', view.second, name='second'),
    path('third', view.third, name='third'),
    path('fourth', view.fourth, name='fourth'),
    path('fifth', view.fifth, name='fifth'),
    path('urls_data/<name>', view.urls_data, name='urls_data'),
    path('url_sum/<ab>', view.url_cal, name='url_ab'),
    path('url_ovel/<s>', view.ovel, name='url_ovel'),
]
