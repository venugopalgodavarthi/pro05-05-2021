from django.urls import path
from ownerapp import views

urlpatterns = [
    path("sample/", views.ownerregister),
    path("register/", views.register , name ="login"),
    path("ologin/", views.ologin),
    path("oregister/", views.oregister),
    path("index/", views.index),
]
