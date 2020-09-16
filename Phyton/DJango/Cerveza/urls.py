from django.conf.urls import url
from Cerveza.views import index, cerveza_list, cerveza_detail

urlpatterns = [
    url('^$',index,name='index'),
    url('^list/$',cerveza_list,name='cerveza_list'),
    url('^detail=(?P<pk>\d+)$',cerveza_detail,name='cerveza_detail'),
]

