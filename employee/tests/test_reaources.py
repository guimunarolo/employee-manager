from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee


class EmployeeResoureTests(APITestCase):# noqa
    REQUIRED_FIELDS = ('name', 'email', 'department')
    TEST_URL = reverse('employee_resource')
    TEST_DATA = {
        'name': 'Guilherme Munarolo',
        'email': 'guimunarolo@hotmail.com',
        'department': 'Software Engineering',
    }

    def test_created(self):
        """Test create employee."""
        data = self.TEST_DATA.copy()
        response = self.client.post(self.TEST_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)

    def test_create_bad_request(self):
        """Test create without required field."""
        for field in self.REQUIRED_FIELDS:
            data = {k: v for k, v in self.TEST_DATA.items() if k != field}
            response = self.client.post(self.TEST_URL, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list(self):
        """Test list employees."""
        data = self.TEST_DATA.copy()
        Employee.objects.create(**data)
        response = self.client.get(self.TEST_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_delete(self):
        """Test delete employee."""
        data = self.TEST_DATA.copy()
        employee = Employee.objects.create(**data)

        url = '{}{}'.format(self.TEST_URL, employee.id)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_delete_not_found(self):
        """Test delete not found."""
        url = '{}{}'.format(self.TEST_URL, 123)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_not_allowed_methods(self):
        """Test put, patch."""
        response = self.client.put(self.TEST_URL, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.TEST_URL, {}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
