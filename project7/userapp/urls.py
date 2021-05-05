from django.urls import path
from userapp import views
userapp = views

userapp = "USERAPP"

urlpatterns = [
    path("sample/", views.sample, name = "sample"),
    path("login/", views.login, name= "userlogin"),
    path("register/", views.register),
    path("indexr/", views.indexregister),
]
