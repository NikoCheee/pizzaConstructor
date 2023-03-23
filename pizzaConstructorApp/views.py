from django.shortcuts import render, redirect
from django.db.models import Sum, F
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse
# https://realpython.com/django-redirects/

from .models import Ingredient, PizzaOrder, Size, PizzaToppings, Category, Sauce, CheeseBoard
# from .forms import PizzaForm


def index(request):
    categories = Category.objects.all()
    toppings = Ingredient.objects.all()
    sizes = Size.objects.all()
    sauces = Sauce.objects.all()
    boards = CheeseBoard.objects.all()
    context = {'sizes': sizes, 'toppings': toppings, 'categories': categories, 'sauces': sauces, 'boards': boards}

    if request.method == 'POST':  # додати if form.valid
        # отримую реквести з форми
        size_rq = request.POST.get('size')
        sauce_rq = request.POST.get('sauce')
        board_rq = request.POST.get('board')

        # створюю об'єкти піца та її складові
        size = Size.objects.get(pk=size_rq)
        sauce = Sauce.objects.get(pk=sauce_rq)
        board = CheeseBoard.objects.get(pk=board_rq)
        pizza = PizzaOrder.objects.create(size=size, total_price=size.price)

        # додаю усі топінги поточної створеної піци у базу
        toppings_names = [x.name for x in toppings]
        for topping_name in toppings_names:
            if request.POST.get(topping_name):
                id = request.POST.get(topping_name)
                quantity = request.POST.get(f"{topping_name}_quantity")
                price = Ingredient.objects.get(pk=id).price * int(quantity)

                PizzaToppings.objects.create(topping=Ingredient(pk=id), topping_quantity=quantity,
                                             pizza_order=PizzaOrder(pizza.pk), price=price)

        # рахую ціну топінгів та остаточну ціну піци з урахуванням топінгів, соусу та сирного бортика
        toppings_price = PizzaToppings.objects.filter(pizza_order=pizza.pk).aggregate(toppings_price=Sum('price'))
        pizza.total_price = F('total_price') + toppings_price['toppings_price'] + sauce.price + board.price
        pizza.save()

        pizza = PizzaOrder.objects.get(pk=pizza.pk)
        context = {'test': pizza}

        return render(request, 'pizzaConstructorApp/grac.html', context)  # можливо треба буде змінити на реверс

    # else:
    #     # form = PizzaForm(data=request.POST)
    #     # return HttpResponse(f'{form}')
    #     pass

    return render(request, 'pizzaConstructorApp/index.html', context)


def redirect_view(request):
    return redirect('constructor/')
