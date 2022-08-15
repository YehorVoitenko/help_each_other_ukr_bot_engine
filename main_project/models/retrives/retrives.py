from main_project.models.base.base import Session
from main_project.models.table.helpers import Helpers

session = Session()


def get_user_info_by_city(city: str):
    users = session.query(Helpers).filter(Helpers.location_city == city).all()
    return f'{users}'


def get_user_info_all():
    user = session.query(Helpers).all()
    return user
