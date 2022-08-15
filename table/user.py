from base.base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    telephone_number = Column(Integer)

    def __repr__(self):
        return f"<User{self.id}\n" \
               f"Name: '{self.name}'\n" \
               f"Surname: '{self.surname}'\n" \
               f"Telephone number: {self.telephone_number}'>"
