from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.home,name = 'Home'),
    path('myphotos/',views.photos,name='myphotos'),
    path('search/',views.search_images,name='search_photos')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)