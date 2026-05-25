from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

# Создаем роутер
router = DefaultRouter()

# Регистрируем наши вьюсеты
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

# Регистрируем вьюсет комментариев. 
# Обрати внимание на регулярное выражение: оно ловит id поста из ссылки
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

# Подключаем сгенерированные роутером пути в urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
