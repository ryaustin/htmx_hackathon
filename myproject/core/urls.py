from django.urls import path
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/1/edit", views.contact_1_edit, name="contact_1_edit"),
]