from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from nasa_picture.apps import NasaPictureConfig
from .serializers import PictureSerializer
from .models import Picture


@api_view(['GET', 'POST'])
def picture_list(request):

    if request.method == 'GET':
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =PictureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def picture_detail(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    if request.method == 'GET':
     serializer = PictureSerializer(picture);
     return Response(serializer.data)
    elif request.method =='PUT':
      serializer = PictureSerializer(picture, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
    elif request.method == 'DELETE':
        picture.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
