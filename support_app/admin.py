from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


class AgentAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'name', 'surname', 'created_at']
    list_filter = ['name', 'surname', 'tg_id', 'created_at']
    list_editable = ['name', 'surname']
    search_fields = ['name', 'surname', 'tg_id']


class ContractAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'agency', 'agent', 'inn', 'code', 'status']
    list_filter = ['status']
    list_editable = ['project', 'agency', 'agent', 'inn', 'code', 'status']
    search_fields = ['inn', 'code']


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project', 'file', 'created_at']
    list_filter = ['name', 'created_at']
    list_editable = ['name', 'file']
    search_fields = ['name']


class AgencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'agent', 'created_at']
    list_filter = ['name', 'created_at']
    list_editable = ['name', 'agent']
    search_fields = ['name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'agent']
    list_filter = ['name', 'agent', 'created_at']
    list_editable = ['name', 'agent']
    search_fields = ['name']


admin.site.unregister(Group)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Contract, ContractAdmin)

admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'
