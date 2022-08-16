from main_project.models.base.base import Base
from sqlalchemy import Column, Integer, String


class Helpers(Base):
    __tablename__ = 'helpers'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))
    telephone_number = Column(String(12))
    location_city = Column(String(20))
    help_description = Column(String(250))

    def __repr__(self):
        return f"<User {self.id}\n" \
               f"Name: '{self.name}'\n" \
               f"Surname: '{self.surname}'\n" \
               f"Telephone number: '{self.telephone_number}'\n" \
               f"City: '{self.location_city}'\n" \
               f"Description {self.help_description}>"


