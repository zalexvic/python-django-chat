"""chatapp URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from register import views as reg_views
from chat import views as chat_views

urlpatterns = [
    path('', chat_views.index, name='index'),
    path('chat/', include('chat.urls')),
    path('sign-up/', reg_views.sign_up, name='sign_up'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('create-room/', chat_views.create_room, name='create_room'),
    path('profile/', chat_views.profile, name='profile'),
    path('all-rooms/', chat_views.all_rooms, name='all_rooms')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
