from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_connection
from dao import dashboard_service

import logging

logger = logging.getLogger('population_resource')

router = APIRouter(
    prefix='/population',
    tags=['population']
)


@router.get('/{_from}/{_to}/{_performed_on}')
async def get_population_between(_from: float, _to: float, db: Session = Depends(get_connection)):
    logger.info("inside get_population_between resource")
    return dashboard_service.get_population(db=db, start=_from * 1000000, end=_to * 1000000,on = True)
