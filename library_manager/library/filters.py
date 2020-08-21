import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class BookFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['author','genre']

class OrderFilter(django_filters.FilterSet):
  
    class Meta:
        model = BookOrder
        fields = '__all__'
        exclude = ['member','date_created']

