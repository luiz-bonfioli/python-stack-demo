import dataclasses
from typing import Optional
from uuid import UUID

from src.core.common.uuid_utils import safe_uuid_to_str


@dataclasses.dataclass
class AlertModel:
    id: Optional[UUID] = dataclasses.field(default=None)
    sensor_id: Optional[UUID] = dataclasses.field(default=None)
    data: Optional[float] = dataclasses.field(default=None)

    def to_dict(self):
        return {
            'id': safe_uuid_to_str(self.id),
            'sensor_id': safe_uuid_to_str(self.sensor_id),
            'data': self.data
        }
