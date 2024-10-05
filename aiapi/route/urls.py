from django.contrib import admin
from django.urls import path,include
from aiapi import views

urlpatterns = [
    path('',views.Questions.as_view(),name="reply"),
]