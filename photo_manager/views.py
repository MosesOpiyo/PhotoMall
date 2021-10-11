from django.http import HttpResponse
from django.shortcuts import render
from photo_manager.models import Image

# Create your views here.
def home(request):
    """
    This will render the home page and the images
    """
   
    return render(request,'base.html')

def images(request):
     images = Image.objects.all()
     return render(request,'photo.html',{'images':images})


