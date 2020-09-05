from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from menu.api_views import MenuDetailApiView, DishDetailApiView

router = routers.DefaultRouter()
router.register(r'menu', MenuDetailApiView, basename='menu')
router.register(r'dish', DishDetailApiView, basename='dish')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api-login'),
    path('api-auth/', include('rest_framework.urls')),
]
