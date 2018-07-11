from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^didslist/$', views.didList, name='didsList'),
    url(r'^SDAslist/$', views.SDAList, name='SDAList'),
    url(r'^customer/(?P<name>[\w\-]+)/$', views.getinfoCustomer, name='infoCustomer')
]