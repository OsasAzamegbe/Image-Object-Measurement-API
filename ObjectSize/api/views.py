from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.objectSizeScript import driver, decodeImage

# Create your views here.

@api_view(["POST"])
def measure_objects(request, *args, **kwargs):
    """
    Return sizes for objects in received image file.

    The request body should contain "image", "name" and "reference size" fields in json format as shown below.

    The POST request should be sent to:
    
        https://imgobjectmeasurement.herokuapp.com/api/v1/measure/


    A sample request body is shown below:



            {   
                'image': 'iVBORw0KGgoAAAANSUhEUgAAAyAAAAJYCAYAAACadoJwAAAg
                                .
                                .
                                .
                        (Base64-encoded String)
                                .
                                .
                                .
                        AAMAnLkNKFEAZ5MAAAAASUVORK5CYII=',
                'name': 'example_01.png',
                'reference size': 0.955
            }


    A sample response for the above request is shown below:



            {
                'created': True,
                'name': 'example_01.png',
                'sizes': [
                    {
                        'height': 0.92,
                        'width': 0.95
                    },
                    {
                        'height': 1.99,
                        'width': 3.46
                    },
                    {
                        'height': 0.92,
                        'width': 0.94
                    },
                    {
                        'height': 2.54,
                        'width': 2.27
                    },
                    {
                        'height': 2.63,
                        'width': 2.28
                    },
                    {
                        'height': 0.82,
                        'width': 0.82
                    }
                ]
            }

            
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
        status = 201
    except:
        response = {
            'created': False,
            'name': "",
            'sizes': []
        }
        status = 500
    return Response(response, status=status)
          
    