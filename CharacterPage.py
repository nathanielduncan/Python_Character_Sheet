from tkinter import ttk

import CustomFrames

# This class is the primary ttk.Frame that houses all UI for the Window.
# There are 7 Frames inside of it, they are defined in Custom Frames
# They are each arranged specifically, using .grid columns and rows


class CharacterPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        # Top Player Frame
        self.frm_player_information = CustomFrames.PlayerInformation(self, self.controller)
        self.frm_player_information.grid(column=0, row=0, columnspan=3)

        # Left scores frame
        self.frm_scores = CustomFrames.Scores(self)
        self.frm_scores.grid(column=0, row=1, rowspan=4)

        # Bottom Left features frame
        self.frm_features = CustomFrames.Features(self)
        self.frm_features.grid(column=0, row=5)

        # Center Life frame
        self.frm_life = CustomFrames.Life(self)
        self.frm_life.grid(column=1, row=1, rowspan=2)

        # Center limits frame
        self.frm_limits = CustomFrames.Limits(self)
        self.frm_limits.grid(column=1, row=3)

        # Right proficiencies frame
        self.frm_proficiencies = CustomFrames.Proficiencies(self)
        self.frm_proficiencies.grid(column=2, row=1, rowspan=3)

        # Bottom Left options frame
        self.frm_options = CustomFrames.Options(self)
        self.frm_options.grid(column=1, row=4, columnspan=2, rowspan=2)
