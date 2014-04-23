# import tkmessagebox
from tkinter import *
from tkinter.ttk import *

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("xPick")

        self.frame = Frame(self.root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        search = StringVar()
        search_entry = Entry(self.frame, width=20, textvariable=search)
        search_entry.grid(column=2, row=1, ipadx=10, sticky=(E, W))

        
        Label(self.frame).grid(column=2, row=2, sticky=(W, E))
        Button(self.frame, text="Calculate").grid(column=3, row=3, sticky=(E, S))

        Label(self.frame, text="").grid(column=3, row=1, sticky=W)
        Label(self.frame, text="").grid(column=1, row=2, sticky=E)
        Label(self.frame, text="").grid(column=3, row=2, sticky=W)
        

        for child in self.frame.winfo_children(): child.grid_configure(padx=5, pady=5)

        search_entry.focus()
        # root.bind('<Return>', calculate)

    def hello(self):
        tkmessagebox.showinfo("Popup", "Hello!")

app = App()
app.root.mainloop()