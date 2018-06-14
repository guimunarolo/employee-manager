from django.db import models


class Employee(models.Model):
    """Responsible to store Employees data."""

    name = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.CharField(max_length=80)
    added = models.DateTimeField(auto_now_add=True)

    class Meta: #noqa
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self): #noqa
        return f'{self.name} <{self.email}> ({self.email})'
