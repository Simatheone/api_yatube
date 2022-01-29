from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from posts.models import Group, Post, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied()
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied()
        super(PostViewSet, self).perform_destroy(instance)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    pass


# api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
# api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
# api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, 
# редактируем или удаляем пост по id.
# api/v1/groups/ (GET): получаем список всех групп.
# api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.

# api/v1/posts/{post_id}/comments/ (GET, POST): получаем список 
# всех комментариев поста с id=post_id или создаём новый, указав id поста, 
# который хотим прокомментировать.

# api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): 
# получаем, редактируем или удаляем комментарий по id у поста с id=post_id.