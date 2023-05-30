from django_filters.rest_framework import FilterSet
from django_filters.rest_framework.filters import DateFromToRangeFilter

from events.models import Event


class EventSearchFilter(FilterSet):
    date = DateFromToRangeFilter()

    class Meta:
        model = Event
        fields = ('date', )
