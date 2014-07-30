from tkinter import *
from tkinter.ttk import *

class App():
    def __init__(self, master):
        self.master = master
        self.master.title("UI")

        self.frame = Frame(self.master, padding="20", borderwidth=16, relief='sunken')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.search = StringVar()
        self.search_entry = Entry(self.frame, width=20, textvariable=self.search)
        self.search_entry.grid(row=1, columnspan=4, sticky=N+S+E+W)

        self.combo = StringVar()
        one_two = ["One", "Two"]
        Combobox(self.frame, width=20, textvariable=self.combo, values=one_two).grid(row=2, columnspan=4)

        Text(self.frame).grid(row=3, columnspan=3)

        Button(self.frame).grid(row=4, column=0)
        Button(self.frame).grid(row=4, column=1)
        Button(self.frame).grid(row=4, column=2)

        Label(self.frame, text="njnjn").grid(row=5)

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()