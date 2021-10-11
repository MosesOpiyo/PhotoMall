from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'Home'),
    url('^myphotos$',views.photos,name='myphotos'),
    url('^search$',views.search_images,name='search_photos')
   
   
]