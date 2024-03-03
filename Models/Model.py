from Models import Character
from Models import DataObjects
from Models.DatabaseAPI import DatabaseAPI
from Models.CharacterClass import CharacterClass
from Models.CharacterRace import CharacterRace
from Models.Armor import Armor


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.databaseAPI = DatabaseAPI()
        self.skill_to_score_map = DataObjects.skill_to_score_map()

        self.character = Character.CharacterData(self.controller, self.skill_to_score_map)

        # Create empty dictionaries
        self.class_options = {}
        self.race_options = {}
        self.armors = {}
        # Fill the dictionaries
        self.load_classes()
        self.load_races()
        self.load_armors()

        # Create directory/registry to be called by the controller
        self.directory = {}
        self.create_directory()
        self.register_fields()

    def create_directory(self):
        self_dir = [self.character]
        for obj in self_dir:
            for field in dir(obj):
                self.directory[field] = obj

    def register_fields(self):
        for field, obj in self.directory.items():
            self.controller.register_field(field, obj)

    def load_character(self, character_name):
        # Load character by name, returns a dict. Keys match the DB table columns
        character_data = self.databaseAPI.load_character(character_name)

        self.character.set_name(character_data["Name"])
        self.set_level(character_data["Level"])  # set_level also sets the proficiency bonus
        self.set_class(character_data["Class"])
        self.set_race(character_data["Race"])

        # Each set_ability also sets the ability modifiers and skill bonuses
        self.character.set_score(["Strength", character_data["Strength Score"]])
        self.character.set_score(["Dexterity", character_data["Dexterity Score"]])
        self.character.set_score(["Constitution", character_data["Constitution Score"]])
        self.character.set_score(["Intelligence", character_data["Intelligence Score"]])
        self.character.set_score(["Wisdom", character_data["Wisdom Score"]])
        self.character.set_score(["Charisma", character_data["Charisma Score"]])

    def call_registered(self, field, new_value):
        self.controller.trigger_widget(field, new_value)

    def set_level(self, new_value):
        self.character.level = new_value
        self.controller.trigger_widget("level", new_value)

        self.set_proficiency_bonus()

    def set_class(self, new_value):
        # Here, new_value is just the name of the class, not the class object
        self.character.claas = self.class_options[new_value]
        self.controller.trigger_widget("class", self.character.claas)

    def set_race(self, new_value):
        # Here, new_value is just the name of the race, not the race object
        self.character.race = self.race_options[new_value]
        self.controller.trigger_widget("race", self.character.race)

    def set_proficiency_bonus(self):
        self.character.proficiency_bonus = DataObjects.proficiency_bonus_map(self.character.level)
        self.controller.trigger_widget("proficiency_bonus", self.character.proficiency_bonus)

    def load_classes(self):
        classes = self.databaseAPI.load_classes()
        for claas in classes:
            # claas[0] is the name of the class, so this saves in dictionary format,
            # Class_name: Class_object
            self.class_options[claas[0]] = CharacterClass(claas)

        # Build empty character class
        empty_class = []
        for i in enumerate(classes[0]):
            empty_class.append("")
        empty_class[0] = "None"
        self.class_options[""] = CharacterClass(empty_class)

    def load_races(self):
        races = self.databaseAPI.load_races()
        for race in races:
            # race[0] is the name of the class, so this saves in dictionary format,
            # Race_name: Race_object
            self.race_options[race[0]] = (CharacterRace(race))

        # Build empty character race
        empty_race = []
        for i in enumerate(races[0]):
            empty_race.append("")
        empty_race[0] = "None"
        self.race_options[""] = CharacterRace(empty_race)

    def load_armors(self):
        armors = self.databaseAPI.load_armors()
        for armor in armors:
            # Armor[0] is the name of the armor, so this save in dictionary format,
            # Armor-name: Armor_object
            self.armors[armor[0]] = Armor(armor)
        # Empty armor is "Unarmored" Loaded from DB
