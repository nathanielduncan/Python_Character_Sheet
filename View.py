from tkinter import ttk

import CharacterPage


class View:
    def __init__(self, window):
        self.character_page = CharacterPage.CharacterPage(window)
