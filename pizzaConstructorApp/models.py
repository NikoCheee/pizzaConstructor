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


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sauce(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'Соус {self.name}, ціна {self.price}'


class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=2)  # вага інгрідієнту додаваємого у піцу
    # кількість у наявності, якщо постійно зменшувати, то потім покаже, що цього елементу нема
    altogether = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  #  - для розділення на сторінці: м'ясо, сир, фрукти овочі

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


class PizzaOrder(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Ingredient, through='PizzaToppings')
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"піцца {self.pk} розміром {self.size} + топпінги, замовленно {self.ordered_at}"


class PizzaToppings(models.Model):
    topping = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    topping_quantity = models.SmallIntegerField(validators=[MaxValueValidator(10, message='Test')])
    pizza_order = models.ForeignKey(PizzaOrder, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.topping} у замовленні № {self.pizza_order}, {self.topping_quantity} штук. Ціна {self.cost}'
