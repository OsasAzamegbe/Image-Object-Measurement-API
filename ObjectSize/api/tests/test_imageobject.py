from django.test import TestCase, SimpleTestCase
from unittest import TestCase as T
from api.objectSizeScript import driver, decodeImage
import os
import base64


class TestImageObjectScript(T):
    def setUp(self):
        #variables
        self.BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.FOLDER = os.path.join(self.BASE, 'testImages')
        self.NAME = 'example_01.png'
        self.REF = 0.955
       

    def test_driverscript(self):
        '''
        test ObjectSizeScript
        '''
        #open image and encode
        # with open(os.path.join(self.FOLDER, self.NAME), 'rb') as image_file:
        #     image = base64.b64encode(image_file.read()).decode('utf-8')
        folder = 'testImages/'
        name = 'example_01.png'
        ref = 0.955

        with open(folder + name, 'rb') as img_file:
            image = base64.b64encode(img_file.read()).decode('utf-8')

        self.assertIs(type(image), str)

        decoded = decodeImage(image)

        #call driver
        sizes = driver(decoded, self.REF, self.NAME)

        # assert values
        self.assertEqual(len(sizes), 6)
        for i in range(6):
            self.assertIn('height', sizes[i])
            self.assertIs(type(sizes[i]['height']), float)
            self.assertIn('width', sizes[i])
            self.assertIs(type(sizes[i]['width']), float)

