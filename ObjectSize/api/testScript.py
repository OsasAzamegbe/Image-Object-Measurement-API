from objectSizeScript import decodeImage, driver
import base64

folder = 'testImages/'
name = 'example_01.png'
ref = 0.955

with open(folder + name, 'rb') as img_file:
    image = base64.b64encode(img_file.read()).decode('utf-8')

decoded = decodeImage(image)
print('decoded:', type(decoded))
sizes = driver(decoded, ref, name)
print(sizes)