from django.contrib import admin
from . models import Employee, TradePoint, Attendance


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    ordering = ['id']
    search_fields = ['name']


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'employee']
    ordering = ['id']
    search_fields = ['name', 'employee__name']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'trade_point', 'latitude', 'longitude']
    ordering = ['id']
    search_fields = ['trade_point__name', 'trade_point__employee__name']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
