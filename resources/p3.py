from tkinter import *
from tkinter.ttk import *

from xparser import ConfigParserMultiOpt
from autocompleteentry import AutoCompleteEntry
print(sys.version)
import queue, threading, re

class App():
    def __init__(self, master):

        self.master = master
        self.load_config()
        self.master.title("xPick")

        self.frame = Frame(self.master, padding="20", borderwidth=16, relief='sunken')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        Label(self.frame, text="WEST 1,1").grid(column=1, row=1, sticky=W)
        Label(self.frame, text="WEST 1,2").grid(column=2, row=1, sticky=W)
        Label(self.frame, text="WEST 1,3").grid(column=3, row=1, sticky=W)

        self.search = StringVar()
        self.search_entry = Entry(self.frame, width=20, textvariable=self.search)
        self.search_entry.grid(row=5, rowspan=4, sticky=N+S+E+W)

        
        Label(self.frame).grid(column=2, row=2, sticky=(W, E))
        self.game_details = Text(self.frame)
        self.game_details.grid(column=1, row=10, sticky=W)

        Label(self.frame, text="").grid(column=1, row=2, sticky=E)
        Label(self.frame, text="").grid(column=3, row=2, sticky=W)

        search2 = StringVar()
        def callback(sv):
            game = self.xfile.get_game(sv.get())
            if game is not None:
                self.game_details.insert('1.0', game)


        #vcmd = (self.master.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        #search_entry2 = Entry(self.frame, textvariable=search2, validate="key", validatecommand=vcmd)
        
        self.search_entry2 = AutoCompleteEntry([], self.frame, listboxLength=6, width=64, matchesFunction=self.matches)
        self.search_entry2.var.trace("w", lambda name, index, mode, sv=self.search_entry2.var: callback(sv))


        self.search_entry2.configure(foreground='green')
        self.search_entry2.grid(column=1, row=4, columnspan=4, sticky=N+S+E+W)
        self.search_entry2.focus()

        
        self.canvas = Canvas(self.frame)
        self.canvas.create_text(20, 30, anchor=W, font="Purisa", text="Most relationships seem so transitory")
        self.canvas.grid(column=1, row=6, columnspan = 4, sticky=N+S+E+W)

        self.progress = Progressbar(self.frame)
        self.progress.grid(column=1, row=7, columnspan = 4, sticky=N+S+E+W)
        self.progress.start()

        self.xversion = Label(self.frame)
        self.xversion.grid(column=4, row=9, columnspan=4, sticky=(W, E))
        #print(self.xversion)

        for child in self.frame.winfo_children(): child.grid_configure(padx=5, pady=5)
        # root.bind('<Return>', calculate)

    def matches(self, fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)

    def OnValidate(self, d, i, P, s, S, v, V, W):
        #print("OnValidate:")
        #print("d='%s'" % d)
        #print("i='%s'" % i)
        print("P='%s'" % P)
        self.search.set(P)
        #print(self.xfile.get('2', 'InGameRenderer'))
        #print("s='%s'" % s)
        #print("S='%s'" % S)
        #print("v='%s'" % v)
        #print("V='%s'" % V)
        #print("W='%s'" % W)
        # only allow if the string is lowercase
        return (S.lower() == S)

    def load_config(self):
        #tkmessagebox.showinfo("Popup", "Hello!")
        self.queue = queue.Queue()
        ThreadedTask(self.queue).start()
        self.master.after(100, self.process_queue)

        #self.process_queue

    def process_queue(self):
        try:
            self.xfile = self.queue.get(0)
            self.progress.grid_forget()
            self.xversion.config(text= 'XFile Version: ' + self.xfile.get('Version', 'Version'))
            #print(self.xfile.get_names()[0])
            self.search_entry2.autocompleteList = self.xfile.get_names()
            #print(self.search_entry2.width)
            #self.search_entry2.listboxLength = 
            # Show result of the task if needed
            #self.prog_bar.stop()
        except queue.Empty:
            self.master.after(100, self.process_queue)
            #self.process_queue

    
class ThreadedTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        print("Started Read")
        xfile = "xfire_games.ini"
        config = ConfigParserMultiOpt()
        config.read(xfile, encoding='utf-8-sig')
        print("Finished Read")
        self.queue.put(config)
        print(self.queue.qsize())
    
if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()