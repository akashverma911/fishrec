from .views import FishViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FishViewSet)
urlpatterns = router.urls
