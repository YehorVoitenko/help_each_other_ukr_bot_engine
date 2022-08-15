from main_project.base.base import Base
from sqlalchemy import Column, Integer, String


class Needy(Base):
    __tablename__ = 'needy'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    telephone_number = Column(Integer)
    location_city = Column(String)

    def __repr__(self):
        return f"<User {self.id}\n" \
               f"Name: '{self.name}'\n" \
               f"Surname: '{self.surname}'\n" \
               f"Telephone number: {self.telephone_number}'\n" \
               f"City: {self.location_city}'>"

