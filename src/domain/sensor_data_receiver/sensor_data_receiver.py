from uuid import UUID

from src.core.common.logger import get_logger
from src.core.common.uuid_utils import safe_uuid_to_str
from src.domain.sensor_data_receiver.sensor_message import SensorMessage

logger = get_logger(__name__)


class SensorDataReceiver:

    def __init__(self, kafka_producer):
        self.__kafka_producer = kafka_producer

    async def publish_sensor_data(self, sensor_id: UUID, data: float):
        logger.debug('New sensor data arrived from request. Sensor id %s', sensor_id)
        message_bytes = SensorMessage(sensor_id=sensor_id,
                                      data=data).to_bytes()

        return self.__kafka_producer.publish_messages(messages=[(safe_uuid_to_str(sensor_id), message_bytes)])
