from django.contrib import admin
from .models import PizzaOrder, Ingredient, PizzaToppings, Size, Category, Sauce, CheeseBoard

admin.site.register(Ingredient)
admin.site.register(PizzaOrder)
admin.site.register(PizzaToppings)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Sauce)
admin.site.register(CheeseBoard)
