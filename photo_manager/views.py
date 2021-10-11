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
    
def search_images(request):
    """This will return the 
    Args:
        request ([type]): [description]
        search_term ([type]): [description]
    """
    if 'image' in request.GET and request.GET['image']:
        search = request.GET.get("image")
        images = Image.get_image_by_name(search)

        message = f"{search}"

        return render(request,'search.html',{"message":message,"images":images})

    else:
        message = "You have not searched for an image"
        return render(request,'search.html',{"message":message})



