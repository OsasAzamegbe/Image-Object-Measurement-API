from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .objectSizeScript import driver, decodeImage

# Create your views here.

@api_view(["POST"])
def measure_objects(request, name, *args, **kwargs):
    """
    Return measurements for objects in received image file
    """    
    
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
          
    