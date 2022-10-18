from django.urls import path

from familiar import views

app_name = "familiar"
urlpatterns = [
    path("familiares", views.familiares, name= "familiar-list"),
]
