from django.contrib import admin
from django.urls import path

from einstein.views import AmioAchiAPIView

urlpatterns = [
    path('add/', AmioAchiAPIView.as_view()),
]
