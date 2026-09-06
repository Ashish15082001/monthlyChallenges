from . import views
from django.urls import path

urlpatterns = [
   path("<int:month>/", views.challenges_int),
   path("<str:month>/", views.challenges_string, name="monthly-challenge"),
]