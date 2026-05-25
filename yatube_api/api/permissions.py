from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Если запрос безопасный (GET) или пользователь авторизован — пускаем
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Безопасные методы (GET, HEAD, OPTIONS) разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменять/удалять может только автор
        return obj.author == request.user
