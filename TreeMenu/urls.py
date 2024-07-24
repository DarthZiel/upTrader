from django.contrib import admin
from django.urls import path
from .views import index, menu


urlpatterns = [
    path("", index),
    path("<slug:slug>", index, name='draw')
]
