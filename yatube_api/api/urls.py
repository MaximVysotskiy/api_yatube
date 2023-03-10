from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register('api/v1/groups', GroupViewSet, basename='groups')
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
