from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet, basename='posts')
router_v1.register(r'v1/groups', GroupViewSet, basename='groups')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments'
                   )

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]
