from main_project.models.base.base import Session
from main_project.models.table.helpers import Helpers

session = Session()


def get_user_info_by_city(city: str):
    users = session.query(Helpers).filter(Helpers.location_city == city).all()
    return users


def get_user_info_by_key_words(key_words: str):
    result = session.query(Helpers).filter(Helpers.key_help_words.contains(f" {key_words}")).all()
    if result:
        return result



def get_user_info_all():
    user = session.query(Helpers).all()
    return user
