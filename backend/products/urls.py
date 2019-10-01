from django.urls import path
from .views import *


urlpatterns = [
    path("",product_list,name="products_list"),
    path("<int:pk>/",product_detail,name="product_details")
]

