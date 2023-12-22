from tkinter import ttk

import CustomFrames

# This class is the primary ttk.Frame that houses all UI for the Window.
# There are 7 Frames inside of it, they are defined in Custom Frames
# They are each arranged specifically, using .grid columns and rows


class CharacterPage(ttk.Frame):
    def __init__(self, parent, character_information):
        ttk.Frame.__init__(self, parent)

        # Top Player Frame
        frm_player_information = CustomFrames.PlayerInformation(self)
        frm_player_information.grid(column=0, row=0, columnspan=3)

        # Left scores frame
        frm_scores = CustomFrames.Scores(self, character_information)
        frm_scores.grid(column=0, row=1, rowspan=4)

        # Bottom Left features frame
        frm_features = CustomFrames.Features(self)
        frm_features.grid(column=0, row=5)

        # Center Life frame
        frm_life = CustomFrames.Life(self)
        frm_life.grid(column=1, row=1, rowspan=2)

        # Center limits frame
        frm_limits = CustomFrames.Limits(self)
        frm_limits.grid(column=1, row=3)

        # Right proficiencies frame
        frm_proficiencies = CustomFrames.Proficiencies(self)
        frm_proficiencies.grid(column=2, row=1, rowspan=3)

        # Bottom Left options frame
        frm_options = CustomFrames.Options(self)
        frm_options.grid(column=1, row=4, columnspan=2, rowspan=2)
