import math

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_connection
from dao import dashboard_service

import logging

logger = logging.getLogger('percentage_user_resource')

router = APIRouter(
    prefix='/percentage',
    tags=['percentage']
)


@router.get('/{percentage}')
async def get_percentage(percentage: float, db: Session = Depends(get_connection)):
    logger.info("inside get_percentage resource")
    start = math.floor(percentage)
    dashboard_service.get_population(start=start, end=start + 1, db=db)
