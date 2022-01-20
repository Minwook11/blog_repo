import json
import unittest

from django.test import Client, TestCase

client = Client(HTTP_USER_AGENT='TestCase') # Log 기록 파트의 User-Agent 데이터를 위한 추가사항

class UnitTest(TestCase):
    test_case_data = {
        'name' : 'test_case',
        'code' : 0
    }
    wrong_name_key = {
        'neme' : 'test_case',
        'code' : 0
    }

    def test_CaseView_POST_SUCCESS(self):
        response = client.post('/base/case', json.dumps(self.test_case_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_caseView_GET_SUCCESS(self):
        client.post('/base/case', json.dumps(self.test_case_data), content_type = 'application/json/json')

        response = client.get('/base/case', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_CaseView_POST_WRONG_DATA_KEY_NAME(self):

        response = client.post('/base/case', json.dumps(self.wrong_name_key), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
