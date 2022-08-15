from base.base import Session

session = Session()


def save_user(user):
    session.add(user)
    session.commit()
