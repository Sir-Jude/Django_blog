from django.urls import path
from . import views

urlpatterns = [
    path("", views.food_list, name="list"),
    path("<int:pk>/", views.food_detail, name="detail"),
    path("new-food/", views.new_food, name="new-food"),
    path("<int:pk>/update", views.edit_food, name="edit-food"),
]
