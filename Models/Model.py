from Models import Character
from Models import DataObjects
from Models.DatabaseAPI import DatabaseAPI


class Model:
    def __init__(self, controller):
        self.controller = controller
        self.character = Character.CharacterData()

        self.databaseAPI = DatabaseAPI()

    def load_character(self, character_name):
        # Load character by name, returns a dict. Keys match the DB table columns
        character_data = self.databaseAPI.load_character(character_name)

        self.set_name(character_data["Name"])
        self.set_level(character_data["Level"])
        # set_level also sets the proficiency bonus
        self.set_ability("Strength", character_data["Strength Score"])
        self.set_ability("Dexterity", character_data["Dexterity Score"])
        self.set_ability("Constitution", character_data["Constitution Score"])
        self.set_ability("Intelligence", character_data["Intelligence Score"])
        self.set_ability("Wisdom", character_data["Wisdom Score"])
        self.set_ability("Charisma", character_data["Charisma Score"])
        # Each set_ability also sets the ability modifiers and skill bonuses

    def call_registered(self, field, new_value):
        self.controller.triggered(field, new_value)

    def set_name(self, new_value):
        self.character.name = new_value
        self.controller.triggered("name", new_value)

    def set_level(self, new_value):
        self.character.level = new_value
        self.controller.triggered("level", new_value)

        self.set_proficiency_bonus()

    def set_proficiency_bonus(self):
        self.character.proficiency_bonus = DataObjects.proficiency_bonus_map(self.character.level)
        self.controller.triggered("proficiency_bonus", self.character.proficiency_bonus)

    def set_ability(self, ability, new_value):
        self.character.ability_scores[ability] = new_value
        self.call_registered(ability, new_value)

        self.set_modifier(ability)
        self.set_skill_bonus(ability)

    def set_modifier(self, ability):
        if self.character.ability_scores[ability] == "":  # If the new ability score is empty
            self.character.ability_modifiers[ability] = ""
        else:
            # Calculate the modifier
            modifier = int(self.character.ability_scores[ability]) - 10
            # Update the modifier
            if modifier < 0:  # This accounts for dividing by negative numbers
                self.character.ability_modifiers[ability] = str(int((modifier - 1) / 2))
            else:
                self.character.ability_modifiers[ability] = str(int(modifier / 2))

        self.call_registered(ability + "_mod", self.character.ability_modifiers[ability])

    def set_skill_bonus(self, ability):
        modifier = self.character.ability_modifiers[ability]
        # If the ability value, and the related modifier is empty, no math is done
        if modifier == "" or modifier is None:
            mod_with_proficiency = ""
        else:  # If not empty, consider the proficiency bonus
            mod_with_proficiency = str(int(modifier) + int(self.character.proficiency_bonus))

        related_skills = DataObjects.score_to_skill_dict(ability)

        # Place modifier for the saving throw
        if self.character.skill_proficiencies.count(ability) != 0:  # If proficient with save
            self.character.skill_bonuses[ability] = mod_with_proficiency  # Update with modifier + proficiency
        else:  # if not proficient with the save
            self.character.skill_bonuses[ability] = modifier  # Update with modifier
        # Announce the save was updated
        self.call_registered(ability + "_skill", self.character.skill_bonuses[ability])

        # Repeat that, but with each related skill for the ability score
        for skill in related_skills:
            if self.character.skill_proficiencies.count(skill) != 0:  # If proficient with skill
                self.character.skill_bonuses[skill] = mod_with_proficiency  # Update with modifier + proficiency
            else:  # if not proficient with the skill
                self.character.skill_bonuses[skill] = modifier  # Update with modifier
            # Announce the skill was updated
            self.call_registered(skill + "_skill", self.character.skill_bonuses[skill])

    def add_proficiency(self, skill):
        related_ability = DataObjects.skill_to_score_map(skill)
        self.character.skill_proficiencies.append(skill)
        self.set_skill_bonus(related_ability)
        # Does not call any registered fields

    def remove_proficiency(self, skill):
        related_ability = DataObjects.skill_to_score_map(skill)
        self.character.skill_proficiencies.remove(skill)
        self.set_skill_bonus(related_ability)
        # Does not call any registered fields
