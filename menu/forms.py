from django import forms

from menu.models import Menu

DIRECTION = (
    ('ASC', 'rosnąco'),
    ('DESC', 'malejąco')
)


class MenuSearchForm(forms.ModelForm):
    SORTING = ('name', 'created', 'modified',)
    SORTING_NAMES = ('nazwa', 'utworzono', 'zmodyfikowano')
    sorting = forms.ChoiceField(choices=[('', '')] + list(zip(SORTING, SORTING_NAMES)), label='Sortuj po')
    sorting_direction = forms.ChoiceField(choices=DIRECTION, label='Kierunek sortowania')

    created_starting_date = forms.DateField(label='Utworzono po dniu')
    created_ending_date = forms.DateField(label='Utworzono przed dniem')

    edited_starting_date = forms.DateField(label='Zmodyfikowno po dniu')
    edited_ending_date = forms.DateField(label='Zmodyfikowno przed dniem')

    class Meta:
        model = Menu
        fields = ('name',)
        labels = {
            'name': 'Szukaj',
        }
        widgets = {
            'name': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False
