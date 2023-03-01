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
    if request.method == 'POST':  # додати if form.valid
        # size = Size.objects.get(request.POST.get('size'))
        size = request.POST.get('size')
        pizza = Pizza.objects.create(size=Size.objects.get(pk=size))

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
                                                   pizza=Pizza(pizza.pk))
                raw.save()
                # toppings_ids.append(request.POST.get(topping_name))

        # for topping_name in toppings_names:
        #     print(topping_name, request.POST.get(topping_name))
        #     if request.POST.get(topping_name):
        #         print(request.POST.get(f"{topping_name}_quantity")+' топінгів')  # отримуб кількість топінгу
        #         topping_quantities.append(request.POST.get(f"{topping_name}_quantity"))
        #
        # for topping_id in toppings_ids:
        #     raw = PizzaToppings.objects.create(topping=Ingredient(pk=topping_id), topping_quantity=1, pizza=Pizza(pizza.pk))
        #     raw.save()
        #
        # "{{topping}}_quantity"

        # for topping_name in toppings_names:
        #     print(topping_name, request.POST.get(topping_name))
        #     if request.POST.get(topping_name):
        #         print(request.POST.get(f"{topping_name}_quantity")+' топінгів')  # отримуб кількість топінгу
        #         topping_quantities.append(request.POST.get(f"{topping_name}_quantity"))
        #
        # for topping_id in toppings_ids:
        #     raw = PizzaToppings.objects.create(topping=Ingredient(pk=topping_id), topping_quantity=1, pizza=Pizza(pizza.pk))
        #     raw.save()

        return HttpResponse(topping_quantities)
        # return HttpResponse(request.POST.get('topping_quantity'))

    else:
        # form = PizzaForm(data=request.POST)
        # return HttpResponse(f'{form}')
        pass

    return render(request, 'pizzaConstructorApp/index.html', context)


def redirect_view(request):
    return redirect('constructor/')
