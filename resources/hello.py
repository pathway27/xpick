#!c:\Python34\python.exe
import os
import sys
print(sys.version)
import wx


class MyWindow(wx.Frame):
    """ Deriving a new Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 500), style=wx.SIMPLE_BORDER )
        self.Centre()
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()

        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About",
                                    "Information About this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Exit")
        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open a file")

        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "A small text editor",
                               "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self, e):
        """ Open a file """
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*",
                            wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

app = wx.App(False)
frame = MyWindow(None, 'Editor1')
app.MainLoop()
