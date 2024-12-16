from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Header
from starlette.responses import JSONResponse

from src.core.common.logger import get_logger
from src.core.context.context import appcontext
from src.domain.sensor_data_receiver.sensor_model import SensorModel

logger = get_logger(__name__)

router = APIRouter(prefix='/v1/sensors', tags=['Sensors'])

sensor_data_receiver = appcontext.get_sensor_data_receiver()


@router.post('/{sensor_id}')
async def send_sensor_data(sensor_data: SensorModel, sensor_id: UUID,
                           user_id: Optional[str] = Header(alias="x-user-id")) -> JSONResponse:
    logger.debug(f'API requested by the user id: {user_id}')
    await sensor_data_receiver.publish_sensor_data(sensor_id, sensor_data.data)
    return JSONResponse(content={"status": "success"})
