from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Responsible to validate and represent models.Employee."""

    class Meta: #noqa
        model = Employee
        fields = ('id', 'name', 'email', 'department', 'added')
        read_only_fields = ('added', )
