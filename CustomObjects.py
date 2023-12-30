from tkinter import *
from tkinter import ttk
from tkinter import font
import re

import DataObjects


class AbilityBox(ttk.Frame):
    def __init__(self, parent, ability, character_information):
        # Initialize the Frame that is this object
        ttk.Frame.__init__(self, parent, borderwidth=2)

        self.ability = ability
        self.character_information = character_information

        # Define a function used by the Entry Widget to Validate the input
        def check_num(entered_val):
            return re.match('^[0-9]*$', entered_val) is not None and len(entered_val) <= 2
        # Create a wrapper for the above function, this helps to pass variables
        check_num_wrapper = (self.register(check_num), '%P')

        # Items used to listen for text entered to the entry
        # These are initialized with the values stored in the Character
        self.entryString = StringVar(value=character_information.ability_scores[ability], name=ability)
        self.modifierString = StringVar(value=character_information.ability_modifiers[ability])


        # Customize the fonts
        abilityFont = font.Font(family='Georgia', size=20, weight='bold')
        modifierFont = font.Font(family='Georgia', size=12)

        # Create the widgets that go into the frame
        self.lbl_ability = ttk.Label(self, text=ability)
        self.ent_score = ttk.Entry(self, width=2, font=abilityFont, justify="center",
                                   textvariable=self.entryString, validate='key', validatecommand=check_num_wrapper)
        self.lbl_modifier = ttk.Label(self, width=2, font=modifierFont, justify="center",
                                      textvariable=self.modifierString)


        # Arrange the three widgets created above
        self.lbl_ability.grid(column=0, row=0)
        self.ent_score.grid(column=0, row=1)
        self.lbl_modifier.grid(column=0, row=2)

    def text_entered(self):
        if self.entryString.get() == "":
            pass  # If the entry box is empty, modifier is unchanged
        else:
            # Calculate the modifier
            modifier = int(self.character_information.ability_scores[self.ability]) - 10
            # Update the modifier
            if modifier < 0:  # This accounts for dividing by negative numbers
                self.character_information.ability_modifiers[self.ability] = str(int((modifier - 1) / 2))
                self.update_modifier()
            else:
                self.character_information.ability_modifiers[self.ability] = str(int(modifier / 2))
                self.update_modifier()

    def update_modifier(self):
        self.modifierString.set(self.character_information.ability_modifiers[self.ability])


class SkillLine(ttk.Frame):
    def __init__(self, parent, skill, character_information):
        ttk.Frame.__init__(self, parent)

        self.character_information = character_information
        self.skill = skill
        self.related_ability = DataObjects.skill_to_score_map(self.skill)
        self.proficient = IntVar()  # Default is false, ensure the boxes default to deselected

        self.bonus = StringVar(value=character_information.ability_modifiers[
            DataObjects.skill_to_score_map(skill)
        ])


        # Define the checkButton, with a lambda pointing to the function called when it is (de)selected
        self.btn_proficient = ttk.Checkbutton(self, textvariable=self.bonus, variable=self.proficient,
                                              command=self.add_proficiency)

        # Defines the label that hold the name of the skill
        self.lbl_skill = ttk.Label(self, text=skill)

        # Place the created items into the parent frame: self
        self.btn_proficient.grid(column=0, row=0)
        self.lbl_skill.grid(column=1, row=0)


    def add_proficiency(self):  # Function called when checkbutton is selected or deselected
        proficiency = 2  # TODO replaced with a data call
        if self.btn_proficient.instate(['selected']):  # When selected, add proficiency bonus
            bonus = int(self.btn_proficient.cget('text')) + proficiency
            self.character_information.skill_proficiencies.append(self.skill)
        else:  # When deselected, remove proficiency bonus
            bonus = int(self.btn_proficient.cget('text')) - proficiency
            self.character_information.skill_proficiencies.remove(self.skill)
        self.bonus.set(value=str(bonus))  # Bonus is stored in the Skill Line Object as a StringVar,
        # It will automatically update the label when changed

    def update_bonus(self):
        # Same as addProficiency, but does not change the Character Data
        proficiency = 2  # TODO replaced with a data call
        if self.btn_proficient.instate(['selected']):  # When selected, add proficiency bonus
            bonus = int(self.character_information.ability_modifiers[self.related_ability]) + proficiency
        else:  # When deselected, remove proficiency bonus
            bonus = int(self.character_information.ability_modifiers[self.related_ability])
        self.bonus.set(value=str(bonus))  # Bonus is stored in the Skill Line Object as a StringVar,
        # It will automatically update the label when changed



class SingleSkill(ttk.Frame):
    def __init__(self, parent, skill):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)

        self.labelString = StringVar()

        self.lbl_bonus = ttk.Label(self, text="0", textvariable=self.labelString)
        self.lbl_skill = ttk.Label(self, text=skill)

        self.lbl_bonus.grid(column=0, row=0)
        self.lbl_skill.grid(column=1, row=0)


class LabeledEntry(ttk.Frame):
    def __init__(self, parent, description):
        ttk.Frame.__init__(self, parent)

        self.entryString = StringVar()
        # Customize the fonts
        entryFont = font.Font(family='Georgia', size=15)

        self.ent_entry = ttk.Entry(self, width=5, font=entryFont, justify='center',
                                   textvariable=self.entryString)
        self.lbl_label = ttk.Label(self, text=description)

        self.ent_entry.grid(column=0, row=0)
        self.lbl_label.grid(column=0, row=1)


class Feature(ttk.Frame):
    def __init__(self, parent, feature):
        ttk.Frame.__init__(self, parent)

        lbl_title = ttk.Label(self, text=feature)
        lbl_description = ttk.Label(self, text="Description")

        lbl_title.grid(column=0, row=0)
        lbl_description.grid(column=0, row=1)


class MajorAttribute(ttk.Frame):
    def __init__(self, parent, title):
        ttk.Frame.__init__(self, parent)

        lbl_bonus = ttk.Label(self, text="0")
        lbl_skill = ttk.Label(self, text=title)

        lbl_bonus.grid(column=0, row=0)
        lbl_skill.grid(column=0, row=1)


class ArmorLine(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        lbl_bonus = ttk.Label(self, text="bonus")
        lbl_armor = ttk.Label(self, text="Armor")
        lbl_description = ttk.Label(self, text="Description")

        lbl_bonus.grid(column=0, row=0)
        lbl_armor.grid(column=1, row=0)
        lbl_description.grid(column=2, row=0)


class LimitedFeature(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        lbl_feature = ttk.Label(self, text="Feature Description")
        lbl_max = ttk.Label(self, text="Max Uses")
        lbl_reset = ttk.Label(self, text="Short or Long rest")
        lbl_uses = ttk.Label(self, text="Uses Count")

        lbl_feature.grid(column=0, row=0)
        lbl_max.grid(column=1, row=0)
        lbl_reset.grid(column=2, row=0)
        lbl_uses.grid(column=3, row=0)
