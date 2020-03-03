import xadmin

from apps.scoreline.models import Batch, ProvinceScore, ProfessionalScore


class BatchAdmin(object):
    list_display = ['province', 'name']
    search_fields = ['province', 'name']
    list_filter = ['province', 'name']
    list_editable = ['name']


class ProvinceScoreAdmin(object):
    list_display = ['province', 'name', 'batch', 'score']
    search_fields = ['province', 'name', 'batch', 'score']
    list_filter = ['province', 'name', 'batch', 'score']
    list_editable = ['name', 'score']


class ProfessionalScoreAdmin(object):
    list_display = ['year', 'school', 'professional', 'province', 'level', 'batch', 'highest', 'lowest', 'average', 'place']
    search_fields = ['year', 'school', 'professional', 'province', 'level', 'batch', 'highest', 'lowest', 'average', 'place']
    list_filter = ['year', 'school', 'professional', 'province', 'level', 'batch', 'highest', 'lowest', 'average', 'place']
    list_editable = ['highest', 'lowest', 'average', 'place']


xadmin.site.register(Batch, BatchAdmin)
xadmin.site.register(ProvinceScore, ProvinceScoreAdmin)
xadmin.site.register(ProfessionalScore, ProfessionalScoreAdmin)
