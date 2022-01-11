from django.urls import path
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/<int:id>/edit", views.contact_1_edit, name="contact_1_edit"),
    path("contact/<int:id>", views.contact_1, name="contact_1"),
]