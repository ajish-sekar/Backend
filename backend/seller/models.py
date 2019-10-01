from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    line_one = models.CharField(max_length=200)
    line_two = models.CharField(max_length=200,null=True,blank=True)
    landmark = models.CharField(max_length=200,null=True,blank=True)
    district = models.CharField(max_length=200)
    state    = models.CharField(max_length=200)
    pincode  = models.IntegerField(validators=[MinValueValidator(100000),MaxValueValidator(999999)])

    def __str__(self):
        full_address = f"{self.line_one},{self.line_two},{self.district},{self.state},{self.pincode}"
        return full_address


class Seller(models.Model):
    seller_account = models.PositiveIntegerField(primary_key=True)
    seller_name = models.CharField(max_length=200)
    seller_contact = PhoneNumberField(null=False,blank=False,unique=True)
    seller_address = models.ForeignKey(Address,on_delete=models.CASCADE)

    def __str__(self):
        seller_details = f"{self.seller_name} - {self.seller_account}"
        return seller_details

class RegisteredSeller(models.Model):
    seller_account = models.PositiveIntegerField(primary_key=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        seller_details = f"{self.seller_account}"
        return seller_details



