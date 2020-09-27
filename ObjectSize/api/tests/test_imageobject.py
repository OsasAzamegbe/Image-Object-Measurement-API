from django.test import SimpleTestCase
from api.objectSizeScript import driver, decodeImage
import os
import base64


class TestImageObjectScript(SimpleTestCase):
    def setUp(self):
        #variables
        self.BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.FOLDER = os.path.join(self.BASE, 'testImages')
        self.NAME = 'example_01.png'
        self.REF = 0.955
       
        #open image and encode
        with open(os.path.join(self.FOLDER, self.NAME), 'rb') as image_file:
            self.image = base64.b64encode(image_file.read()).decode('utf-8')
            

    def test_driverscript(self):
        '''
        test ObjectSizeScript
        '''
        self.assertIs(type(self.image), str)

        decoded = decodeImage(self.image)

        #call driver
        sizes = driver(decoded, self.REF, self.NAME)

        # assert values
        self.assertEqual(len(sizes), 6)
        for i in range(6):
            self.assertIn('height', sizes[i])
            self.assertIs(type(sizes[i]['height']), float)
            self.assertIn('width', sizes[i])
            self.assertIs(type(sizes[i]['width']), float)

