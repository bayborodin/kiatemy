from .views import AccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", AccountViewSet, basename="accounts")

urlpatterns = router.urls
