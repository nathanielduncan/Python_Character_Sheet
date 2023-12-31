from tkinter import ttk

import CharacterPage


class View:
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller

        # configure style
        self.window.style = ttk.Style(self.window)
        self.window.style.configure('TFrame', background="white")
        self.window.style.configure('TLabel', background="white")
        self.window.style.configure('TButton', background="white")
        self.window.style.configure('TRadiobutton', background="white")

        # Once the controller gets created, set_controller defines both of these
        self.character_page = CharacterPage.CharacterPage(self.window, self.controller)
        self.character_page.grid(column=0, row=0)
