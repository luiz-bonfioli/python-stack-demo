import uuid

from tests.common.base import BaseTestCase


class TestAlertController(BaseTestCase):

    def test_get_alerts_by_sensor_id(self):
        sensor_id = uuid.uuid4()
        response = self.client.get(f'/v1/alerts/{str(sensor_id)}', headers={'x-user-id': 'test'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.__alerts_response(str(sensor_id)), response.json())

    @staticmethod
    def __alerts_response(sensor_id):
        return {'content': [{'data': 1234.345,
                             'id': '0a13fc2b-e962-424e-a1e5-73528065d591',
                             'sensor_id': str(sensor_id)},
                            {'data': 1234.345,
                             'id': '0a13fc2b-e962-424e-a1e5-73528065d580',
                             'sensor_id': str(sensor_id)},
                            {'data': 1234.345,
                             'id': '0a13fc2b-e962-424e-a1e5-73528065d554',
                             'sensor_id': str(sensor_id)}]}
