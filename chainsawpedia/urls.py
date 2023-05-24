"""chainsawpedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main.views import home
from volumes.views import volume_list, volume_detail
from characters.views import character_list, character_detail
from mangas.views import manga_detail
from seasons.views import season_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('volume/', volume_list, name='volume_list'),
    path('volume/<int:pk>', volume_detail, name='volume_detail'),
    path('character/', character_list, name='character_list'),
    path('character/<int:pk>', character_detail, name='character_detail'),
    path('manga/<int:pk>', manga_detail, name='manga_detail'),
    path('season/', season_list, name='season_list'),
    path('', home, name='home'),
]
