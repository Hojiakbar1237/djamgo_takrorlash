from django.contrib import admin
from django.urls import path
from .views import register_html,loogin_html

urlpatterns = (
    path('register/', register_html),
    path('loogin/', loogin_html)
)