"""Get the tkinter functions for our GUI."""
from tkinter import *


def create_app(master):
    """Create a Window with labels and buttons."""
    global label
    label = Label(master, text="Hello, Buttons!")
    label.grid(row=0, column=0, columnspan=2)

    Button(master, text="Spanish",
           command=spanish_hello).grid(row=1, column=0)

    Button(master, text="Italian",
           command=italian_hello).grid(row=1, column=1)


def spanish_hello():
    """Change the label to spanish greeting."""
    global label
    label.config(text="Hola, Buttons!")


def italian_hello():
    """Change the label to Italian greeting."""
    global label
    label.config(text="Ciao, Buttons!")


def main():
    """Main app."""
    root = Tk()
    create_app(root)
    root.mainloop()


if __name__ == "__main__":
    main()
