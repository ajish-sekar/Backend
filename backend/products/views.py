from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

# Create your views here.
def product_list(request):
    # pass
    # products = Product.objects.all()
    # json_response = []
    # for product in products:
    #     json_response.append({
    #         "product_id" : product.product_id,
    #         "product_title":product.product_title,
    #         "product_price":product.product_price,
    #         "product_description":product.product_description,
    #         "product_category":product.product_category
    #     })
    # return JsonResponse(json_response,safe=False)
    pass

def product_detail(request):
    pass