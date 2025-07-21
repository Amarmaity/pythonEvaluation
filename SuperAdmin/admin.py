from django.contrib import admin

from . models import Master

# Register your models here.
@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','emp_id', 'user_type', 'user_role']
    search_fields = ['id', 'name', 'email']
