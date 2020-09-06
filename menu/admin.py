from django.contrib import admin

from .models import Menu, Dish


class MenuAdminView(admin.ModelAdmin):
    list_display = ['id', 'name',  'created', 'modified']
    search_fields = ['name']
    readonly_fields = ['created',  'modified']

    filter_horizontal = ('dishes', )
    list_filter = ('created',  'modified')
    fieldsets = ()


class DishAdminView(admin.ModelAdmin):
    list_display = ['id', 'name',  'created', 'modified']
    search_fields = ['name']
    readonly_fields = ['created',  'modified']

    filter_horizontal = ()
    list_filter = ('created',  'modified', 'is_vege')
    fieldsets = ()


admin.site.register(Menu, MenuAdminView)
admin.site.register(Dish, DishAdminView)
