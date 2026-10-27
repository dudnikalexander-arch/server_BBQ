from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('academy.urls')), # Все запросы к блогу будут начинаться с /api/reviews/
]