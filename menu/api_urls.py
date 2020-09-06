from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from menu.api_views import MenuDetailApiView, DishDetailApiView, MenuListPublicApiView, DishDetailPublicApiView

router = routers.DefaultRouter()
router.register(r'menu', MenuDetailApiView, basename='menu')
router.register(r'public/menu', MenuListPublicApiView, basename='menu_public')
router.register(r'dish', DishDetailApiView, basename='dish')
router.register(r'public/dish', DishDetailPublicApiView, basename='dish_public')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api-login'),
    path('api-auth/', include('rest_framework.urls')),
]
