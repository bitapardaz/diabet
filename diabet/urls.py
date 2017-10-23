from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.utils.translation import ugettext_lazy


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_profile/', include('user_profile.urls'))
]


admin.site.site_header = 'Diabetkadeh Management System'
admin.site.site_title = ugettext_lazy('Administrative Panel')
admin.site.index_title = ugettext_lazy('Operation Management')
