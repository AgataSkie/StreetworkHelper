from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlaceListView.as_view(), name='index'),
]