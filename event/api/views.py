from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.response import Response

from .filters import EventSearchFilter
from .mixins import CreateViewSet, CreateRetrieveListViewSet
from .pagination import SixPagination
from .serializers import (
    OrganizationSerializer,
    EventCreateSerializer,
    EventReturnedViewSerializer,
    EventViewSerializer
)
from events.models import Organization, Event


class CreateOrganizationViewSet(CreateViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class EventsViewSet(CreateRetrieveListViewSet):
    queryset = Event.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    pagination_class = SixPagination
    filterset_class = EventSearchFilter
    search_fields = ('title', )
    ordering_fields = ('date', )

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return EventViewSerializer
        return EventCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        event = Event.objects.get(title=request.data['title'])
        serializer = EventReturnedViewSerializer(
            instance=event, context={"request": request}
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
