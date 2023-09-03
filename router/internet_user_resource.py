from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_connection
from dao import dashboard_service

import logging

logger = logging.getLogger('internet_user_resource')

router = APIRouter(
    prefix='/internet_user',
    tags=['internet_user']
)


@router.get('/{_from}/{_to}/{_performed_on}')
async def get_internet_user(_from: float, _to: float, _performed_on,
                            db: Depends(get_connection)):
    logger.info("inside get_inter_user_resource")
    return dashboard_service.get_population(db=db, start=_from * 1000000, end=_to * 1000000, on= False)
