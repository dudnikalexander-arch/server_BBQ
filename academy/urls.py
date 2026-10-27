from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # Встроенный эндпоинт входа от Django
from .views import BlogPostViewSet, register_user

router = DefaultRouter()
router.register(r'reviews', BlogPostViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', register_user, name='register'),  # Ссылка для Регистрации
    path('auth/login/', obtain_auth_token, name='login'),    # Ссылка для Входа (принимает username/password, возвращает token)
]