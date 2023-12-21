# This will be the class that holds information on the Player Character as they enter information

class CharacterData:
    def __init__(self):
        self.ability_scores = {
            "Strength": "10",
            "Dexterity": "10",
            "Constitution": "10",
            "Intelligence": "10",
            "Wisdom": "10",
            "Charisma": "10"
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
