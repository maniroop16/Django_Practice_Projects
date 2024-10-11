from django.db import models
from uuid import uuid4

# Create your models here.

# Creating a baseclass for adding generic attributes which are used to all the models
class Baseclass(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    product_added_date = models.DateField(auto_created=True)
    product_updated_date = models.DateField(auto_created=True)

    # This helps us to create Baseclass as Class not as Model
    class Meta:
        abstract = True

# We are inheriting Baseclass to get all the properties(attributes) from Baseclass
class Product(Baseclass):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)

class Productmetainformation(Baseclass):
    product_quantity = models.CharField(max_length=100, null=True, blank=True)
    product_measuring = models.CharField(max_length=100,choices=(("ml","ml"),('l','l'),('kg','kg')),null=True, blank=True)


class ProductImage(Baseclass):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product_image")
    ProductImage = models.ImageField(upload_to="Product_Images")