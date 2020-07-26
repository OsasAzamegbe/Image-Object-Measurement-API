from django.shortcuts import render
from .objectSizeScript import decodeImage, driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import cv2

# Create your views here.

@api_view(["POST"])
def measure_objects(request, name, *args, **kwargs):
    """
    Return measurements for objects in received image file
    """    
    try:
        image_string = request.data["image"]
        image = decodeImage(image_string)
        ref = 0.955
        sizes = driver(image, ref, name)
        # img = cv2.imread(f'./images/results/received_{name}.jpg')
        response = {
            'image status': 'created',
            'name': f'received_{name}',
        }
        try:
            response['sizes'] = sizes[1]
        except IndexError:
            response['sizes'] = sizes[0]
        finally:
            return Response(response, status=status.HTTP_200_OK)
    except e:
        print(e)
        response = {
            'error': "file wasn't processed"
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    