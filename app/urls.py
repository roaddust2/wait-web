from django.urls import path
from app import views


urlpatterns = [
    path('', views.home.IndexView.as_view(), name='index'),
]
