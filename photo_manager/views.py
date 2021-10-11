from django.http import HttpResponse
from django.shortcuts import render
from ..photo_manager.models import Image

# Create your views here.
def welcome(request):
    return render(request,'base.html')

def my_photos(request):
    photos = Image.query.all
    return render(request, 'my_photos.html',image_list = photos)