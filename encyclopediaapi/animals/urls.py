from django.urls import path
from animals import views


urlpatterns = [
    path('', views.AnimalList.as_view()),
    
]