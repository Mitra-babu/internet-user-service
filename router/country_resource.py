from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_connection
from dao import dashboard_service

import logging

logger = logging.getLogger("country_resource")

router = APIRouter(
    prefix='/country',
    tags=['Country']
)


@router.get('/')
def get_world(db: Session = Depends(get_connection)):
    logger.info("inside get world(country)")
    return dashboard_service.get_country(db=db)


@router.get('/{country_}')
def get_country(country_: str, db: Session = Depends(get_connection)):
    logger.info("inside get country. Requested country :" + country_)
    return dashboard_service.get_country(db=db, country_=country_)


@router.get('/all')
def get_all_country(db: Session = Depends(get_connection)):
    logger.info("Inside get_all_country")
    return dashboard_service.get_all_country(db=db)
