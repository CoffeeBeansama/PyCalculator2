from django.urls import path
from . import views

urlpatterns = [
    path("", views.calculator,name="Main Page"),
]
