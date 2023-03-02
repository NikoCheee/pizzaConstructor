from django.contrib import admin
from .models import PizzaOrder, Ingredient, PizzaToppings, Size, Category

admin.site.register(Ingredient)
admin.site.register(PizzaOrder)
admin.site.register(PizzaToppings)
admin.site.register(Size)
admin.site.register(Category)
