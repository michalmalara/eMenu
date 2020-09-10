from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers, permissions
from rest_framework.authtoken.views import obtain_auth_token

from menu.api_views import MenuApiView, DishApiView, MenuListPublicApiView, DishDetailPublicApiView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="eMenu API",
        default_version='v1',
        description="API for eMenu application",
        contact=openapi.Contact(email="michalmalara@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'public/menu', MenuListPublicApiView, basename='menu_public')
router.register(r'public/dish', DishDetailPublicApiView, basename='dish_public')

router.register(r'menu', MenuApiView, basename='menu')
router.register(r'dish', DishApiView, basename='dish')

urlpatterns = [
    path(r'', include(router.urls)),
    path('login/', obtain_auth_token, name='api_login'),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema_json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
]
