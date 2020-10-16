from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^general$',views.General_detailList.as_view()),
    url(r'^general/update/(?P<pk>[0-9]+)$',views.Update_detailList.as_view()),
    url(r'^general/delete/(?P<pk>[0-9]+)$',views.Delete_detailList.as_view()),
    url(r'^general/(?P<pk>[0-9]+)',views.GetbyID_detailList.as_view()),
]
