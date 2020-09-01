from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
    paginate_by = 10

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


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish_detail_view.html'
