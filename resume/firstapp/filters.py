import django_filters
from django_filters import DateFilter, CharFilter
from django import forms

from .models import *

class ResumeFilter(django_filters.FilterSet):
    start_date= DateFilter(field_name="dob", lookup_expr='gte')
    end_date= DateFilter(field_name="dob", lookup_expr='lte')
    name= CharFilter(field_name="name", lookup_expr='icontains')
    class Meta:
        model = Resume
        fields = [ 'name','gender', 'locality','city','pin','state','job_city',  'mobile','email' ]
        exclude = ('dob','profile_image','my_file')
