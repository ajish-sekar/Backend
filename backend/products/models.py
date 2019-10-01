from django.db import models
from seller.models import Seller

# Create your models here.
class Product(models.Model):
    CATEGORIES = (
        ("HC","Handicraft"),
        ("FD","Food"),
        ("BE","Beauty"),
        ("CL","Clothing"),
        ("FJ","Fashion Jewellery"),
        ("HG","Home and Garden"),
    )
    product_id = models.BigAutoField(primary_key=True)
    product_title = models.CharField(max_length=200)
    product_category = models.CharField(max_length=2,choices=CATEGORIES)
    product_price = models.FloatField()
    product_description = models.CharField(max_length=500)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)

    def __str__(self):
        product_details = f"{self.product_title}, {self.product_price}₹, {self.product_category}"
        return product_details
