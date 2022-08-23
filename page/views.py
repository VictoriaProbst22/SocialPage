from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from page.apps import PageConfig
from .serializers import PageSerializer
from .models import Page


@api_view(['GET', 'POST'])
def page_list(request):

    if request.method == 'GET':
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =PageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'GET':
     serializer = PageSerializer(car);
     return Response(serializer.data)
    elif request.method =='PUT':
      serializer = PageSerializer(car, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
    elif request.method == 'DELETE':
        page.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
