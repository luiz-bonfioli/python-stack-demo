from src.core.common.logger import get_logger
from src.core.context.context import appcontext
from src.domain.sensor_data_receiver.sensor_message import SensorMessage

logger = get_logger(__name__)

sensor_data_service = appcontext.get_sensor_data_service()


class SensorDataConsumer:

    @staticmethod
    def read_sensor_data(payload: bytes):
        sensor_data_service.save_data(SensorMessage.from_bytes(payload))

    @staticmethod
    def sensor_data_error(msg: str):
        logger.error(msg)
