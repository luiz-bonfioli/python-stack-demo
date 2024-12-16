import uuid
from unittest import TestCase
from unittest.mock import Mock

from src.domain.sensor_data.sensor_data_service import SensorDataService
from src.domain.sensor_data_receiver.sensor_message import SensorMessage


class TestSensorDataService(TestCase):

    def test_get_alerts_by_sensor_id(self):
        mock_repository = Mock()
        mock_repository.save_data.return_value = None
        service = SensorDataService(sensor_data_repository=mock_repository)
        message = SensorMessage(sensor_id=uuid.uuid4(),
                                data=123.56)
        service.save_data(message)

        mock_repository.save_data.assert_called_once_with(message)
        called_message = mock_repository.save_data.call_args[0][0]

        self.assertEqual(called_message.sensor_id, message.sensor_id)
        self.assertEqual(called_message.data, message.data)
