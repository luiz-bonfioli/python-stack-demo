from pydantic import BaseModel


class SensorModel(BaseModel):
    data: float
