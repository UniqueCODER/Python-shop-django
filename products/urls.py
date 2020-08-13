from django.urls import path
from . import views


urlpatterns = [
    #root of our app
    path('',views.index),
    path('new', views.new)
]