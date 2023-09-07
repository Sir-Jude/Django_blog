from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from .models import Game
from .forms import GameForm


def game_list(request):
    games = Game.objects.all()
    context = {
        "list_of_games": games,
        "count": games.count(),
    }
    return render(request, "blog/game_list.html", context)


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "blog/game_detail.html", {"game": game})


def new_game(request):
    form = GameForm()
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog_list"))
    return render(request, "blog/new_game.html", {"form": form})


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    form = GameForm(instance=game)
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("game_detail", kwargs={"pk": pk}))
    return render(request, "blog/edit_game.html", {"form": form})
