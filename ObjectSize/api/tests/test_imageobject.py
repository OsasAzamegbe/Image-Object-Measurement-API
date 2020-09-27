from django.test import TestCase
from rest_framework import status
from api.objectSizeScript import driver, decodeImage
import os
import base64


class TestImageObjectScript(TestCase):
    def setUp(self):
        #variables
        self.BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.FOLDER = os.path.join(self.BASE, 'testImages')
        self.NAME = 'example_01.png'
        self.REF = 0.955

        self.ENDPOINT = f'/api/v1/measure/'
        self.CONTENT_TYPE = 'application/json'
       
        #open image and encode
        with open(os.path.join(self.FOLDER, self.NAME), 'rb') as image_file:
            self.image = base64.b64encode(image_file.read()).decode('utf-8')

        self.REQUEST_BODY = {
            "image": self.image,
            "name": self.NAME,
            "reference size": self.REF
        }


    def test_driverscript(self):
        '''
        test ObjectSizeScript
        '''
        self.assertIs(type(self.image), str)

        decoded = decodeImage(self.image)

        #call driver
        sizes = driver(decoded, self.REF, self.NAME)

        # assert values
        self.assertTrue(sizes)
        
        for size in sizes:
            self.assertIn('height', size)
            self.assertIs(type(size['height']), float)
            self.assertIn('width', size)
            self.assertIs(type(size['width']), float)


    def test_API_endpoint(self):
        response = self.client.post(self.ENDPOINT, data=self.REQUEST_BODY, content_type=self.CONTENT_TYPE)
        response_json = response.json()

        # assert values
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('created', response_json)
        self.assertIn('name', response_json)
        self.assertIn('sizes', response_json)

        self.assertTrue(response_json['created'])
        self.assertTrue(response_json['name'])
        self.assertTrue(response_json['sizes'])

        self.assertIs(type(response_json['created']), bool)
        self.assertIs(type(response_json['sizes']), list)
        self.assertIs(type(response_json['name']), str)

        for size in response_json['sizes']:
            self.assertIn('height', size)
            self.assertIs(type(size['height']), float)
            self.assertIn('width', size)
            self.assertIs(type(size['width']), float)
