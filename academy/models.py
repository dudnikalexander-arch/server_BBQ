from django.db import models
from django.contrib.auth.models import User # Импортируем встроенных пользователей Django

class BlogPost(models.Model):
    # Связываем отзыв с пользователем. Если пользователя удалят, его отзывы тоже удалятся (CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    
    # Текст отзыва/комментария
    text = models.TextField(verbose_name="Текст отзыва")
    
    # Оценка (количество звёзд от 1 до 5)
    rating = models.IntegerField(default=5, verbose_name="Количество звёзд")
    
    # Автоматическая дата создания отзыва
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв Академии BBQ"
        verbose_name_plural = "Отзывы Академии BBQ"
        ordering = ['-created_at'] # Свежие отзывы всегда будут отображаться сверху

    def __str__(self):
        return f"Отзыв от {self.author.username} | Оценка: {self.rating} ⭐"