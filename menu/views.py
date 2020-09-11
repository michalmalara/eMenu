from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.template.defaulttags import register

from menu.forms import MenuSearchForm
from menu.models import Menu, Dish


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Function returns GET parameters to use with pagination next/prev data.
    It allows to keep search and ordering settings with pagination.
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()


class MenuListView(ListView):
    model = Menu
    template_name = 'index.html'
    ordering = 'pk'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Menu.objects.all()
        else:
            return Menu.objects.all().exclude(dishes_count__lt=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        search_form = MenuSearchForm(self.request.GET)

        if search_form.is_valid():
            name = search_form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

            sorting = search_form.cleaned_data['sorting']
            if sorting:
                sorting_direction = search_form.cleaned_data['sorting_direction']
                if sorting_direction == 'DESC':
                    sorting = '-' + sorting
                queryset = queryset.order_by(sorting, '-pk')

            created_starting_date = search_form.cleaned_data['created_starting_date']
            created_ending_date = search_form.cleaned_data['created_ending_date']
            if created_starting_date and created_ending_date:
                queryset = queryset.filter(created__gte=created_ending_date,
                                           created__lte=created_ending_date)
            if created_starting_date and not created_ending_date:
                queryset = queryset.filter(created__gte=created_starting_date)
            if not created_starting_date and created_ending_date:
                queryset = queryset.filter(created__lte=created_ending_date)

            edited_starting_date = search_form.cleaned_data['edited_starting_date']
            edited_ending_date = search_form.cleaned_data['edited_ending_date']
            if edited_starting_date and created_ending_date:
                queryset = queryset.filter(created__gte=edited_ending_date,
                                           created__lte=edited_starting_date)
            if edited_starting_date and not edited_ending_date:
                queryset = queryset.filter(created__gte=edited_starting_date)
            if not edited_starting_date and edited_ending_date:
                queryset = queryset.filter(created__lte=edited_ending_date)

        return super().get_context_data(
            search_form=search_form,
            object_list=queryset,
            **kwargs)


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail_view.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            menu_queryset = Menu.objects.get(pk=self.kwargs['pk'])
            menu_queryset.dishes.remove(self.request.POST['dish_pk'])
            return redirect(reverse('menu_detail', args=[self.kwargs['pk']]))
        else:
            return HttpResponse('Tylko zalogowani użytkownicy mogą to zrobić.', status=403)


class DishListView(ListView):
    model = Dish
    template_name = 'dish_list_view.html'
    paginate_by = 10
    ordering = 'pk'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail_view.html'


class MenuCreateView(LoginRequiredMixin, CreateView):
    model = Menu
    fields = ('name', 'description', 'dishes')
    template_name = 'create_menu_view.html'
    success_url = '/'


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    fields = ('name', 'description', 'price', 'preparation_time', 'is_vege', 'picture')
    template_name = 'create_dish_view.html'
    success_url = '/'


class AddDishToMenu(LoginRequiredMixin, ListView):
    model = Dish
    template_name = 'add_dish_to_menu.html'

    def post(self, *args, **kwargs):
        menu_queryset = Menu.objects.get(pk=self.kwargs['pk'])
        menu_queryset.dishes.add(self.request.POST['dish_pk'])
        menu_queryset.save()
        return redirect(reverse('add_dish_to_menu', args=[self.kwargs['pk']]))

    def get_context_data(self, *, object_list=None, **kwargs):
        menu_queryset = Menu.objects.get(pk=self.kwargs['pk'])
        dishes_pk = [mpk.pk for mpk in menu_queryset.dishes.all()]

        objects = Dish.objects.all().exclude(pk__in=dishes_pk)

        return_url = reverse('menu_detail', args=[self.kwargs['pk']])

        return super().get_context_data(
            object_list=objects,
            return_url=return_url,
        )