# test_interventions.py

from app import app
import unittest
import json


class TestCase(unittest.TestCase):
    def setup(self):
        # self.app = create_app(config_name="testing_interventions")
        self.interventions = {
            "int_id": 1,
            "title": "broken bridge in katanga",
            "description": "There has been a broken bridge for months in Katanga Wandegeya",
            "latitude": 3.145,
            "longitude": 1.124,
            "attachement": "image.jpg",
            "status": "pending"
        }
        self.update = {
            "int_id": 1,
            "title": "broken bridge in wandegeya",
            "description": "There is a broken bridge in Katanga Wandegeya",
            "latitude": 2.145,
            "longitude": 9.124,
            "attachement": "images.jpg",
            "status": "Under Investigation"
        }
        self.messed = {
            "int_id": 1,
            "description": "There has been a broken bridge for months in Katanga Wandegeya",
            "latitude": 3.145,
            "status": "pending"
        }
        self.client = app.test_client(self)

    def tearDown(self):
        self.interventions.clear()
        self.messed.clear()

    def test_route_indices(self):
        """ This should test for the start index's response """
        resp = self.client.get('api/v1/', content_type='application/json')
        self.assertTrue(b'Welcome to the iReporter' in resp.data)
        self.assertEqual(resp.status_code, 200)

    def test_post_method(self):
        """This method should test for inserting in new intervention"""
        respo = self.client.post(
            '/api/v1/interventions',
            data=json.dumps(self.interventions),
            content_type='application/json')
        self.assertTrue(b'Intervention added Successfully' in respo.data)
        self.assertEqual(respo.status_code, 201)

    def test_post_method_invalid_content_type_response(self):
        """ This tests for the response when content type other than json is
         entered """
        resp = self.client.post(
            '/api/v1/interventions',
            data=json.dumps(
                self.interventions),
            content_type='text/plain')
        self.assertTrue(b'Invalid Content Type' in resp.data)
        self.assertEqual(resp.status_code, 406)

    def test_post_method_missing_fields(self):
        resp = self.client.post(
            '/api/v1/interventions',
            data=json.dumps(
                self.messed),
            content_type='application/json')
        self.assertTrue(b'Missing field/s' in resp.data)
        self.assertEqual(resp.status_code, 400)

    def test_get_all_method(self):
        """This tests the get_all method of the interventions"""
        resp = self.client.get('/api/v1/interventions')
        self.assertEqual(resp.status_code, 200)

    def test_get_one_method_response(self):
        """This tests the get_one method response status code """
        resp = self.client.post(
            '/api/v1/interventions',
            data=json.dumps(self.interventions),
            content_type='application/json')

        resp = self.client.get('/api/v1/interventions/1')
        self.assertEqual(resp.status_code, 200)

    def test_get_one_method_index_error(self):
        resp = self.client.post(
            '/api/v1/interventions',
            data=json.dumps(self.interventions), content_type='application/json')

        resp = self.client.get('/api/v1/interventions/23')
        self.assertTrue(b'Intervention Not found!' in resp.data)
        self.assertEqual(resp.status_code, 404)

    def test_put_method_response(self):
        """ This tests the put method's response status code"""
        resp = self.client.post(
            '/api/v1/interventions',
            data=json.dumps(
                self.interventions),
            content_type='application/json')

        resp = self.client.put(
            '/api/v1/interventions/1',
            data=json.dumps(
                self.update),
            content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(b'Intervention Updated' in resp.data)


if __name__ == '__main__':
    unittest.main()
