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

def single_photo(request, pk):
    photo = photos.get_image_by_id(pk)
    return render(request, 'single_photo.html', {'photo':photo})

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
        search_term = request.GET.get("photo")
        searched_photos = photos.search_by_category(search_term)
        
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"photos":searched_photos})

    else:
        message = "You have not searched for an image"
        return render(request,'search.html',{"message":message})

def single_image(request,pk):
    image = Photos.objects.get(pk = pk)

    return render(request,'image.html',{"image":image})



