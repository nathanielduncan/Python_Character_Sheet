from tkinter import *
from tkinter import ttk

from Controller import Controller


class Application:
    def __init__(self):
        self.window = Tk()
        self.window.title("Character Sheet")

        # Define the controller, it contains the model and view
        # It acts as the go between for each
        controller = Controller(self.window)
        controller.show_main_menu()

        # Testing stuff
        ttk.Label(self.window, text="The Content of the SRD 5.1 may be distributed under The CC-BY-4.0 license.")\
            .grid(column=0, row=1)

        def test_button():
            pass
        ttk.Button(self.window, text="Test", command=test_button).grid(column=1, row=1)


if __name__ == '__main__':
    app = Application()
    app.window.mainloop()
