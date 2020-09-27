from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.objectSizeScript import driver, decodeImage

# Create your views here.

@api_view(["POST"])
def measure_objects(request, *args, **kwargs):
    """
    Return measurements for objects in received image file
    """    
    try:
        image_string = request.data["image"]
        name = request.data["name"]
        ref = request.data["reference size"]
        image = decodeImage(image_string)
        ref = 0.955
        sizes = driver(image, ref, name)
        response = {
            'created': True,
            'name': name,
            'sizes': sizes
        }
    except:
        response = {
            'created': False,
            'name': "",
            'sizes': []
        }

    return Response(response, status=status.HTTP_200_OK)
          
    