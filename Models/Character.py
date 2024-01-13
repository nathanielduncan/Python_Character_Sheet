# This will be the class that holds information on the Player Character as they enter information

class CharacterData:
    def __init__(self):
        self.name = ""
        self.level = None
        self.proficiency_bonus = None
        self.claas = None
        self.race = None

        self.ability_scores = {
            "Strength": "",
            "Dexterity": "",
            "Constitution": "",
            "Intelligence": "",
            "Wisdom": "",
            "Charisma": ""
        }

        self.ability_modifiers = {
            "Strength": "0",
            "Dexterity": "0",
            "Constitution": "0",
            "Intelligence": "0",
            "Wisdom": "0",
            "Charisma": "0"
        }

        self.skill_proficiencies = []

        self.skill_bonuses = {
            "Strength": "0",
            "Dexterity": "0",
            "Constitution": "0",
            "Intelligence": "0",
            "Wisdom": "0",
            "Charisma": "0",

            "Acrobatics": "0",
            "Animal Handling": "0",
            "Arcana": "0",
            "Athletics": "0",
            "Deception": "0",
            "History": "0",
            "Insight": "0",
            "Intimidation": "0",
            "Investigation": "0",
            "Medicine": "0",
            "Nature": "0",
            "Perception": "0",
            "Performance": "0",
            "Persuasion": "0",
            "Religion": "0",
            "Sleight of Hand": "0",
            "Stealth": "0",
            "Survival": "0"
        }
