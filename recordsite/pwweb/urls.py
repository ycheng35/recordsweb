from django.urls import path

from . import views

app_name = "pwweb"
urlpatterns = [
    path("", views.index, name="index"),
    path("create_record/", views.create_record, name="create_record"),
]