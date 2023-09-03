from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_connection
from dao import dashboard_service

import logging

logger = logging.getLogger("region_resource")

router = APIRouter(prefix='/region',
                   tags=['Region'])


@router.get('/')
async def get_world(db: Session = Depends(get_connection)):
    logger.info("inside get world(region)")
    return dashboard_service.get_region(db)


@router.get('/{region_}')
async def get_region(region_: str, db: Session = Depends(get_connection)):
    logger.info("Inside get region. Requested region : " + region_)
    return dashboard_service.get_region(db, region_)
