from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from db.model import InternetUserTable
from entity.internet_user import InternetUser
from utility import constant
from typing import List

import logging

logger = logging.getLogger("dashboard_service")


def get_country(db: Session, country_: str = constant.DATABASE_COUNTRY_WORLD) -> InternetUser:
    """
    This function returns the internet_user entity mapped with requested country
    name value from inter_user table.
    :param db: Session of db connection.
    :param country_: requested country name
    :return: internet_user entity
    """
    logger.info("Inside get country dao. Requested country: " + country_)
    country = db.query(InternetUserTable).filter(func.lower(InternetUserTable.country) == func.lower(country_)).first()
    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'{country_} is not found')
    return country


def get_all_country(db: Session):
    logger.info("Inside get all country dao.")
    res = db.query(InternetUserTable.country).filter(InternetUserTable.country != constant.DATABASE_COUNTRY_WORLD).all()
    countries = []
    for row in res:
        countries.append(row[0])
    print(countries)
    return {'country': countries}


def get_region(db: Session, region_: str = constant.DATABASE_COUNTRY_WORLD) -> InternetUser:
    """
    This function returns the internet_user entity mapped with requested region
    name value from inter_user table.
    :param db: Session of db connection.
    :param region_: requested region name
    :return: internet_user entity
    """
    logger.info("Inside get region dao. Requested region: " + region_)
    region = db.query(InternetUserTable).filter(func.lower(InternetUserTable.region) == func.lower(region_)).first()
    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'{region_} is not found')
    return region
