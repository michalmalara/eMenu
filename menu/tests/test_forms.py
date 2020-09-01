from django.test import TestCase

from menu.forms import MenuSearchForm


class TestForms(TestCase):
    def test_menu_search_form(self):
        form = MenuSearchForm(data={
            'name': 'menu 1',
            'sorting': 'created',
            'sorting_direction': 'ASC'
        })
        self.assertTrue(form.is_valid())

    # def test_menu_search_date_not_valid(self):
    #     form = MenuSearchForm(data={
    #         'created_starting_date': 'menu 1',
    #         'created_ending_date': 'created',
    #         'edited_starting_date': 'ASC',
    #         'edited_ending_date': '2020-04-05'
    #     })
    #     self.assertFalse(form.is_valid())
