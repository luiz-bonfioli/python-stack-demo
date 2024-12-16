from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Header
from starlette.responses import JSONResponse

from src.application.model.non_pageable import NonPageable
from src.core.common.logger import get_logger
from src.core.context.context import appcontext
from src.domain.alert.alert_model import AlertModel

logger = get_logger(__name__)

router = APIRouter(prefix='/v1/alerts', tags=['Alerts'])

alerts_service = appcontext.get_alert_service()


@router.get('/{sensor_id}')
async def get_alerts_by_sensor_id(sensor_id: UUID,
                                  user_id: Optional[str] = Header(alias="x-user-id")) -> JSONResponse:
    logger.debug(f'API requested by the user id: {user_id}')
    response: NonPageable[AlertModel] = await alerts_service.get_alerts_by_sensor_id(sensor_id)
    return JSONResponse(content=response.to_dict())
