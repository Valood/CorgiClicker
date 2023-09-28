from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns =[
    path("register", RegisterAPIView.as_view()),
    path("render_register", register_user_render),
    path("logout", LogoutAPIView.as_view()),
    path("", LoginAPIView.as_view()),
    path("game", GameAPIView.as_view()),
    path("boost", BoostAPIView.as_view())
]