from tkinter import *
from tkinter import ttk

import CharacterPage
import Character


def run_program():
    character_information = Character.CharacterData()

    window = Tk()
    window.title("Character Sheet")
    main_frame = CharacterPage.CharacterPage(window, character_information)
    main_frame.grid(column=0, row=0, columnspan=2)

    ttk.Label(window, text="The Content of the SRD 5.1 may be distributed under The CC-BY-4.0 license.")\
        .grid(column=0, row=1)

    def test_button():
        print(character_information.ability_scores)
    ttk.Button(window, text="Test", command=test_button).grid(column=1, row=1)

    # configure style
    window.style = ttk.Style(window)
    window.style.configure('TFrame', background="white")
    window.style.configure('TLabel', background="white")
    window.style.configure('TButton', background="white")
    window.style.configure('TRadiobutton', background="white")

    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_program()
