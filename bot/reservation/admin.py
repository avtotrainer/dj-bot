# admin.py

from django.contrib import admin
from .models import Person, PersonStatus, Role, BotSetting, Visit, Service, CompletedService, WorkSchedule

class BotSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class PersonStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'description')
    search_fields = ('status',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'contact_info', 'personal_number', 'iban')
    search_fields = ('name', 'contact_info', 'personal_number', 'iban')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price_per_hour')
    search_fields = ('name',)

class VisitAdmin(admin.ModelAdmin):
    list_display = ('client', 'specialist', 'visit_time', 'service', 'prepayment_made','visit_completed')
    list_filter = ('visit_time', 'service', 'prepayment_made', 'visit_completed')
    search_fields = ('client__name', 'specialist__name', 'service__name')

class CompletedServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'client', 'specialist', 'duration', 'payment')
    list_filter = ('service', 'client', 'specialist')
    search_fields = ('service__name', 'client__name', 'specialist__name')

class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('person', 'start_time', 'end_time', 'break_start_time', 'break_duration', 'work_days')
    search_fields = ('person__name',)
    list_filter = ('work_days',)
# Регистрация моделей с админ-классами
admin.site.register(BotSetting, BotSettingAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(PersonStatus, PersonStatusAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(CompletedService, CompletedServiceAdmin)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
