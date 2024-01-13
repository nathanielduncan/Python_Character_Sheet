class CharacterClass:
    def __init__(self, class_attributes):
        self.name = class_attributes[0]
        self.hit_die = class_attributes[1]
        self.armor_proficiencies = str(class_attributes[2]).split(',')
        self.weapon_proficiencies = str(class_attributes[3]).split(',')
        self.tool_proficiencies = str(class_attributes[4]).split(',')
        self.saving_throw_proficiencies = str(class_attributes[5]).split(',')
        self.skill_proficiencies = str(class_attributes[6]).split(',')
        self.equipment_options = str(class_attributes[7]).split(',')
        self.features = str(class_attributes[8]).split(',')
        self.subclasses = str(class_attributes[9]).split(',')

    def print_all(self):
        print(self.name, self.hit_die, self.armor_proficiencies, self.weapon_proficiencies, self.tool_proficiencies,
              self.saving_throw_proficiencies, self.skill_proficiencies, self.equipment_options, self.features,
              self.subclasses)
