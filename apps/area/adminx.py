import xadmin
from apps.area.models import Province, City


class GlobalSetting(object):
    site_title = "高校信息库"
    site_footer = "STARK 编程营"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class ProvinceAdmin(object):
    list_display = ['name', 'add_time']


class CityAdmin(object):
    list_display = ['province', 'name']
    search_fields = ['province', 'name']
    list_filter = ['province', 'name']
    list_editable = ['name']


xadmin.site.register(Province, ProvinceAdmin)
xadmin.site.register(City, CityAdmin)


xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
