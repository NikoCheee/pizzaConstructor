from django.shortcuts import render, redirect
from django.http.response import HttpResponse
# https://realpython.com/django-redirects/

from .models import Ingredient, Pizza, Size, PizzaToppings
# from .forms import PizzaForm


def index(request):

    # model = Ingredient
    toppings = Ingredient.objects.all()
    sizes = Size.objects.all()
    context = {'sizes': sizes, 'toppings': toppings}
    if request.method != 'POST':
        pass
    else:
        # form = PizzaForm(data=request.POST)
        # return HttpResponse(f'{form}')
        pass

    return render(request, 'pizzaConstructorApp/index.html', context)


def redirect_view(request):
    return redirect('constructor/')
