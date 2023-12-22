from tkinter import *
from tkinter import ttk

import CustomObjects
import DataObjects


class PlayerInformation(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)

        character_name = CustomObjects.LabeledEntry(self, "Character Name")
        character_name.grid(column=0, row=0)

        # Frame for the other 6 player information items
        frm_player_items = ttk.Frame(self)
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


class Scores(ttk.Frame):
    def __init__(self, parent, character_information):
        ttk.Frame.__init__(self, parent)

        # Left abilities frame
        self.frm_abilities = ttk.Frame(self, borderwidth=2, relief=SOLID)
        self.frm_abilities.grid(column=0, row=0, rowspan=4)
        ttk.Label(self.frm_abilities, text="Ability Scores").grid(column=0, row=0)
        abilities = DataObjects.ability_scores()  # Get the list of abilities, TODO:: change to database
        self.ability_boxes = []  # Make an array, to store the 6 frame_AbilityBoxes
        for index, ability in enumerate(abilities):  # For each box
            temp = CustomObjects.AbilityBox(self.frm_abilities, ability, character_information)  # Initiate it
            temp.grid(column=0, row=index + 1)  # Place it
            temp.entryString.trace_add("write", self.textEntered)  # Make a listener for the Entry
            self.ability_boxes.append(temp)  # Save the box into the array


        # Right column, 1st spot, Proficiency bonus
        self.proficiency_bonus = CustomObjects.SingleSkill(self, "Proficiency Bonus")
        self.proficiency_bonus.grid(column=1, row=0)

        # right column, 2nd spot, saving throws
        self.frm_saves = ttk.Frame(self, borderwidth=2, relief=SOLID)
        self.frm_saves.grid(column=1, row=1)
        ttk.Label(self.frm_saves, text="Saving Throws").grid(column=0, row=0, columnspan=2)
        saves = DataObjects.ability_scores()
        for index, save in enumerate(saves):
            CustomObjects.SkillLine(self.frm_saves, save, character_information).grid(column=0, row=index+1, sticky=W)

        # Right column, 3rd spot, skills box
        self.frm_skills = ttk.Frame(self, borderwidth=2, relief=SOLID)
        self.frm_skills.grid(column=1, row=2)
        ttk.Label(self.frm_skills, text="Skills").grid(column=0, row=0, columnspan=2)
        skills = DataObjects.ability_skills()
        for index, skill in enumerate(skills):
            CustomObjects.SkillLine(self.frm_skills, skill, character_information).grid(column=0, row=index+1, sticky=W)

        # Right column, 4th spot, passive perception
        passive_perception = CustomObjects.SingleSkill(self, "Passive Perception")
        passive_perception.grid(column=1, row=3)

    def textEntered(*args):
        print("Hello Andi")


class Features(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Frame for racial traits
        frm_race_traits = ttk.Frame(self, borderwidth=2, relief=SOLID)
        frm_race_traits.grid(column=0, row=0)
        ttk.Label(frm_race_traits, text="Racial Traits").grid(column=0, row=0)
        for index in range(5):
            CustomObjects.Feature(frm_race_traits, "Feature").grid(column=0, row=index+1)

        # Frame for the background feature
        frm_background_features = ttk.Frame(self, borderwidth=2, relief=SOLID)
        frm_background_features.grid(column=0, row=1)
        ttk.Label(frm_background_features)
        CustomObjects.Feature(frm_background_features, "Background Feature").grid(column=0, row=0)


class Life(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)

        # Frame for the top three items
        frm_major_attributes = ttk.Frame(self)
        frm_major_attributes.grid(column=0, row=0)

        ent_max_health = CustomObjects.LabeledEntry(frm_major_attributes, "Max Hit Points")
        ent_max_health.grid(column=0, row=0)
        lbl_initiative = CustomObjects.MajorAttribute(frm_major_attributes, "Initiative")
        lbl_initiative.grid(column=1, row=0)
        lbl_speed = CustomObjects.MajorAttribute(frm_major_attributes, "Speed")
        lbl_speed.grid(column=2, row=0)

        # Frame for Health
        frm_health = ttk.Frame(self)
        frm_health.grid(column=0, row=1)

        lbl_hitPoints = CustomObjects.LabeledEntry(frm_health, "Current Hit Points")
        lbl_hitPoints.grid(column=0, row=0, columnspan=2)
        lbl_tempPoints = CustomObjects.LabeledEntry(frm_health, "Temporary Hit Points")
        lbl_tempPoints.grid(column=0, row=1, columnspan=2)
        lbl_hitDice = CustomObjects.LabeledEntry(frm_health, "Hit Dice")
        lbl_hitDice.grid(column=0, row=2)
        lbl_deathRolls = CustomObjects.LabeledEntry(frm_health, "Death Saves")
        lbl_deathRolls.grid(column=1, row=2)


class Limits(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)

        ttk.Label(self, text="Daily Limits").grid(column=0, row=0, columnspan=4)
        ttk.Label(self, text="Feature").grid(column=0, row=1)
        ttk.Label(self, text="Max Uses").grid(column=1, row=1)
        ttk.Label(self, text="Resets On").grid(column=2, row=1)
        ttk.Label(self, text="Used").grid(column=3, row=1)
        for index in range(5):
            CustomObjects.LimitedFeature(self).grid(column=0, row=index+2, columnspan=4)


class Proficiencies(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Frame for armor information
        frm_armor = ttk.Frame(self, borderwidth=2, relief=SOLID)
        frm_armor.grid(column=0, row=0)
        ttk.Label(frm_armor, text="Armor Attributes").grid(column=0, row=0)
        for index in range(3):
            CustomObjects.ArmorLine(frm_armor).grid(column=0, row=index+1)

        # Frame for Proficiencies
        frm_proficiencies = ttk.Frame(self, borderwidth=2, relief=SOLID)
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


class Options(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)

        for index in range(10):
            for i in range(3):
                ttk.Label(self, text="Action").grid(column=i, row=index)
