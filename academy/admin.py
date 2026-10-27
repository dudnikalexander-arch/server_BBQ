from django.contrib import admin
from .models import BlogPost  # Импортируем нашу модель отзывов

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # Какие поля отображать в виде таблицы
    list_display = ('author', 'rating', 'created_at')
    
    # По какому полю делать фильтрацию (справа появится панель фильтров)
    list_filter = ('rating', 'created_at')
    
    # По каким полям вести поиск вверху админки
    search_fields = ('author__username', 'text')