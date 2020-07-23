from django.shortcuts import render
from .objectSizeScript import decodeImage, driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import cv2

# Create your views here.

@api_view(["POST"])
def measure_objects(request):
    """
    Return measurements for objects in received image file
    """    
    try:
        image_string = request.data["image"]
        _id = image_string[-10:]
        image = decodeImage(image_string)
        ref = 0.955
        driver(image, ref, _id)
        img = cv2.imread(f'./images/results/received_{_id}.jpg')
        response = {
            'image status': 'created',
            'name': f'received_{_id}'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    except e:
        print(e)
        response = {
            'error': "file wasn't saved successfully"
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    