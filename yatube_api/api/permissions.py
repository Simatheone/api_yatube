from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Классовый permission.
    который проверяет является ли юзер автором поста/коммента и т.д.,
    и какой метод запроса к эндпоинту.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user and request.method in SAFE_METHODS
