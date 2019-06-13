from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^details/$', views.news_details, name='details'),
    url(r'^registration/$', views.registration, name='add'),
    url(r'^year/<int:year>', views.news_years, name='news'),
    url(r'^addUser/$', views.addUser, name='addUser'),
    url(r'^modelform/$', views.modelformview, name='addModelform'),
    url(r'^addmodelformdata/$', views.addModeldata, name='insertdata'),
    url(r'^detect/$', views.detect, name='detect'),
]