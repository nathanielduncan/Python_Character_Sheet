import DataObjects
from Model import Model
from View import View


class Controller:
    def __init__(self, window):
        self.registered_widgets = []

        self.model = Model(self)
        self.view = View(window, self)

    def fill_character_data(self, character_name):
        """
        This function is to be called when the Character page first opens. It will take all the data from the character
        object, and fill the corresponding widgets in the view.
        :return:
        """

    def register(self, widget, field):
        """
        Widgets with access to the controller can call this function to register themselves, or a widget they own, to be
        notified if the specified field is updated in the model. The passed widget must have a method named
        'update_field(field, new_value)'
        :param widget:
        :param field:
        :return:
        """
        to_register = {"widget": widget,
                       "field": field}
        self.registered_widgets.append(to_register)

    def triggered(self, field, new_value):
        for item in self.registered_widgets:
            if item["field"] == field:
                item["widget"].update_field(item["field"], new_value)

    def name_entered(self, name, *args):
        self.model.set_name(name)

    def ability_entered(self, ability, new_value):
        self.model.set_ability(ability, new_value)

    def proficiency_entered(self, action, skill):
        if action == "add":
            self.model.add_proficiency(skill)
        if action == "remove":
            self.model.remove_proficiency(skill)

    def get_ability_list(self):
        return list(self.model.character.ability_scores)

    def get_skill_list(self):
        skills = list(self.model.character.skill_bonuses)
        for x in range(6):  # Remove the saves from this list
            skills.pop(0)
        return skills

    def get_related_ability(self, skill):
        return DataObjects.skill_to_score_map(skill)
