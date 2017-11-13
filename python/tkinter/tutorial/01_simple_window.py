# tkinter is a wrapper around tk amd tcl which is used to create windows
# and graphical user interfaces (GUIs)

# Import everything from tkinter
from tkinter import *


# Define the settings to create a window instance
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        #call the init_window function below
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("This is my tkinter app")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        clickMeButton = Button(self, text="Click me!")
        # placing the button on my window
        clickMeButton.place(x=0, y=0)
        # creating another button
        belowButton = Button(self, text="I'm down here")
        belowButton.place(x=0, y=100)
        # and yet one more
        middleButton = Button(self, text="In the middle")
        middleButton.place(x=200, y=150)

# Create the root window
root = Tk()

# define the size
root.geometry("400x300")

# create instance using the class that we created above
app = Window(root)
# Show the window and begin mainloop
root.mainloop()
