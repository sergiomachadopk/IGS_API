from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','name','email','department')
    list_display_links=('id','name')
    search_fields=('name','department',)
    list_per_page = 25

admin.site.register(Employee, EmployeeAdmin)
