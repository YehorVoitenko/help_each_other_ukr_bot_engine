from main_project.base.base import Session

session = Session()


def save_user(user: list):
    session.add(user)
    session.commit()
