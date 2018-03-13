from tkinter import *


class Calculator(Frame):
    """A class used to create an interactive calculator
     on the screen."""
    def __init__(self, master, *args, **kwargs):
        """Calculator constructor."""
        Frame.__init__(self, master, *args, **kwargs)
        self.createElements()

    def createElements(self):
        """Function to add all the widgets to the calculator window."""
        self.screen = Entry(self, font=("Courier", 16), relief=RAISED,
                            justify=RIGHT)
        self.screen.insert(0, "0")
        self.screen.grid(row=0, column=0, columnspan=4)

#       Top row buttons
        self.buttonSeven = Button(self, font=("Courier", 11), text="7")
        self.buttonSeven.grid(row=1, column=0, sticky=NSEW)
        self.buttonEight = Button(self, font=("Courier", 11), text="8")
        self.buttonEight.grid(row=1, column=1, sticky=NSEW)
        self.buttonNine = Button(self, font=("Courier", 11), text="9")
        self.buttonNine.grid(row=1, column=2, sticky=NSEW)
        self.buttonMult = Button(self, font=("Courier", 11), text="x")
        self.buttonMult.grid(row=1, column=3, sticky=NSEW)

#       Second row buttons
        self.buttonSeven = Button(self, font=("Courier", 11), text="4")
        self.buttonSeven.grid(row=2, column=0, sticky=NSEW)
        self.buttonEight = Button(self, font=("Courier", 11), text="5")
        self.buttonEight.grid(row=2, column=1, sticky=NSEW)
        self.buttonNine = Button(self, font=("Courier", 11), text="6")
        self.buttonNine.grid(row=2, column=2, sticky=NSEW)
        self.buttonMult = Button(self, font=("Courier", 11), text="-")
        self.buttonMult.grid(row=2, column=3, sticky=NSEW)

#       Third row buttons
        self.buttonSeven = Button(self, font=("Courier", 11), text="1")
        self.buttonSeven.grid(row=3, column=0, sticky=NSEW)
        self.buttonEight = Button(self, font=("Courier", 11), text="2")
        self.buttonEight.grid(row=3, column=1, sticky=NSEW)
        self.buttonNine = Button(self, font=("Courier", 11), text="3")
        self.buttonNine.grid(row=3, column=2, sticky=NSEW)
        self.buttonMult = Button(self, font=("Courier", 11), text="+")
        self.buttonMult.grid(row=3, column=3, sticky=NSEW)

#       Bottom row buttons
        self.buttonSeven = Button(self, font=("Courier", 11), text="0")
        self.buttonSeven.grid(row=4, column=0, columnspan=2, sticky=NSEW)
        self.buttonEight = Button(self, font=("Courier", 11), text="C")
        self.buttonEight.grid(row=4, column=2, sticky=NSEW)
        self.buttonNine = Button(self, font=("Courier", 11), text="=")
        self.buttonNine.grid(row=4, column=3, sticky=NSEW)

def main():
    """Main function."""
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)
    app = Calculator(root)
#   Use Grid layout manager
    app.grid()
    root.mainloop()

if __name__ == '__main__':
    main()
