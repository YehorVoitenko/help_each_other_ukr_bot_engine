from main_project.models.base.base import Base, engine, Session
from main_project.models.insert.save import save_user
from main_project.models.retrives.retrives import get_user_info_by_city, get_user_info_all
from main_project.models.table.helpers import Helpers
from main_project.utils.file_utils import get_translation
session = Session()

Base.metadata.create_all(engine)

interface_phrase = get_translation()

choose_your_report = input(interface_phrase.ask_user_what_he_looking_for)


def get_info_about_helper():
    name: str = input(interface_phrase.get_name)
    surname: str = input(interface_phrase.get_surname)
    telephone_number: str = input(interface_phrase.get_telephone_number)
    location_city: str = input(interface_phrase.get_users_city)

    user_info = Helpers(
        name=name,
        surname=surname,
        location_city=location_city,
        telephone_number=telephone_number,
    )
    return save_user(user_info)


#  Add handler 'start'  #  TODO: ADD TWO BOTS FOR DIVIDE SERVICES (ONE FOR SEARCH, ONE FOR ADD)
if choose_your_report == interface_phrase.need:  # TODO: ADD BUTTON
    needed_city = input(interface_phrase.report_for_find_city)
    needy = get_user_info_by_city(needed_city)
    print(needy)

elif choose_your_report == interface_phrase.give:  # TODO: ADD BUTTON
    print(interface_phrase.enter_self_info)
    get_info_about_helper()
    print(interface_phrase.thanks_for_help, '\n')
    user = get_user_info_all()
    final_user = user.pop()
    print(final_user)

