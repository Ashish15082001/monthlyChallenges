from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('january/', views.january),
    path('february/', views.february),
]