from django.shortcuts import render, redirect
# https://realpython.com/django-redirects/


def index(request):
    # return redirect('https://www.geeksforgeeks.org/iterators-in-python/')
    # return redirect('constructor/')
    return render(request, 'pizzaConstructorApp/index.html')

def redirect_view(request):
    # return redirect('https://www.geeksforgeeks.org/iterators-in-python/')
    return redirect('constructor/')
    # return render(request, 'pizzaConstructorApp/index.html')