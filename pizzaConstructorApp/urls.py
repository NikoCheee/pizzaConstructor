from django.urls import path
from . import views

app_name = 'pizza'
urlpatterns = [
    path('', views.index, name='index'),
    # path('grac', views.index, name='ordered'),
]