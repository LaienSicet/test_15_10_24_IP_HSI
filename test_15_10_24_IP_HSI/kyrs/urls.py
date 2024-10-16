from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('get-current-usd/', views.kyrs, name='kyrs'),
    ]