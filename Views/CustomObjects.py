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


class ProfBonusBox(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)
        self.controller = controller

        self.labelString = StringVar()
        self.lbl_bonus = ttk.Label(self, text="0", textvariable=self.labelString)

        self.lbl_proficiency = ttk.Label(self, text="Proficiency Bonus")

        self.lbl_bonus.grid(column=0, row=0)
        self.lbl_proficiency.grid(column=1, row=0)

        self.controller.register(self, "proficiency_bonus")

    def update_field(self, field, new_val):
        if field == "proficiency_bonus":
            self.labelString.set(new_val)


class PassiveSkillBox(ttk.Frame):
    def __init__(self, parent, skill, controller):
        ttk.Frame.__init__(self, parent, borderwidth=2, relief=SOLID)
        self.controller = controller
        self.skill = skill

        self.labelString = StringVar()
        self.lbl_bonus = ttk.Label(self, text="0", textvariable=self.labelString)

        self.lbl_skill = ttk.Label(self, text="Passive " + skill)

        self.lbl_bonus.grid(column=0, row=0)
        self.lbl_skill.grid(column=1, row=0)

        self.controller.register(self, self.skill + "_skill")

    def update_field(self, field, new_val):
        if field == self.skill + "_skill":
            if new_val == "":
                self.labelString.set("")
            else:
                self.labelString.set(str(int(new_val) + 10))


