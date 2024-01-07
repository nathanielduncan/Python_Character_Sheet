from Models.Model import Model
from Models import DataObjects
from Views.View import View


class Controller:
    def __init__(self, window):
        self.registered_widgets = []

        self.model = Model(self)
        self.view = View(window, self)

    def show_main_menu(self):
        self.view.show_main_menu()

    def show_character_page(self):
        self.view.show_character_page()
        self.model.load_character("New_Character")

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
        """
        Called by the model when it changes some data. the model provides the field name that was changed and the
        new value of that filed. This function then looks at all the registered widgets, to see if they have requested
        that field. If it has, it gives the widget the new value. The widget can do whatever with that knowledge.
        :param field:
        :param new_value:
        :return:
        """
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
