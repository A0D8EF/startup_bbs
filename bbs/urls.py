from django.urls import path
from . import views

app_name = "bbs"
urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("edit/<int:pk>/", views.edit, name="edit"),
]