from django.contrib import admin
from django.urls import path, include
import review.views

urlpatterns = [
    path('', review.views.index),
    path('create/<book_id>', review.views.create_review,
         name="create_review_route"),
    path('create/comment/<review_id>', review.views.create_comment,
         name="create_comment_route")
]