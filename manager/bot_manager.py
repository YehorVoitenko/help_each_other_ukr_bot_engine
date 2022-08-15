from datetime import date, time
from base.base import Base, engine, Session
from insert.save import save_user
from retrives.retrives import get_user_info
from table.user import User

session = Session()

Base.metadata.create_all(engine)

name = input('Enter your name: ')
surname = input('Enter your surname: ')
telephone_number = int(input('Enter your telephone number: '))


user_info = User(name=name,
                 surname=surname,
                 telephone_number=telephone_number)

save_user(user_info)

user = get_user_info()

last_user = user.pop()

print(last_user)
