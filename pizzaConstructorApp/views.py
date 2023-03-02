from django.shortcuts import render, redirect
from django.http.response import HttpResponse
# https://realpython.com/django-redirects/

from .models import Ingredient, PizzaOrder, Size, PizzaToppings, Category
# from .forms import PizzaForm


def index(request):

    # model = Ingredient
    categories = Category.objects.all()
    toppings = Ingredient.objects.all()
    sizes = Size.objects.all()
    context = {'sizes': sizes, 'toppings': toppings, 'categories': categories}
    if request.method == 'POST':  # додати if form.valid
        # size = Size.objects.get(request.POST.get('size'))
        size = request.POST.get('size')
        pizza = PizzaOrder.objects.create(size=Size.objects.get(pk=size))

        # quantity = request.POST.get('topping')
        # toppings =
        toppings_names = [x.name for x in toppings]
        toppings_ids = []
        topping_quantities = []
        for topping_name in toppings_names:
            if request.POST.get(topping_name):
                id = request.POST.get(topping_name)
                quantity = request.POST.get(f"{topping_name}_quantity")

                raw = PizzaToppings.objects.create(topping=Ingredient(pk=id), topping_quantity=quantity,
                                                   pizza=PizzaOrder(pizza.pk))
                raw.save()
                # toppings_ids.append(request.POST.get(topping_name))

        return HttpResponse(topping_quantities)
        # return HttpResponse(request.POST.get('topping_quantity'))

    else:
        # form = PizzaForm(data=request.POST)
        # return HttpResponse(f'{form}')
        pass

    return render(request, 'pizzaConstructorApp/index.html', context)


def redirect_view(request):
    return redirect('constructor/')
