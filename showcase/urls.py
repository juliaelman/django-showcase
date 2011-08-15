from django.conf.urls.defaults import *
from showcase.models import Project

info_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
