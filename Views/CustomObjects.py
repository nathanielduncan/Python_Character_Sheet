from tkinter import *
from tkinter import ttk
from tkinter import font
import re



class AbilityBox(ttk.Frame):
    def __init__(self, parent, ability, controller):
        # Initialize the Frame that is this object
        ttk.Frame.__init__(self, parent, borderwidth=2)

        # Save arguments to object
        self.controller = controller
        self.ability = ability
        # Create StringVars for the related widgets
        self.ability_score = StringVar()  # Tied to ent_score
        self.modifier = StringVar()  # Tied to lbl_modifier

        # Define a function used by the Entry Widget to Validate the input
        def check_num(entered_val):
            return re.match('^[0-9]*$', entered_val) is not None and len(entered_val) <= 2
        # Create a wrapper for the above function, this helps to pass variables
        check_num_wrapper = (self.register(check_num), '%P')

        # Customize the fonts
        abilityFont = font.Font(family='Georgia', size=20, weight='bold')
        modifierFont = font.Font(family='Georgia', size=12)

        # Create the widgets that go into the frame
        self.lbl_ability = ttk.Label(self, text=ability)

        self.ent_score = ttk.Entry(self, width=2, font=abilityFont, justify="center",
                                   textvariable=self.ability_score, validate='key', validatecommand=check_num_wrapper)
        # Assign a function to fire when the ability score is edited (from the entry)
        self.ability_score.trace_add("write", self.ability_updated)

        self.lbl_modifier = ttk.Label(self, width=2, font=modifierFont, justify="center",
                                      textvariable=self.modifier)

        # Arrange the three widgets created above
        self.lbl_ability.grid(column=0, row=0)
        self.ent_score.grid(column=0, row=1)
        self.lbl_modifier.grid(column=0, row=2)

        # Register with the controller, to be notified if the ability modifier is updated
        self.controller.register(self, self.ability + "_mod")


    def ability_updated(self, *args):
        # Let the controller know that the ability score was updated
        self.controller.ability_entered(self.ability, self.ability_score.get())

    def update_field(self, field, new_value):
        if field == self.ability + "_mod":
            self.modifier.set(new_value)


class SkillLine(ttk.Frame):
    def __init__(self, parent, skill, controller):
        ttk.Frame.__init__(self, parent)

        # Save arguments to object
        self.skill = skill
        self.controller = controller
        # Define the ability related to the given skill
        self.related_ability = self.controller.get_related_ability(self.skill)
        # Define Vars to be connected with widgets
        self.proficient = IntVar()  # Assigned to ckbtn_proficient. Ensures the box defaults to deselected
        self.bonus = StringVar()

        # Define the widgets
        self.ckbtn_proficient = ttk.Checkbutton(self, textvariable=self.bonus, variable=self.proficient,
                                                command=self.update_proficiency)
        self.lbl_skill = ttk.Label(self, text=skill)

        # Place the created items
        self.ckbtn_proficient.grid(column=0, row=0)
        self.lbl_skill.grid(column=1, row=0)

        # Register with the controller, to be notified if the related ability modifier gets updated
        self.controller.register(self, self.skill + "_skill")

    def update_field(self, field, new_val):
        if field == self.skill + "_skill":
            self.bonus.set(new_val)

    def update_proficiency(self):
        if self.ckbtn_proficient.instate(['selected']):  # When selected, add proficiency
            self.controller.proficiency_entered('add', self.skill)
        else:
            self.controller.proficiency_entered('remove', self.skill)


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
