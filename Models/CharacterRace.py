class CharacterRace:
    def __init__(self, race_attributes):
        self.name = race_attributes[0]
        self.ability_score_increase = str(race_attributes[1]).split(',')
        self.age = race_attributes[2]
        self.alignment = race_attributes[3]
        self.size = race_attributes[4]
        self.speed = race_attributes[5]
        self.features = str(race_attributes[6]).split(',')
        self.tool_proficiencies = str(race_attributes[7]).split(',')
        self.languages = str(race_attributes[8]).split(',')

    def print_all(self):
        print(self.name, self.ability_score_increase, self.age, self.alignment, self.size, self.speed, self.features,
              self.tool_proficiencies, self.languages)
