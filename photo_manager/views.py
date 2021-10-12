from django.http import HttpResponse
from django.shortcuts import render
from photo_manager.models import  Photos

# Create your views here.
def home(request):
    """
    This will render the home page and the images
    """
   
    return render(request,'base.html')

def photos(request):
     photos = Photos.objects.all()
     return render(request,'photo.html',{'images':photos})

# def view_photo(request,pk):
#     photo = Photos.get_image_by_id(pk)
#     return render(request,'photo.html',{'photo':photo})
    
def search_images(request):
    """This will return the 
    Args:
        request ([type]): [description]
        search_term ([type]): [description]
    """
    if 'image' in request.GET and request.GET['image']:
        search = request.GET.get("image")
        images = Photos.get_image_by_name(search)

        message = f"{search}"

        return render(request,'search.html',{"message":message,"images":images})

    else:
        message = "You have not searched for an image"
        return render(request,'search.html',{"message":message})



