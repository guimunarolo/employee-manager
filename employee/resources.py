from rest_framework import generics, mixins

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeResource(mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.DestroyModelMixin, generics.GenericAPIView):
    """Responsible to list, create and delete Employee obj."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        """List all Employee."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create Employee."""
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete Employee."""
        return self.destroy(request, *args, **kwargs)
