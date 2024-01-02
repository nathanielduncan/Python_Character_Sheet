from tkinter import ttk


class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        ttk.Label(self, text="Welcome to the program").grid(column=0, row=0)
        ttk.Button(self, text="Create new Character", command=self.controller.show_character_page).grid(column=0, row=1)
