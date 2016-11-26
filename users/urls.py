from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^hospital/$',views.hospital,name='hospital'),
    url(r'^test/$',views.test,name='test'),
    url(r'^doctor/$',views.doctor,name='doctor'),
    url(r'^reservation/$',views.reservation,name='reservation'),
]