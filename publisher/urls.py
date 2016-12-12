from django.conf.urls import url

from . import views

app_name = 'publisher'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'register/$', views.register, name='register'),
    url(r'success/$', views.success, name='success'),
    url(r'create_bulletin/$', views.create_bulletin, name='create'),
    url(r'alter_bulletin/$', views.alter_bulletin, name='alter_bulletin'),
    url(r'^delete/(?P<bulletin_id>\d+)/$', views.delete_bulletin, name='delete'),
    url(r'^batchUpload/$', views.batch_import_bulletin_by_excel, name='batchUpload'),
]