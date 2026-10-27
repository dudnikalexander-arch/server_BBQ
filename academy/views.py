from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # Настройка прав: Читать отзывы могут ВСЕ, а создавать — только залогиненные
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # Сервер автоматически привязывает текущего юзера к отзыву при сохранении
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])  # Регистрация открыта для всех
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password:
        return Response({'error': 'Логин и пароль обязательны'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Пользователь с таким логином уже существует'}, status=status.HTTP_400_BAD_REQUEST)

    # Создаем пользователя с безопасным хэшированием пароля в базе
    user = User.objects.create_user(username=username, password=password, email=email)
    
    # Сразу генерируем для него токен-ключ, чтобы React мог автоматически его авторизовать
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'message': 'Регистрация успешна!',
        'token': token.key,
        'username': user.username
    }, status=status.HTTP_201_CREATED)