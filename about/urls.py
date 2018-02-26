from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AboutList.as_view()),
]

