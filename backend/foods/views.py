from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Food
from .forms import FoodForm


def food_list(request):
    number_of_visitors = request.session.get("number_of_visitors", 1)
    request.session["number_of_visitors"] = number_of_visitors + 1
    request.session["user_logged_in"] = True
    list_of_favorite_foods = Food.objects.all()
    context = {
        "list_of_favorite_foods": list_of_favorite_foods,
        "count": list_of_favorite_foods.count(),
        "number_of_visitors": number_of_visitors,
    }
    return render(request, "foods/food_list.html", context)


def food_detail(request, pk):
    # BEFORE: SELECT * FROM foods_food WHERE id = 8;
    # food = Food.objects.get(id=pk)
    food = Food.objects.get(id=pk)
    return render(request, "foods/food_detail.html", {"food": food})


def new_food(request):
    form = FoodForm()
    if request.method == "POST":
        form = FoodForm(request.POST)
        # check for post validity
        if form.is_valid():
            form.save()
            # "reverse" is a black box:
            # after saving the game, we are sent back to our "list" (file urls.py)
            return HttpResponseRedirect(reverse("list"))
    return render(request, "foods/new.html", {"form": form})


def edit_food(request, pk):
    food = Food.objects.get(pk=pk)
    form = FoodForm(instance=food)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("detail", kwargs={"pk": pk}))
    return render(request, "foods/edit_food.html", {"form": form})
