from tkinter import *
from tkinter import ttk
from tkinter import font
import re

import DataObjects


class AbilityBox(ttk.Frame):
    def __init__(self, parent, ability, character_information):
        # Initialize the Frame that is this object
        ttk.Frame.__init__(self, parent, borderwidth=2)

        # Define a function used by the Entry Widget to Validate the input
        def check_num(newval):
            return re.match('^[0-9]*$', newval) is not None and len(newval) <= 2
        # Create a wrapper for the above function, this helps to pass variables
        check_num_wrapper = (self.register(check_num), '%P')

        # Items used to listen for text entered to the entry
        # These are initialized with the values stored in the Character
        entryString = StringVar(value=character_information.ability_scores[ability])
        modifierString = StringVar(value=character_information.ability_modifiers[ability])


        # This function defines what happens when the entry string is changed
        def textEntered(*args):
            if entryString.get() == "":
                pass  # If the entry box is empty, modifier is unchanged
            else:
                character_information.ability_scores[ability] = entryString.get()
                modifier = int(entryString.get()) - 10
                if modifier < 0:  # This accounts for dividing by negative numbers
                     updateModifier(str(int((modifier-1) / 2)))
                else:
                    updateModifier(str(int(modifier / 2)))
        def updateModifier(*args):
            modifierString.set(args[0])
            character_information.ability_modifiers[ability] = args[0]

        # Add a listener function to the string variable
        entryString.trace_add("write", textEntered)

        # Customize the fonts
        abilityFont = font.Font(family='Georgia', size=20, weight='bold')
        modifierFont = font.Font(family='Georgia', size=12)

        # Create the widgets that go into the frame
        lbl_ability = ttk.Label(self, text=ability)
        ent_score = ttk.Entry(self, width=2, font=abilityFont, justify="center",
                              textvariable=entryString, validate='key', validatecommand=check_num_wrapper)
        lbl_modifier = ttk.Label(self, width=2, font=modifierFont, justify="center",
                                 textvariable=modifierString)


        # Arrange the three widgets created above
        lbl_ability.grid(column=0, row=0)
        ent_score.grid(column=0, row=1)
        lbl_modifier.grid(column=0, row=2)


class SkillLine(ttk.Frame):
    def __init__(self, parent, skill, character_information):
        ttk.Frame.__init__(self, parent)

        self.proficient = IntVar()  # Default is false, ensure the boxes default to deselected

        self.bonus = character_information.ability_modifiers[
            DataObjects.skill_to_score_map(skill)
        ]

        def addProficiency(button):  # Function called when checkbutton is selected or deselected
            proficiency = 2  # To be replaced with a data call
            if button.instate(['selected']):  # When selected, add proficiency bonus
                bonus = int(button.cget('text')) + proficiency
                character_information.skill_proficiencies.append(skill)
            else:  # When deselected, remove proficiency bonus
                bonus = int(button.cget('text')) - proficiency
                character_information.skill_proficiencies.remove(skill)
            button.configure(text=str(bonus))  # Replace the button text with the new calculated bonus

        # Define the checkButton, with a lambda pointing to the function called when it is (de)selected
        btn_proficient = ttk.Checkbutton(self, text=self.bonus, variable=self.proficient,
                                         command=lambda: addProficiency(btn_proficient))

        # Defines the label that hold the name of the skill
        lbl_skill = ttk.Label(self, text=skill)

        # Place the created items into the parent frame: self
        btn_proficient.grid(column=0, row=0)
        lbl_skill.grid(column=1, row=0)


class SingleSkill(ttk.Frame):
    def __init__(self, parent, skill):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)

        lbl_bonus = ttk.Label(self, text="0")
        lbl_skill = ttk.Label(self, text=skill)

        lbl_bonus.grid(column=0, row=0)
        lbl_skill.grid(column=1, row=0)


class LabeledEntry(ttk.Frame):
    def __init__(self, parent, description):
        ttk.Frame.__init__(self, parent)

        ent_entry = ttk.Entry(self)
        lbl_label = ttk.Label(self, text=description)

        ent_entry.grid(column=0, row=0)
        lbl_label.grid(column=0, row=1)


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
