from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^checkLogin/$', views.checkLogin, name='checkLogin'),
    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^logOut/$', views.logout, name='logOut'),
    url(r'^didslist/$', views.didList, name='didsList'),
    url(r'^SDAslist/$', views.SDAList, name='SDAList'),
    url(r'^customer/(?P<name>[\w\-]+)/$', views.getinfoCustomer, name='infoCustomer'),
    url(r'^Account/(?P<i_account>[0-9]+)/$', views.getAccountInfo, name='infoAccount'),
    url(r'^accueil/$', views.accueil, name='accueil'),
    url(r'^Download/$', views.syncronisation, name='getAllData'),
    url(r'^CustomersList/$', views.CustomersList, name='CustomersList'),
    url(r'^AccountsList/$', views.AccountsList, name='AccountsList'),
    url(r'^VendorsList/$', views.VendorsList, name='VendorsList'),
    url(r'^Syncronisation/$', views.syncronisation, name='syncroDB')

]