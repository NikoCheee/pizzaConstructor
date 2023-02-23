"""створити модель "інгрідієнти"(категорія, ціна, грами, назва
створити модель "основа": розмір, намазка
створити модель "піцца" (хз нашо, мабуть має комбінувати попередні дві)


для інгрідієнтів:
треба вказати ціну, назву, грами
кнопочки щоб додавати та віднімати елементи
при цому мають з'являтись назви цих елементів десь
ці додані елементи мають відніматись з бази, де загальна кількість інгрідієнтів


"""
from django.db import models
from django.core.validators import MaxValueValidator


# class Category(models.Model):
#     name = models.CharField(max_length=100)


class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=2)  # вага інгрідієнту додавамого у піцу
    altogether = models.DecimalField(max_digits=5, decimal_places=2) # кількість у наявності, якщо постійно меншувати, то потім покаже, що ього елементу нема
    # limit - треба дізнатися про обмеження поля
    amount = models.PositiveSmallIntegerField(default=0)  #  кількість доданих елементів у піццу
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)  #  - для розділення на сторінці: м'ясо, сир, фрукти овочі, соус, база для піцци

    def amount_subtraction(self):
        # total = self.weight*self.amount
        self.altogether -= self.weight

        # return self.amount

    def __str__(self):
        return self.name


class Size(models.Model):  # зробити тут розміри піцц, а не у самій піцці
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.size

class Pizza(models.Model):  # перейменувати у клас сайз
    # pizza30cm = '30'
    # pizza40cm = '40'
    # PIZZA_SIZE_CHOICES = [
    #     (pizza30cm, 'Піцца 30 см'),
    #     (pizza40cm, 'Піцца 40 см'),
    # ]
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Ingredient, through='PizzaToppings')
    # total_cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"pizza + топпінги"


class PizzaToppings(models.Model):
    topping = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    topping_quantity = models.SmallIntegerField(validators=[MaxValueValidator(10, message='Test')])
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.topping} у піцці № {self.pizza.pk}, {self.topping_quantity} штук'
