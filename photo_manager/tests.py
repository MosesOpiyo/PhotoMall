from django.test import TestCase
import datetime

from .models import Category,Photos,Location

class TestImage(TestCase):
    """This defines tests for the image behaviours
    Args:
        TestCase ([module]): [This is where we inherit the testing infrastructure]
    """
    def setUp(self):
        """This will run before every other test does"""
        self.location = Location(name = 'location1')
        self.location.save_location()

        self.category = Category(name = 'Cat1')
        self.category.save_category()

        self.name001 = Photos(name = 'name001', image="location", post_date = datetime.date(2017,5,12),description = 'This is a sample descrition',category = self.category,location = self.location)

    def test_instance(self):
        """
        This will check if an instance of the image class is being created
        """
        self.assertTrue(isinstance(self.name001,Photos))

    def test_save_image(self):
        """This checks if an image instance can be saved to the database
        """
        self.name001.save_photo()
        photos = Photos.objects.all()

        self.assertTrue(len(photos)>0)

    def test_add_category(self):
        """This will check if a category has been added to an image instance
        """
        self.assertTrue(self.name001.category == self.category)

    def test_add_location(self):
        """This will check if a location has been added to an image instance
        """
        self.assertTrue(self.name001.location == self.location)

    def test_get_image_by_id(self):
        """This will test if one can get an image by the id
        """
        self.name001.save_photo()
        photo = Photos.get_image_by_id(1)
        self.assertEqual(photo.pk,self.name001.pk)

    def test_delete_image(self):
        """
        This will test that an image can be deleted from the database given its id"""
        self.name001.save_photo()
        self.name001.delete_photo()

        photo = Photos.objects.all()
        self.assertTrue(len(photo) == 0)

    def test_update_image(self):
        """This will test the method to update an image's records
        """
        self.name001.save_photo()
        new_image_record = Photos(name = 'name002', image="location002", post_date = datetime.date(2000,4,10),description = 'This is another sample description',category = self.category,location = self.location)
        self.name001.update_photo(new_image_record)

        self.assertEqual(self.name001.name,'name002')

    


    def tearDown(self):
        Photos.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()



