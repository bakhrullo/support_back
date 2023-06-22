from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


class AgentAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'name', 'uniq', 'show_agency', 'created_at']
    list_filter = ['tg_id', 'name', 'tg_id', 'created_at']
    list_editable = ['name', 'uniq']
    search_fields = ['name', 'uniq', 'tg_id']


class ContractAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'agent', 'inn', 'code', 'status']
    list_filter = ['id', 'status', 'created_at', 'updated_at']
    list_editable = ['status']
    search_fields = ['inn', 'code']


class AgencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uniq', 'created_at']
    list_filter = ['id', 'name']
    list_editable = ['name', 'uniq']
    search_fields = ['name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uniq', 'agency', 'file', 'created_at']
    list_filter = ['id', 'name']
    list_editable = ['name', 'uniq', 'agency']
    search_fields = ['name', 'uniq']


admin.site.unregister(Group)
admin.site.register(Agency, AgencyAdmin)
#admin.site.register(Counter)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contract, ContractAdmin)

admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'
