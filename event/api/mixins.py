from rest_framework import viewsets
from rest_framework.mixins import (
    CreateModelMixin, RetrieveModelMixin, ListModelMixin
)


class CreateRetrieveListViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    viewsets.GenericViewSet
):
    pass


class CreateViewSet(CreateModelMixin, viewsets.GenericViewSet):
    pass
