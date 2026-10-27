from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    # Дополнительно выводим текстовое имя автора вместо его числового ID
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'author_name', 'text', 'rating', 'created_at']
        # Поле автора сделаем необязательным при отправке с фронта, 
        # так как бэкэнд сам подставит текущего залогиненного юзера
        extra_kwargs = {'author': {'required': False}}