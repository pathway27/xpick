from tkinter import *
from tkinter.ttk import *

class App():
    def __init__(self, master):
        self.master = master
        self.master.title("UI")

        style = Style()
        style.configure("TButton", background='grey', borderwidth=2)
        style.configure("TLabel",  background='grey')
        style.configure("TFrame",  background='grey')

        self.frame = Frame(self.master, padding="20", borderwidth=16, relief='sunken')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid(column=0, row=0)

        self.search = StringVar()
        self.search_entry = Entry(self.frame, textvariable=self.search)
        self.search_entry.grid(row=1)
        self.search_entry.configure()

        self.combo = StringVar()
        one_two = ["One", "Two"]
        Combobox(self.frame, textvariable=self.combo, values=one_two).grid(row=2)

        Text(self.frame).grid(row=3)

        self.button_frame = Frame(self.frame, borderwidth=1, relief='sunken')
        self.button_frame.grid(row=5, column=0)

        Button(self.button_frame).grid(row=0, column=0, sticky="w")
        Button(self.button_frame).grid(row=0, column=1, sticky="s")
        Button(self.button_frame).grid(row=0, column=2, sticky="e")

        Label(self.button_frame, text="njnjn").grid(row=1)

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()