"""
URL configuration for youtube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.Home),
    path('movies',v.Movie),
    path('song',v.Song),
    path('edu',v.Education),
    path('business',v.Bussiness),
    path('python',v.Python),
    path('javascript',v.Javascript),
    path('web',v.Web),
    path('Search_word',v.Seacrh),
    path('savetoplay/<int:id>',v.Save_play),
    path('history/<int:id>',v.History),
    path('history_my',v.History_my),
    path('playlist',v.Playlist),
]

