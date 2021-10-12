from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
# Create your models here.
class Category(models.Model):
    """
    This defines the category table and all its contents and behaviours
    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=50)

    def save_category(self):
        """
        This adds a category to the database
        """
        self.save()

    def delete_category(self):
        """
        This removes a category from the database
        """
        self.delete()

    def update_category(self,new):
        """This will update a category
        Args:
            new ([type]): [description]
        """
        self.name = new.name
        self.save()

    def __str__(self):
        return self.name

class Location(models.Model):
    """
    This defines the location table and all its contents and behaviours
    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=100)

    def save_location(self):
        """
        This adds a category to the database
        """
        self.save()

    def delete_location(self):
        """
        This removes a category from the database
        """
        self.delete()

    def update_location(self,new):
        """
        This will update a category
        Args:
            new ([type]): [description]
        """
        self.name = new.name
        self.save()

    def __str__(self):
        return self.name

class Photos(models.Model):
     """
     This defines the image table and all its contents and behaviours
     """
     name = models.CharField(max_length=100)
     image = models.ImageField(upload_to='articles/')
     description = models.TextField(blank=True)
     post_date = models.DateField(auto_now_add=True)
     category = models.ForeignKey(Category,on_delete=models.CASCADE)
     location = models.ForeignKey(Location,on_delete=models.CASCADE)

     def __str__(self):
        return self.name


     def get_image_by_id(id):
        photo = Photos.objects.get(pk = id)
        return photo


     def save_photo(self):
         self.save()

     def delete_photo(self):
        """This deletes the image from the database using its pk
        Args:
            id ([type]): [description]
        """
        self.delete()
    
     def update_photo(self,new):
        """This method will update a record of an image
        """
        self.name = new.name
        self.image = new.image
        self.description = new.description
        self.post_date = new.post_date
        self.category = new.category
        self.location = new.location
        self.save()

     def get_image_by_category(pk):
         photo = Category.objects.get(pk = id)
         return photo

    
