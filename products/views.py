import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Products
from products import serializers

@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def product_detail(request, pk):
    try:
        products = Products.objects.get(pk=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)