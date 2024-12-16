from src.core.common.logger import get_logger
from src.domain.sensor_data_receiver.sensor_message import SensorMessage

logger = get_logger(__name__)


class SensorDataService:

    def __init__(self, sensor_data_repository):
        self.__sensor_data_repository = sensor_data_repository

    def save_data(self, message: SensorMessage):
        self.__sensor_data_repository.save_data(message)
