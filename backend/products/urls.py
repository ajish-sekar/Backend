from django.urls import path,include
from rest_framework import routers
from .views import *
from rest_framework_swagger.views import get_swagger_view 


router = routers.DefaultRouter()
router.register(r'',ProductViewSet)

schema_view = get_swagger_view(title="API Name")

urlpatterns = [
    path('docs/',schema_view),
]

urlpatterns += router.urls 


