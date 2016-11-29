from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login, name='login'),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^alter/(?P<bulletin_id>)/$', views.alter_bulletin, name='alter'),
    url(r'^delete/(?P<bulletin_id>)/$', views.delete_bulletin, name='delete'),
    url(r'^create/$', views.create_bulletin, name='create'),

]