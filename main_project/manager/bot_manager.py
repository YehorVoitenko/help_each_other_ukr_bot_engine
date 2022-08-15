from main_project.base.base import Base, engine, Session
from main_project.insert.save import save_user
from main_project.retrives.retrives import get_user_info_by_city, get_user_info_all
from main_project.table.user import User

session = Session()

Base.metadata.create_all(engine)

name = input('Enter your name: ')
surname = input('Enter your surname: ')
telephone_number = int(input('Enter your telephone number: '))
location_city = input('Enter your city: ')

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

find_city = input('Enter city, where you want to find help: ')
needy = get_user_info_by_city(find_city)
print(needy)
