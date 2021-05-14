from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status


from .serializers import ImageSerializer
from .models import Image, UserPlan

import pathlib


@api_view(['PUT'])
@parser_classes([MultiPartParser])
def upload_image(request):
    acceptable_exts = ['png', 'jpg']

    if not 'file' in request.data.keys():
        return Response({'detail': "file must be provided"}, 
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if ('format' in request.data.keys() and 
        request.data.get('format').lower() in acceptable_exts):
        
            file_obj = request.data['file']
            
            if not pathlib.Path(str(file_obj)).suffix[1:] in acceptable_exts:
                return Response({'detail': 'wrong file format provided for this file'}, 
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            image = Image(user=request.user, image=file_obj)
            image.save()

            return Response({'detail': "uploaded"}, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class ImageView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        image = get_object_or_404(Image, pk=pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ImagesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        images = Image.objects.filter(user=request.user)

        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

