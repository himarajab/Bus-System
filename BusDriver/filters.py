import django_filters
from django_filters import CharFilter
from .models import Bus


class BusFilter(django_filters.FilterSet):
    destination = CharFilter(field_name='destination' , lookup_expr='icontains')
    origin = CharFilter(field_name='origin' , lookup_expr='icontains')

    class Meta:
        model = Bus
        fields = ['destination','origin']
