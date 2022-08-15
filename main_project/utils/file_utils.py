import json
from main_project.static.path.path import TRANSLATIONS
from main_project.utils.string_utils import Translation


def get_translation(file: str = TRANSLATIONS):
    with open(file) as text:
        kwargs = json.load(text)
    return Translation(**kwargs)
