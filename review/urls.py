from django.contrib import admin
from django.urls import path, include
import review.views

urlpatterns = [
    path('', review.views.index),
    path('create', review.views.create_review)
]
