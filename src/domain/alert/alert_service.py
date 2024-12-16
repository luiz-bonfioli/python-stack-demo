from uuid import UUID

from src.core.common.logger import get_logger

logger = get_logger(__name__)


class AlertService:

    def __init__(self, alert_repository):
        self.__alert_repository = alert_repository

    async def get_alerts_by_sensor_id(self, sensor_id: UUID):
        return await self.__alert_repository.get_alerts_by_sensor_id(sensor_id)
