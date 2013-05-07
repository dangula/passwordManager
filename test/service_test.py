import os
import service
import unittest
import tempfile
import json


class RESTServiceTest(unittest.TestCase):
    
    def setUp(self):
        service.app.config['STORE_DB'] = tempfile.mkstemp()
        service.app.config['TESTING'] = True
        self.client = service.app.test_client()
        self.app = service.app
    
    def tearDown(self):
        pass

        
    def test_testServiceUp(self):
        with self.app.test_request_context("/"):
            self.app.preprocess_request()
            request = self.client.get("/")
            self.assertEquals("200 OK", request.status)
            self.assertEquals(200, request.status_code)
            self.assertEquals("application/json", request.mimetype)
            data =json.loads(request.data)
            self.assertEquals(1, len(data))
            self.assertEqual('Service Up',data['status'])
