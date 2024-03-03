from Models.Model import Model
from Views.View import View


class Controller:
    def __init__(self, window):
        self.registered_widgets = []
        self.registered_fields = []

        self.model = Model(self)
        self.view = View(window, self)

    def show_main_menu(self):
        self.view.show_main_menu()

    def show_character_page(self):
        self.view.show_character_page()
        self.model.load_character("New_Character")

    def register_widget(self, widget, field):
        """
        Widgets with access to the controller can call this function to register themselves, or a widget they own, to be
        notified if the specified field is updated in the model. The passed widget must have a method named
        'update_field(field, new_value)'
        """
        to_register = {"widget": widget,
                       "field": field}
        self.registered_widgets.append(to_register)

    def trigger_widget(self, field, new_value):
        """
        Called by the model when it changes some data. the model provides the field name that was changed and the
        new value of that filed. This function then looks at all the registered widgets, to see if they have requested
        that field. If it has, it gives the widget the new value. The widget can do whatever with that knowledge.
        """
        for item in self.registered_widgets:
            if item["field"] == field:
                item["widget"].update_field(item["field"], new_value)

    def register_field(self, field, obj):
        """
        Fields with access to the controller can call this function to register themselves, to be notified if any
        widgets from the view try to update that field. The passed field must have a method named
        'update_field(field, new_value)'
        """
        to_register = {"field": field,
                       "object": obj}
        self.registered_fields.append(to_register)

    def trigger_field(self, field, new_value):
        """
        Called by a widget when it changes some data. The widget provides the field name that was changed and the
        new value of that filed. This function then looks at all the registered fields from the model, to see if they
        have requested that field. If it has, it gives the field the new value.
        The field can do whatever with that knowledge.
        """
        for item in self.registered_fields:
            if item["field"] == field:
                item["object"].update_field(item["field"], new_value)

    def get_ability_list(self):
        return list(self.model.character.ability_scores)

    def get_skill_list(self):
        skills = list(self.model.character.skill_bonuses)
        for x in range(6):  # Remove the saves from this list
            skills.pop(0)
        return skills

    def get_related_ability(self, skill):
        return self.model.skill_to_score_map(skill)

    def get_class_names(self):
        names = []
        for claas in self.model.class_options:
            names.append(claas)

        return names

    def get_race_names(self):
        races = []
        for race in self.model.race_options:
            races.append(race)

        return races
