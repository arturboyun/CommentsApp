from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet


router = DefaultRouter()
router.register('comments', CommentViewSet, 'comments_view')

urlpatterns = router.urls
