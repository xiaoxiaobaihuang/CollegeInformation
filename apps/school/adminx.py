import xadmin
from apps.school.models import School, AdmissionsCategory, College, Professional


class SchoolAdmin(object):
    list_display = ['name', 'province', 'heat_rank']
    search_fields = ['name', 'province', 'city']
    list_filter = ['name', 'province', 'city']
    list_editable = ['heat_rank']


class AdmissionsCategoryAdmin(object):
    list_display = ['school', 'name']
    search_fields = ['school', 'name']
    list_filter = ['school', 'name']
    list_editable = ['name']


class CollegeAdmin(object):
    list_display = ['school', 'name']
    search_fields = ['school', 'name']
    list_filter = ['school', 'name']
    list_editable = ['name']


class ProfessionalAdmin(object):
    list_display = ['school', 'college', 'name']
    search_fields = ['school', 'college', 'name']
    list_filter = ['school', 'college', 'name']
    list_editable = ['name']


xadmin.site.register(School, SchoolAdmin)
xadmin.site.register(AdmissionsCategory, AdmissionsCategoryAdmin)
xadmin.site.register(College, CollegeAdmin)
xadmin.site.register(Professional, ProfessionalAdmin)
