from tkinter import ttk

import CharacterPage
import MainMenu


class View:
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller

        # Now the views can be created
        self.character_page = CharacterPage.CharacterPage(self.window, self.controller)
        self.main_menu = MainMenu.MainMenu(self.window, self.controller)

        # configure style
        self.window.style = ttk.Style(self.window)
        self.window.style.configure('TFrame', background="white")
        self.window.style.configure('TLabel', background="white")
        self.window.style.configure('TButton', background="white")
        self.window.style.configure('TRadiobutton', background="white")

    def show_character_page(self):
        self.main_menu.grid_forget()
        self.character_page.grid(column=0, row=0)
        self.center_window()

    def show_main_menu(self):
        self.character_page.grid_forget()
        self.main_menu.grid(column=0, row=0)
        self.center_window()

    def center_window(self):
        self.window.update_idletasks()

        # Tkinter way to find the screen resolution
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        size = tuple(int(_) for _ in self.window.geometry().split('+')[0].split('x'))
        x = screen_width / 2 - size[0] / 2
        y = screen_height / 2 - size[1] / 2

        self.window.geometry("+%d+%d" % (x, y))
