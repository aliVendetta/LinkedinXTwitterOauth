
from rest_framework.routers import DefaultRouter
from .views import LinkedInAuthViewSet, TwitterAuthViewSet

router = DefaultRouter()
router.register(r'complete/linkedin', LinkedInAuthViewSet, basename='linkedin-auth')
router.register(r'complete/twitter', TwitterAuthViewSet, basename='twitter-auth')
urlpatterns = router.urls
