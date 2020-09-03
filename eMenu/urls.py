"""eMenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, reverse
from django.contrib.auth import views as auth_views

from eMenu import settings

from menu import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MenuListView.as_view(), name='home'),
    path('menu_detail/<int:pk>', views.MenuDetailView.as_view(), name='menu_detail'),
    path('dish_detail/<int:pk>', views.DishDetailView.as_view(), name='dish_detail'),
    path('create_menu/', views.MenuCreateView.as_view(), name='create_menu'),
    path('create_dish/', views.DishCreateView.as_view(), name='create_dish'),
    path('add_dish_to_menu/<int:pk>', views.AddDishToMenu.as_view(), name='add_dish_to_menu'),
    path(r'login/', auth_views.LoginView.as_view(), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
