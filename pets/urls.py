from django.urls import path
from .views import PetView, PetSpecificView

urlpatterns = [
    path("pets/", PetView.as_view()),
    path("pets/<int:pet_id>/", PetSpecificView.as_view()),
]
