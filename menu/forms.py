from django import forms

from menu.models import Dish

DIRECTION = (
    ('ASC', 'rosnąco'),
    ('DESC', 'malejąco')
)


class MenuSearchForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nazwa')
    SORTING = ('name', 'created', 'modified', 'dishes_length')
    SORTING_NAMES = ('nazwa', 'utworzono', 'zmodyfikowano', 'Liczba dań')
    sorting = forms.ChoiceField(choices=[('', '')] + list(zip(SORTING, SORTING_NAMES)), label='Sortuj po')
    sorting_direction = forms.ChoiceField(choices=DIRECTION, label='Kierunek sortowania')

    created_starting_date = forms.DateField(label='Utworzono po dniu')
    created_ending_date = forms.DateField(label='Utworzono przed dniem')

    edited_starting_date = forms.DateField(label='Zmodyfikowno po dniu')
    edited_ending_date = forms.DateField(label='Zmodyfikowno przed dniem')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False
