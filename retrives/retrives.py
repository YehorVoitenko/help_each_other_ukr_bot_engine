from base.base import Session
from table.user import User

session = Session()


def get_user_info():
    user = session.query(User) \
        .all()
    return user
