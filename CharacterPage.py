from tkinter import *
from tkinter import ttk

import CustomObjects
import DataObjects
import Character


class CharacterPage(ttk.Frame):
    def __init__(self, parent, character_information):
        ttk.Frame.__init__(self, parent)

        # Top Player Frame
        frm_player_information = ttk.Frame(self, borderwidth=2, relief=SOLID)
        self.populateFrame_playerInformation(frm_player_information)
        frm_player_information.grid(column=0, row=0, columnspan=3)

        # Left scores frame
        frm_scores = ttk.Frame(self)
        self.populateFrame_scores(frm_scores, character_information)
        frm_scores.grid(column=0, row=1, rowspan=4)

        # Bottom Left features frame
        frm_features = ttk.Frame(self)
        self.populateFrame_features(frm_features)
        frm_features.grid(column=0, row=5)

        # Center Life frame
        frm_life = ttk.Frame(self, borderwidth=2, relief=SOLID)
        self.populateFrame_life(frm_life)
        frm_life.grid(column=1, row=1, rowspan=2)

        # Center limits frame
        frm_limits = ttk.Frame(self, borderwidth=2, relief=SOLID)
        self.populateFrame_limits(frm_limits)
        frm_limits.grid(column=1, row=3)

        # Right proficiencies frame
        frm_proficiencies = ttk.Frame(self)
        self.populateFrame_proficiencies(frm_proficiencies)
        frm_proficiencies.grid(column=2, row=1, rowspan=3)

        # Bottom Left options frame
        frm_options = ttk.Frame(self, borderwidth=2, relief=SOLID)
        self.populateFrame_options(frm_options)
        frm_options.grid(column=1, row=4, columnspan=2, rowspan=2)


    def populateFrame_playerInformation(self, parentFrame):
        character_name = CustomObjects.LabeledEntry(parentFrame, "Character Name")
        character_name.grid(column=0, row=0)

        # Frame for the other 6 player information items
        frm_player_items = ttk.Frame(parentFrame)
        frm_player_items.grid(column=1, row=0)
        # Item 1, level and class
        frm_class = CustomObjects.LabeledEntry(frm_player_items, "Class")
        frm_class.grid(column=0, row=0)
        # Item 2, Race
        frm_race = CustomObjects.LabeledEntry(frm_player_items, "Race")
        frm_race.grid(column=1, row=0)
        # Item 3, Background
        frm_background = CustomObjects.LabeledEntry(frm_player_items, "Background")
        frm_background.grid(column=2, row=0)
        # Item 4, Level
        frm_level = CustomObjects.LabeledEntry(frm_player_items, "Level exp/exp")
        frm_level.grid(column=0, row=1)
        # Item 5, Alignment
        frm_Alignment = CustomObjects.LabeledEntry(frm_player_items, "Alignment")
        frm_Alignment.grid(column=1, row=1)
        # Item 6, Player Name
        frm_player = CustomObjects.LabeledEntry(frm_player_items, "Player Name")
        frm_player.grid(column=2, row=1)


    def populateFrame_scores(self, parentFrame, character_information):
        # Left abilities frame
        frm_abilities = ttk.Frame(parentFrame, borderwidth=2, relief=SOLID)
        frm_abilities.grid(column=0, row=0, rowspan=4)
        ttk.Label(frm_abilities, text="Ability Scores").grid(column=0, row=0)
        abilities = DataObjects.ability_scores()
        for index, ability in enumerate(abilities):
            CustomObjects.AbilityBox(frm_abilities, ability, character_information).grid(column=0, row=index+1)

        # Right column, 1st spot, Proficiency bonus
        proficiency_bonus = CustomObjects.SingleSkill(parentFrame, "Proficiency Bonus")
        proficiency_bonus.grid(column=1, row=0)

        # right column, 2nd spot, saving throws
        frm_saves = ttk.Frame(parentFrame, borderwidth=2, relief=SOLID)
        frm_saves.grid(column=1, row=1)
        ttk.Label(frm_saves, text="Saving Throws").grid(column=0, row=0, columnspan=2)
        saves = DataObjects.ability_scores()
        saveLines = []
        for index, save in enumerate(saves):
            saveLines.append(CustomObjects.SkillLine(frm_saves, save))
            saveLines[index].grid(column=0, row=index+1, sticky=W)

        # Right column, 3rd spot, skills box
        frm_skills = ttk.Frame(parentFrame, borderwidth=2, relief=SOLID)
        frm_skills.grid(column=1, row=2)
        ttk.Label(frm_skills, text="Skills").grid(column=0, row=0, columnspan=2)
        skills = DataObjects.ability_skills()
        for index, skill in enumerate(skills):
            CustomObjects.SkillLine(frm_skills, skill).grid(column=0, row=index+1, sticky=W)

        # Right column, 4th spot, passive perception
        passive_perception = CustomObjects.SingleSkill(parentFrame, "Passive Perception")
        passive_perception.grid(column=1, row=3)


    def populateFrame_features(self, parentFrame):
        # Frame for racial traits
        frm_race_traits = ttk.Frame(parentFrame, borderwidth=2, relief=SOLID)
        frm_race_traits.grid(column=0, row=0)
        ttk.Label(frm_race_traits, text="Racial Traits").grid(column=0, row=0)
        for index in range(5):
            CustomObjects.Feature(frm_race_traits, "Feature").grid(column=0, row=index+1)

        # Frame for the background feature
        frm_background_features = ttk.Frame(parentFrame, borderwidth=2, relief=SOLID)
        frm_background_features.grid(column=0, row=1)
        ttk.Label(frm_background_features)
        CustomObjects.Feature(frm_background_features, "Background Feature").grid(column=0, row=0)


    def populateFrame_life(selfself, parentFrame):
        # Frame for the top three items
        frm_major_attributes = ttk.Frame(parentFrame)
        frm_major_attributes.grid(column=0, row=0)

        ent_max_health = CustomObjects.LabeledEntry(frm_major_attributes, "Max Hit Points")
        ent_max_health.grid(column=0, row=0)
        lbl_initiative = CustomObjects.MajorAttribute(frm_major_attributes, "Initiative")
        lbl_initiative.grid(column=1, row=0)
        lbl_speed = CustomObjects.MajorAttribute(frm_major_attributes, "Speed")
        lbl_speed.grid(column=2, row=0)

        # Frame for Health
        frm_health = ttk.Frame(parentFrame)
        frm_health.grid(column=0, row=1)

        lbl_hitPoints = CustomObjects.LabeledEntry(frm_health, "Current Hit Points")
        lbl_hitPoints.grid(column=0, row=0, columnspan=2)
        lbl_tempPoints = CustomObjects.LabeledEntry(frm_health, "Temporary Hit Points")
        lbl_tempPoints.grid(column=0, row=1, columnspan=2)
        lbl_hitDice = CustomObjects.LabeledEntry(frm_health, "Hit Dice")
        lbl_hitDice.grid(column=0, row=2)
        lbl_deathRolls = CustomObjects.LabeledEntry(frm_health, "Death Saves")
        lbl_deathRolls.grid(column=1, row=2)


    def populateFrame_proficiencies(self, parentFrame):
        # Frame for armor information
        frm_armor = ttk.Frame(parentFrame, borderwidth=2, relief=SOLID)
        frm_armor.grid(column=0, row=0)
        ttk.Label(frm_armor, text="Armor Attributes").grid(column=0, row=0)
        for index in range(3):
            CustomObjects.ArmorLine(frm_armor).grid(column=0, row=index+1)

        # Frame for Proficiencies
        frm_proficiencies = ttk.Frame(parentFrame, borderwidth=2, relief=SOLID)
        frm_proficiencies.grid(column=0, row=1)
        # Additional Proficiencies Frame for Armor
        frm_armor_proficiencies = ttk.Frame(frm_proficiencies)
        frm_armor_proficiencies.grid(column=0, row=0, columnspan=2)
        ttk.Label(frm_armor_proficiencies, text="Armor Proficiencies").grid(column=0, row=0, columnspan=4)
        for index in range(4):
            ttk.Radiobutton(frm_armor_proficiencies, text="Armor Type").grid(column=index, row=1)
        # Additional Proficiencies Frame for Weapons
        frm_weapon_proficiencies = ttk.Frame(frm_proficiencies)
        frm_weapon_proficiencies.grid(column=0, row=1, columnspan=2)
        ttk.Label(frm_weapon_proficiencies, text="Weapon Proficiencies").grid(column=0, row=2, columnspan=4)
        for index in range(3):
            ttk.Radiobutton(frm_weapon_proficiencies, text="Weapon type").grid(column=index, row=3)
        # Additional proficiencies Frame for languages
        frm_language_proficiencies = ttk.Frame(frm_proficiencies)
        frm_language_proficiencies.grid(column=0, row=2)
        ttk.Label(frm_language_proficiencies, text="Language Proficiencies").grid(column=0, row=0)
        for index in range(5):
            ttk.Label(frm_language_proficiencies, text="Language").grid(column=0, row=index+1)
        # Additional proficiencies Frame for Tools
        frm_tool_proficiencies = ttk.Frame(frm_proficiencies)
        frm_tool_proficiencies.grid(column=1, row=2)
        ttk.Label(frm_tool_proficiencies, text="Tool Proficiencies").grid(column=0, row=0)
        for index in range(5):
            ttk.Label(frm_tool_proficiencies, text="Tool").grid(column=0, row=index+1)


    def populateFrame_limits(self, parent):
        ttk.Label(parent, text="Daily Limits").grid(column=0, row=0, columnspan=4)
        ttk.Label(parent, text="Feature").grid(column=0, row=1)
        ttk.Label(parent, text="Max Uses").grid(column=1, row=1)
        ttk.Label(parent, text="Resets On").grid(column=2, row=1)
        ttk.Label(parent, text="Used").grid(column=3, row=1)
        for index in range(5):
            CustomObjects.LimitedFeature(parent).grid(column=0, row=index+2, columnspan=4)



    def populateFrame_options(self, parent):
        for index in range(10):
            for i in range(3):
                ttk.Label(parent, text="Action").grid(column=i, row=index)

