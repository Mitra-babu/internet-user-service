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


@router.get('/')
def get_population_between(_from: int, _to: int, db: Session = Depends(get_connection)):
    logger.info("inside get_population_between")
    return dashboard_service.get_population(db=db, start=_from, end=_to)


