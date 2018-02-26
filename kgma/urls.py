from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.KgmaList.as_view()),
]

