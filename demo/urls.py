from django.contrib import admin
from django.urls import path
from demo import views
urlpatterns = [
    path('',views.index,name="home"),
    path('count/',views.count,name="count"),
]