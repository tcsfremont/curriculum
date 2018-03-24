from tkinter import *


class Calculator(Frame):
    """A class used to create an interactive calculator
     on the screen."""
    def __init__(self, master, *args, **kwargs):
        """Calculator constructor."""
        Frame.__init__(self, master, *args, **kwargs)
        self.create_elements()

    def appendToDisplay(self, text):
        self.entryText = self.screen.get()
        self.textLength = len(self.entryText)

        self.screen.insert(self.textLength, text)


    def replaceText(self, text):
        self.screen.delete(0, END)
        self.screen.insert(0, text)

    def clearScreen(self):
        self.replaceText("0")

    def calculate(self):
        self.calculation = self.screen.get()
        self.result = eval(self.calculation)

        self.replaceText(self.result)

    def create_elements(self):
        """Function to add all the widgets to the calculator window."""
        self.screen = Entry(self, font=("Courier", 16), relief=RAISED,
                            justify=RIGHT)
        self.screen.insert(0, "0")
        self.screen.grid(row=0, column=0, columnspan=5)

#       Top row buttons
        self.buttonSeven = Button(self, font=("Courier", 11), text="7", command=lambda: self.appendToDisplay("7"))
        self.buttonSeven.grid(row=1, column=0, sticky=NSEW)
        self.buttonEight = Button(self, font=("Courier", 11), text="8")
        self.buttonEight.grid(row=1, column=1, sticky=NSEW)
        self.buttonNine = Button(self, font=("Courier", 11), text="9")
        self.buttonNine.grid(row=1, column=2, sticky=NSEW)
        self.buttonMul = Button(self, font=("Courier", 11), text="x", command=lambda: self.appendToDisplay("*"))
        self.buttonMul.grid(row=1, column=3, sticky=NSEW)

#       Second row buttons
        self.buttonFour = Button(self, font=("Courier", 11), text="4")
        self.buttonFour.grid(row=2, column=0, sticky=NSEW)
        self.buttonFive = Button(self, font=("Courier", 11), text="5")
        self.buttonFive.grid(row=2, column=1, sticky=NSEW)
        self.buttonSix = Button(self, font=("Courier", 11), text="6")
        self.buttonSix.grid(row=2, column=2, sticky=NSEW)
        self.buttonSub = Button(self, font=("Courier", 11), text="-")
        self.buttonSub.grid(row=2, column=3, sticky=NSEW)

#       Third row buttons
        self.buttonOne = Button(self, font=("Courier", 11), text="1")
        self.buttonOne.grid(row=3, column=0, sticky=NSEW)
        self.buttonTwo = Button(self, font=("Courier", 11), text="2")
        self.buttonTwo.grid(row=3, column=1, sticky=NSEW)
        self.buttonThree = Button(self, font=("Courier", 11), text="3")
        self.buttonThree.grid(row=3, column=2, sticky=NSEW)
        self.buttonAdd = Button(self, font=("Courier", 11), text="+")
        self.buttonAdd.grid(row=3, column=3, sticky=NSEW)

#       Bottom row buttons
        self.buttonZero = Button(self, font=("Courier", 11), text="0")
        self.buttonZero.grid(row=4, column=0, columnspan=2, sticky=NSEW)
        self.buttonClear = Button(self, font=("Courier", 11), text="C", command= lambda: self.clearScreen())
        self.buttonClear.grid(row=4, column=2, sticky=NSEW)
        self.buttonEqu = Button(self, font=("Courier", 11), text="=", command = lambda: self.calculate())
        self.buttonEqu.grid(row=4, column=3, sticky=NSEW)


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
