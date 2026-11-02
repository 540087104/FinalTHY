from django.contrib import admin
from django.urls import path
from diagnose.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("index", index, name="index"),
]
