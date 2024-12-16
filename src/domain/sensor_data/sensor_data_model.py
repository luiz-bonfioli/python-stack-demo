from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from src.core.common.uuid_utils import safe_uuid_to_str


@dataclass
class SensorDataModel:
    id: Optional[UUID] = field(default=None)
    sensor_id: Optional[UUID] = field(default=None)
    data: Optional[float] = field(default=None)

    def to_dict(self):
        return {
            'id': safe_uuid_to_str(self.id),
            'sensor_id': safe_uuid_to_str(self.sensor_id),
            'data': self.data
        }
