from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CreateOrganizationViewSet, EventsViewSet

app_name = 'api'

router = DefaultRouter()
router.register('events', EventsViewSet, basename='events')
router.register(
    'organizations', CreateOrganizationViewSet, basename='organizations'
)

urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
