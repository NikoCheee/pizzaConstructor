from django.contrib import admin
from .models import Pizza, Ingredient, PizzaToppings, Size

admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(PizzaToppings)
admin.site.register(Size)

# admin - 1234