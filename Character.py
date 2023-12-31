# This will be the class that holds information on the Player Character as they enter information

class CharacterData:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.proficiency_bonus = 2

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
