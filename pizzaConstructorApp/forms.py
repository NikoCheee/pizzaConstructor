from django import forms
from .models import Pizza, PizzaToppings, Ingredient, Size

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['toppings', 'size']
        labels = {'toppings': 'начинка', 'size': 'розмір'}