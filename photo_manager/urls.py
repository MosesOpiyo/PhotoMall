from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'Home'),
    url('^images$',views.images,name='images'),
    url('^search$',views.search_images,name='search_images')
   
   
]