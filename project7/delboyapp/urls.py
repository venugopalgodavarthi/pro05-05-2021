from django.urls import path
from delboyapp import views
urlpatterns = [
    path("carry/<data>",views.carrydata, name="carry")
]