class CharacterNameBox(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.name = StringVar()
        self.name.trace_add("write", self.name_entered)
        entryFont = font.Font(family='Georgia', size=15)

        self.ent_name = ttk.Entry(self, width=25, font=entryFont, justify='center', textvariable=self.name)
        self.lbl_label = ttk.Label(self, text="Character Name")

        self.ent_name.grid(column=0, row=0)
        self.lbl_label.grid(column=0, row=1)

        self.controller.register(self, "name")

    def name_entered(self, *args):
        # Called by changes to ent_name
        self.controller.name_entered(self.name.get())

    def update_field(self, field, new_val):
        # Called by the controller, since self is registered
        if field == "name":
            self.name.set(new_val)


class LabeledOptions(ttk.Frame):
    def __init__(self, parent, title, options, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = title

        self.option = StringVar()
        custom_font = font.Font(family='Georgia', size=15)
        self.cbox_optionsList = ttk.Combobox(self, textvariable=self.option, values=options,
                                             font=custom_font, width=9)
        self.cbox_optionsList.state(["readonly"])

        self.label = ttk.Label(self, text=self.title)

        self.cbox_optionsList.grid(column=0, row=0)
        self.label.grid(column=0, row=1)

        self.cbox_optionsList.bind("<<ComboboxSelected>>", self.option_selected)
        self.controller.register(self, self.title)

    def option_selected(self, *args):
        if self.title == "class":
            self.controller.class_entered(self.option.get())
        if self.title == "race":
            self.controller.race_entered(self.option.get())

    def update_field(self, field, new_value):
        if field == self.title:
            self.option.set(new_value.name)


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


class HitDieBox(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.hitDie_string = StringVar()
        # Customize the fonts
        dieFont = font.Font(family='Georgia', size=15)

        self.lbl_die = ttk.Label(self, font=dieFont, justify='center',
                                 textvariable=self.hitDie_string)
        self.lbl_description = ttk.Label(self, text="Hit Die", justify='center')

        self.lbl_die.grid(column=0, row=0)
        self.lbl_description.grid(column=0, row=1)

        self.controller.register(self, "class")


    def update_field(self, field, new_value):
        if field == "class":
            self.hitDie_string.set("D" + new_value.hit_die)


class ArmorProficiencies(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        ttk.Label(self, text="Armor Proficiencies").grid(column=0, row=0, columnspan=4)

        self.light_proficiency = BooleanVar(value=FALSE)
        self.medium_proficiency = BooleanVar(value=FALSE)
        self.heavy_proficiency = BooleanVar(value=FALSE)
        self.shield_proficiency = BooleanVar(value=FALSE)

        rb_light = ttk.Radiobutton(self, text="Light Armor", state='disabled', variable=self.light_proficiency)
        rb_medium = ttk.Radiobutton(self, text="Medium Armor", state='disabled', variable=self.medium_proficiency)
        rb_heavy = ttk.Radiobutton(self, text="Heavy Armor", state='disabled', variable=self.heavy_proficiency)
        rb_shield = ttk.Radiobutton(self, text="Shields", state='disabled', variable=self.shield_proficiency)

        rb_light.grid(column=0, row=1)
        rb_medium.grid(column=1, row=1)
        rb_heavy.grid(column=2, row=1)
        rb_shield.grid(column=3, row=1)

        self.controller.register(self, "class")

    def update_field(self, field, new_value):
        if field == "class":
            # Check for light armor proficiency
            if new_value.armor_proficiencies.count("Light Armor") != 0:
                self.light_proficiency.set(TRUE)
            else:
                self.light_proficiency.set(FALSE)
            # Check for medium armor proficiency
            if new_value.armor_proficiencies.count("Medium Armor") != 0:
                self.medium_proficiency.set(TRUE)
            else:
                self.medium_proficiency.set(FALSE)
            # Check for heavy armor proficiency
            if new_value.armor_proficiencies.count("Heavy Armor") != 0:
                self.heavy_proficiency.set(TRUE)
            else:
                self.heavy_proficiency.set(FALSE)
                # Check for shield proficiency
            if new_value.armor_proficiencies.count("Shields") != 0:
                self.shield_proficiency.set(TRUE)
            else:
                self.shield_proficiency.set(FALSE)


class WeaponProficiencies(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        ttk.Label(self, text="Weapon Proficiencies").grid(column=0, row=0, columnspan=2)

        self.simple_proficiency = BooleanVar(value=FALSE)
        self.martial_proficiency = BooleanVar(value=FALSE)
        self.other_proficiency = StringVar()

        rb_simple = ttk.Radiobutton(self, text="Simple Weapons", state='disabled', variable=self.simple_proficiency)
        rb_martial = ttk.Radiobutton(self, text="Martial Weapons", state='disabled', variable=self.martial_proficiency)
        self.lbl_other = ttk.Label(self, text="Other Weapons", state='disabled', textvariable=self.other_proficiency)

        rb_simple.grid(column=0, row=1)
        rb_martial.grid(column=1, row=1)
        # lbl_other gets .grid when fields are updated

        self.controller.register(self, "class")

    def update_field(self, field, new_value):
        if field == "class":
            other_weapons = new_value.weapon_proficiencies

            # Check for simple weapon proficiency
            if new_value.weapon_proficiencies.count("Simple Weapons") != 0:
                self.simple_proficiency.set(TRUE)
                other_weapons.remove("Simple Weapons")
            else:
                self.simple_proficiency.set(FALSE)
            # Check for martial weapon proficiency
            if new_value.weapon_proficiencies.count("Martial Weapons") != 0:
                self.martial_proficiency.set(TRUE)
                other_weapons.remove("Martial Weapons")
            else:
                self.martial_proficiency.set(FALSE)
            # Other Weapon proficiencies, if none, do not show the label
            self.other_proficiency.set("Other Weapons: " + str(other_weapons))
            if len(other_weapons) > 1:
                self.lbl_other.grid(column=0, row=2, columnspan=2)
            else:
                self.lbl_other.grid_forget()


class ListProficiencies(ttk.Frame):
    def __init__(self, parent, description, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.description = description

        ttk.Label(self, text=description).grid(column=0, row=0)
        self.items_frame = ttk.Frame(self)
        self.items_frame.grid(column=0, row=1)

        ttk.Label(self.items_frame, text="None").grid(column=0, row=0)

        if self.description == "Tool Proficiencies":
            self.controller.register(self, "class")
        if self.description == "Language Proficiencies":
            self.controller.register(self, "race")

    def update_field(self, field, new_value):
        if field == "class":
            # Remove what is currently listed
            for child in self.items_frame.winfo_children():
                child.destroy()
            # List the new items
            for item in enumerate(new_value.tool_proficiencies):
                ttk.Label(self.items_frame, text=item[1]).grid(column=0, row=item[0])

        if field == "race":
            # Remove what is currently listed
            for child in self.items_frame.winfo_children():
                child.destroy()
            # List the new items
            for item in enumerate(new_value.languages):
                ttk.Label(self.items_frame, text=item[1]).grid(column=0, row=item[0])



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
