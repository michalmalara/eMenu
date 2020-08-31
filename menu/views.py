from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from menu.models import Menu, Dish


class MenuListView(ListView):
    model = Menu
    template_name = 'index.html'


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail_view.html'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail_view.html'

