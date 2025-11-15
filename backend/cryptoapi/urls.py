from django.contrib import admin
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def crypto_prices(request):
    data = [
        {"name": "Bitcoin", "value": "35000"},
        {"name": "Ethereum", "value": "2000"},
    
    ]
    return Response(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prices/', crypto_prices, name='crypto_prices'),
]
