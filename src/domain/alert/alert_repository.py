import uuid

from src.application.model.non_pageable import NonPageable
from src.domain.alert.alert_model import AlertModel


class AlertRepository:

    async def get_alerts_by_sensor_id(self, sensor_id: uuid.UUID):
        return NonPageable(self.__fake_alert(sensor_id))

    @staticmethod
    def __fake_alert(sensor_id):
        return [AlertModel(id=uuid.UUID('0a13fc2b-e962-424e-a1e5-73528065d591'),
                           sensor_id=sensor_id,
                           data=1234.345),
                AlertModel(id=uuid.UUID('0a13fc2b-e962-424e-a1e5-73528065d580'),
                           sensor_id=sensor_id,
                           data=1234.345),
                AlertModel(id=uuid.UUID('0a13fc2b-e962-424e-a1e5-73528065d554'),
                           sensor_id=sensor_id,
                           data=1234.345)
                ]
