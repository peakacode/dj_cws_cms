from django.urls import path

from .views import index, about

name_space = "pages"
urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
]
