from .views import HomeView

from django.urls import path

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
]