from django.test import TestCase

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeSerializerTestCase(TestCase): #noqa
    REQUIRED_FIELDS = ('name', 'email', 'department')
    TEST_DATA = {
        'name': 'Guilherme Munarolo',
        'email': 'guimunarolo@hotmail.com',
        'department': 'Software Engineering',
    }

    def test_required_fields(self): #noqa
        for field in self.REQUIRED_FIELDS:
            data = {k: v for k, v in self.TEST_DATA.items() if k != field}
            serializer = EmployeeSerializer(data=data)
            self.assertFalse(serializer.is_valid())
            self.assertIn(field, serializer.errors)

    def test_create(self): #noqa
        data = self.TEST_DATA.copy()
        serializer = EmployeeSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertTrue(Employee.objects.count() is 1)
