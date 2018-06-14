from django.urls import re_path

from rest_framework.urlpatterns import format_suffix_patterns

from .resources import EmployeeResource


urlpatterns = [
    re_path(r'^(?P<pk>[0-9])?$', EmployeeResource.as_view(),
            name='employee_resource'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
