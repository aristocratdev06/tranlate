from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path("", home, name="home"),
    path("<slug:slug>", translate, name="mulomot")
]
