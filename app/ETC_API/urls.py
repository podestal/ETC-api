from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('topics', views.TopicViewSet)
router.register('posts', views.PostViewSet)
router.register('sections', views.SectionViewSet)
router.register('content', views.TextContentViewSet)

urlpatterns = router.urls