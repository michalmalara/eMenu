from django.urls import path
from django.contrib.auth import views as auth_views

from menu import views

# Views URLs
urlpatterns = [
    path(r'login/', auth_views.LoginView.as_view(), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

# Menu managing views
urlpatterns += [
    path(r'', views.MenuListView.as_view(), name='home'),
    path(r'menu_detail/<int:pk>', views.MenuDetailView.as_view(), name='menu_detail'),
    path(r'create_menu/', views.MenuCreateView.as_view(), name='create_menu'),
    path(r'edit_menu/<int:pk>', views.MenuUpdateView.as_view(), name='edit_menu'),
    path(r'add_dish_to_menu/<int:pk>', views.AddDishToMenu.as_view(), name='add_dish_to_menu'),
    path(r'delete_menu/<int:pk>', views.MenuDeleteView.as_view(), name='delete_menu'),
]

# Dish managing views
urlpatterns += [
    path(r'dish_list/', views.DishListView.as_view(), name='dish_list'),
    path(r'dish_detail/<int:pk>', views.DishDetailView.as_view(), name='dish_detail'),
    path(r'create_dish/', views.DishCreateView.as_view(), name='create_dish'),
    path(r'edit_dish/<int:pk>', views.DishUpdateView.as_view(), name='edit_dish'),
    path(r'delete_dish/<int:pk>', views.DishDeleteView.as_view(), name='delete_dish'),

]