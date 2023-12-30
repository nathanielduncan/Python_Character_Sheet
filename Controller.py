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
        to_register = {"widget": widget,
                       "field": field}
        self.registered_widgets.append(to_register)
        self.model.register(field)

    def triggered(self, field, new_value):
        for widget in self.registered_widgets:
            if widget["field"] == field:
                widget["widget"].update_field(widget["field"], new_value)

    def name_entered(self, name, *args):
        self.model.set_name(name)
