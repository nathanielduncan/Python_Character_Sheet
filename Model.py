import Character


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.character = Character.CharacterData()
        self.registered_fields = []

    def register(self, field):
        self.registered_fields.append(field)

    def set_name(self, new_value):
        self.character.name = new_value
        for field in self.registered_fields:
            if field == "name":
                self.controller.triggered(field, new_value)
