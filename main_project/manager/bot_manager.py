from main_project.models.base.base import Base, engine, Session
from main_project.models.insert.save import save_user
from main_project.models.retrives.retrives import get_user_info_by_city, get_user_info_all, get_user_info_by_key_words
from main_project.models.table.helpers import Helpers
from main_project.utils.file_utils import get_translation
session = Session()

Base.metadata.create_all(engine)

interface_phrase = get_translation()

# def check_value(*args):
#     for value in args:
#         if isinstance(value, str):
#             result = True
#         else:
#             print(f'Enter only worlds in \'{value}\'')
#             result = False
#             return result
#     return result


def choose_your_report():
    report_type = input(interface_phrase.ask_user_what_he_looking_for)
    return report_type


def get_info_about_helper():
    name = input(interface_phrase.get_name)
    surname: str = input(interface_phrase.get_surname)
    telephone_number: int = int(input(interface_phrase.get_telephone_number))  # TODO: ADD CONTACT INSTEAD OF NUMBER
    location_city: str = input(interface_phrase.get_users_city)
    help_description: str = input(interface_phrase.write_help_description)
    key_help_words: str = input(interface_phrase.get_key_help_words).split(',')
    add_key_help_words = ' ' + ' '.join(key_help_words)

    user_info = Helpers(
        name=name,
        surname=surname,
        location_city=location_city,
        telephone_number=telephone_number,
        help_description=help_description,
        key_help_words=add_key_help_words,
    )
    return save_user(user_info)


def interact_with_needy():  # TODO: ADD BUTTON
    #  Add handler 'start'  #  TODO: ADD TWO BOTS FOR DIVIDE SERVICES (ONE FOR SEARCH, ONE FOR ADD)
    needed_city = input(interface_phrase.report_for_find_city)
    print(get_user_info_by_city(needed_city))
    key_words = input(interface_phrase.add_key_words)
    print(get_user_info_by_key_words(key_words))


def interact_with_helper():  # TODO: ADD BUTTON
    print(interface_phrase.enter_self_info)
    get_info_about_helper()
    print(interface_phrase.thanks_for_help, '\n')
    user = get_user_info_all()
    final_user = user.pop()
    print(final_user)




