from django.contrib import admin
from .models import Seller,Address,RegisteredSeller
# Register your models here.

admin.site.register(Seller)
admin.site.register(Address)
admin.site.register(RegisteredSeller)