from src.core.common.logger import get_logger
from src.domain.sensor_data_receiver.sensor_message import SensorMessage

logger = get_logger(__name__)


class SensorDataRepository:

    @staticmethod
    def save_data(message: SensorMessage):
        logger.info(f'Sensor data persisted. Sensor id {message.sensor_id}')
