from tkinter import *
from tkinter import ttk

import CharacterPage
import Character

from Model import Model
from View import View
from Controller import Controller


class Application:
    def __init__(self):
        self.window = Tk()
        self.window.title("Character Sheet")

        model = Model()


        view = View(self.window)
        view.character_page.grid(column=0, row=0, columnspan=2)


        controller = Controller(model, view)



        # Testing stuff
        ttk.Label(self.window, text="The Content of the SRD 5.1 may be distributed under The CC-BY-4.0 license.")\
            .grid(column=0, row=1)

        def test_button():
            print(model.character.ability_scores)
            print(model.character.ability_modifiers)
            print(model.character.skill_proficiencies)
        ttk.Button(self.window, text="Test", command=test_button).grid(column=1, row=1)

        # configure style
        self.window.style = ttk.Style(self.window)
        self.window.style.configure('TFrame', background="white")
        self.window.style.configure('TLabel', background="white")
        self.window.style.configure('TButton', background="white")
        self.window.style.configure('TRadiobutton', background="white")


if __name__ == '__main__':
    app = Application()
    app.window.mainloop()
