from django.urls import path 
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Testing API",
      default_version='v1',
      description="Test API for Swagger UI",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('member/', views.members, name='members'),
    path('sign-up/', views.create_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', views.logout_user, name='logout'),
    path('members/', views.members, name='members'),
#      path('users/<int:pk>/', views.user_detail, name='user-detail'),
#     path('products/', views.get_products, name='products'),
#    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    #swagger-UI
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
