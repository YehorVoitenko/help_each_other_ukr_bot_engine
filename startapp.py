from main_project.manager.bot_manager import choose_your_report, interact_with_needy, interact_with_helper
from main_project.utils.file_utils import get_translation

interface_phrase = get_translation()

while True or interact_type != interface_phrase.stop:
    interact_type = choose_your_report()

    if interact_type == interface_phrase.give:
        interact_with_helper()
    elif interact_type == interface_phrase.need:
        interact_with_needy()
    elif interact_type == interface_phrase.stop:
        exit()
    else:
        print(interface_phrase.syntax_error)





