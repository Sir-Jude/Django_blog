from django.urls import path
from . import views

urlpatterns = [
    path("", views.game_list, name="game_list"),
    path("<int:pk>/", views.game_detail, name="game_detail"),
    path("new-game/", views.new_game, name="new-game"),
    path("<int:pk>/update", views.edit_game, name="edit-game"),
]
