from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.objectSizeScript import driver, decodeImage

# Create your views here.

@api_view(["POST"])
def measure_objects(request, *args, **kwargs):
    """
    Return sizes for objects in received image file.

    Request body should contain "image" in json format for the required shipping rates to be calculated.

    The POST request should be sent to:
    
        https://image-object-measurement.herokuapp.com/api/v1/measure/


    A sample request body is shown below:



            {   
                'image': 'nJskUDUkGvZFlycNnWKGoxIdjMHO7WD9PVTYWlo8L4iGMjkSg4vsfbnE8kL7k/+uQuh08dmeGeEGVp+20APVfUGDAhJp9pwy6halyNzRVDS2+g7kuiJ4EJ7K3377Dk1aKvfb/cvbF3mDVXtyQ2jsaViBMx/V33//x9uXt//83x/JvDAxC5J9Ql14LSa+bg2F89yEIY1D36ZoVDrPhtwpT6fr7fb3z/e/M7XKKWI5Ezp4d/Rg2XLMDF/tgnl0SlpWTNVut02H8Vl/nM7rtsOigaUTfj56EjDLQSrxA3tzr6N8/
                ...(Base64-encoded String)...
                Uo7bgYMZIav0TJS9CKf0ae4bSlFdZZZ6Krx6MScdgJ5IBS6hmMCGxM6Kvoq0mJjP7m4KXloc77pp6YrMjBn5cRZRIoLhdxo1GV2iAYgZDsbCJfX/jthjdTIYpi1Hp6qmRYttjXOMAhUy21fzMvy/AAMAnLkNKFEAZ5MAAAAASUVORK5CYII=',
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
    except:
        response = {
            'created': False,
            'name': "",
            'sizes': []
        }

    return Response(response, status=status.HTTP_200_OK)
          
    