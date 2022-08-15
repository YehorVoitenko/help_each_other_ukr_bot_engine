from main_project.base.base import Base, engine, Session
from main_project.insert.save import save_user
from main_project.retrives.retrives import get_user_info_by_city, get_user_info_all
from main_project.table.user import User
from main_project.utils.file_utils import get_translation
session = Session()

Base.metadata.create_all(engine)

interface_phrase = get_translation()

choose_your_report = input(interface_phrase.ask_user_what_he_looking_for)

if choose_your_report == 'give':  # TODO: ADD BUTTON
    print(interface_phrase.enter_self_info)
    name = input(interface_phrase.get_name)
    surname = input(interface_phrase.get_surname)
    telephone_number = int(input(interface_phrase.get_telephone_number))
    location_city = input(interface_phrase.get_users_city)

elif choose_your_report == 'need':  # TODO: ADD BUTTON
    location_city = input(interface_phrase.get_users_city)


user_info = User(
    name=name,
    surname=surname,
    location_city=location_city,
    telephone_number=telephone_number,
)

save_user(user_info)

user = get_user_info_all()
final_user = user.pop()
print(final_user)

find_city = input(interface_phrase.report_for_find_city)
needy = get_user_info_by_city(find_city)
print(needy)
