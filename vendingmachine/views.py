from django.http import JsonResponse
from .models import vending_machine
from .serializers import itemsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def item_list(request, format = None):

    if request.method == 'GET':
        items = vending_machine.objects.all()
        serializer = itemsSerializer(items, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = itemsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def items_detail(request, id, format = None):

    try:
        items = vending_machine.objects.get(pk=id)
    except vending_machine.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = itemsSerializer(items)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = itemsSerializer(items, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        items.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


