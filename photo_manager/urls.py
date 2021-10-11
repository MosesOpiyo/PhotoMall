from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^myphotos',views.my_photos,name = 'My_ photos')
]