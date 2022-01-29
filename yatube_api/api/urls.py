from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
#router_v1.register(r'posts\/\d+\/comment\/\d+\/', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]

# api/v1/posts/{post_id}/comments/ (GET, POST): 
# получаем список всех комментариев поста с id=post_id или создаём новый, 
# указав id поста, который хотим прокомментировать.

# api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): 
# получаем, редактируем или удаляем комментарий по id у поста с id=post_id.