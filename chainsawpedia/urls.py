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
from animes.views import AnimeView
from arcs.views import ArcView
from main.views import home
from sagas.views import SagaView
from volumes.views import VolumeView, volume_list
from characters.views import CharacterView, character_list, character_detail
from mangas.views import MangaView, manga_detail
from seasons.views import SeasonView, season_list
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for your application",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('volume/', volume_list, name='volume_list'),
    path('character/', character_list, name='character_list'),
    path('character/<int:pk>', character_detail, name='character_detail'),
    path('manga/<int:pk>', manga_detail, name='manga_detail'),
    path('season/', season_list, name='season_list'),
    path('', home, name='home'),
    path('api/character/', CharacterView.as_view(), name='character-list'),
    path('api/character/<str:name>/', CharacterView.as_view(), name='character'),
    path('api/volume/', VolumeView.as_view(), name='volume-list'),
    path('api/manga/', MangaView.as_view(), name='manga-list'),
    path('api/manga/<int:number>', MangaView.as_view(), name='manga'),
    path('api/anime/', AnimeView.as_view(), name='anime-list'),
    path('api/arc/', ArcView.as_view(), name='arc-list'),
    path('api/season/', SeasonView.as_view(), name='season-list'),
    path('api/saga/', SagaView.as_view(), name='saga-list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
