from tkinter import *


class Calculator(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


def main():
    """Main function."""
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)
    app = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
