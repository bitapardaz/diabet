from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = [
    url(r'^send_sms/$',views.send_sms),
    url(r'^verify_code/$',views.verify_code),
    url(r'^register_customer_data/$',views.register_customer_data),
]

urlpatterns = format_suffix_patterns(urlpatterns)
