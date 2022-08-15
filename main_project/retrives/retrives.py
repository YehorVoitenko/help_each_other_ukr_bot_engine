from main_project.base.base import Session
from main_project.table.user import User

session = Session()


def get_user_info_by_city(city: str):
    user = session.query(User).filter(User.location_city == city).all()
    return user


def get_user_info_all():
    user = session.query(User).all()
    return user
