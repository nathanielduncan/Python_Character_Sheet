# This will be the class that holds information on the Player Character as they enter information

class CharacterData:
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

        self.name = ""
        self.level = ""
        self.proficiency_bonus = ""
        self.claas = ""
        self.race = ""
        self.strength_score = ""

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

    def __dir__(self):
        return ["name", "level", "proficiency_bonus", "class", "race", "Strength_score", "score",
                "ability_modifiers", "skill_proficiencies", "skill_bonuses"]

    def update_field(self, field, new_value):
        try:
            print("Calling", "set_"+field, "with ", new_value)
            getattr(self, "set_" + field)(new_value)
        except AttributeError:
            print("No function found in Character for set_" + field)

    def set_name(self, new_name):
        self.name = new_name
        self.controller.trigger_widget("name", self.name)

    def set_score(self, value_details):
        ability = value_details[0]
        new_score = value_details[1]
        self.ability_scores[ability] = new_score
        self.controller.trigger_widget(ability, new_score)

        self.set_modifier(ability)
        self.set_skill_bonus(ability)

    def set_modifier(self, ability):
        if self.ability_scores[ability] == "":  # If the new ability score is empty
            self.ability_modifiers[ability] = ""
        else:
            # Calculate the modifier
            modifier = int(self.ability_scores[ability]) - 10
            # Update the modifier
            if modifier < 0:  # This accounts for dividing by negative numbers
                self.ability_modifiers[ability] = str(int((modifier - 1) / 2))
            else:
                self.ability_modifiers[ability] = str(int(modifier / 2))

        self.controller.trigger_widget(ability + "_mod", self.ability_modifiers[ability])

    def set_skill_bonus(self, ability):
        modifier = self.ability_modifiers[ability]
        # If the ability value, and the related modifier is empty, no math is done
        if modifier == "" or modifier is None:
            mod_with_proficiency = ""
        else:  # If not empty, consider the proficiency bonus
            mod_with_proficiency = str(int(modifier) + int(self.proficiency_bonus))

        related_skills = self.model.score_to_skill_dict(ability)

        # Place modifier for the saving throw
        if self.skill_proficiencies.count(ability) != 0:  # If proficient with save
            self.skill_bonuses[ability] = mod_with_proficiency  # Update with modifier + proficiency
        else:  # if not proficient with the save
            self.skill_bonuses[ability] = modifier  # Update with modifier
        # Announce the save was updated
        self.controller.trigger_widget(ability + "_skill", self.skill_bonuses[ability])

        # Repeat that, but with each related skill for the ability score
        for skill in related_skills:
            if self.skill_proficiencies.count(skill) != 0:  # If proficient with skill
                self.skill_bonuses[skill] = mod_with_proficiency  # Update with modifier + proficiency
            else:  # if not proficient with the skill
                self.skill_bonuses[skill] = modifier  # Update with modifier
            # Announce the skill was updated
            self.controller.trigger_widget(skill + "_skill", self.skill_bonuses[skill])

    def set_skill_proficiencies(self, value_details):
        if value_details[0] == 'add':
            related_ability = self.model.skill_to_score_map(value_details[1])
            self.skill_proficiencies.append(value_details[1])
            self.set_skill_bonus(related_ability)
            # Dont trigger_widget, this is done in set_skill_bonus
        elif value_details[0] == 'remove':
            related_ability = self.model.skill_to_score_map(value_details[1])
            self.skill_proficiencies.remove(value_details[1])
            self.set_skill_bonus(related_ability)
            # Dont trigger_widget, this is done in set_skill_bonus

    def set_level(self, new_value):
        self.level = new_value
        self.controller.trigger_widget("level", new_value)

        self.set_proficiency_bonus()

    def set_proficiency_bonus(self):
        self.proficiency_bonus = self.model.proficiency_bonus_map(self.level)
        self.controller.trigger_widget("proficiency_bonus", self.proficiency_bonus)

        # Also update skills using new prof bonus, do for each ability type
        for ability in list(self.ability_scores):
            self.set_skill_bonus(ability)

    def set_race(self, new_value):
        # Here, new_value is just the name of the race, not the race object
        self.race = self.model.race_options[new_value]
        self.controller.trigger_widget("race", self.race)

    def set_class(self, new_value):
        # Here, new_value is just the name of the class, not the class object
        self.claas = self.model.class_options[new_value]
        self.controller.trigger_widget("class", self.claas)
