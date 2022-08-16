from main_project.models.base.base import Base
from sqlalchemy import Column, Integer, String


class Helpers(Base):
    __tablename__ = 'helpers'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, )
    surname = Column(String(20), nullable=False)
    telephone_number = Column(String(12), nullable=False)
    location_city = Column(String(20), nullable=False)
    help_description = Column(String(250), nullable=False)
    key_help_words = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<\nUser {self.id}\n" \
               f"Name: '{self.name}'\n" \
               f"Surname: '{self.surname}'\n" \
               f"Telephone number: '{self.telephone_number}'\n" \
               f"City: '{self.location_city}'\n" \
               f"Description: {self.help_description}\n" \
               f"Key words: '{self.key_help_words}'\n>"
