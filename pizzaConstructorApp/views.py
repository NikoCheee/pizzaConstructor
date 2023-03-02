from django.shortcuts import render, redirect
from django.http.response import HttpResponse
# https://realpython.com/django-redirects/

from .models import Ingredient, PizzaOrder, Size, PizzaToppings, Category
# from .forms import PizzaForm


def index(request):
    categories = Category.objects.all()
    toppings = Ingredient.objects.all()
    sizes = Size.objects.all()
    context = {'sizes': sizes, 'toppings': toppings, 'categories': categories}

    if request.method == 'POST':  # додати if form.valid
        print(request.POST)
        size = request.POST.get('size')
        pizza = PizzaOrder.objects.create(size=Size.objects.get(pk=size))

        toppings_names = [x.name for x in toppings]
        for topping_name in toppings_names:
            if request.POST.get(topping_name):
                id = request.POST.get(topping_name)
                quantity = request.POST.get(f"{topping_name}_quantity")
                price = Ingredient.objects.get(pk=id).price * int(quantity)

                raw = PizzaToppings.objects.create(topping=Ingredient(pk=id), topping_quantity=quantity,
                                                   pizza_order=PizzaOrder(pizza.pk), cost=price)
                raw.save()

        return HttpResponse()

    else:
        # form = PizzaForm(data=request.POST)
        # return HttpResponse(f'{form}')
        pass

    return render(request, 'pizzaConstructorApp/index.html', context)


def redirect_view(request):
    return redirect('constructor/')
