from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Admin for models.Employee."""

    exclude = ('added', )
    readonly_fields = ('added', )
    list_display = ('name', 'email', 'department', 'added')
