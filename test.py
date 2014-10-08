import wx

class MyFrame(wx.Frame):
   def __init__(self, parent, ID, title):
       wx.Frame.__init__(self, parent, ID, title, size=(300, 250))

       panel1 = wx.Panel(self,-1, style=wx.SUNKEN_BORDER)
       panel2 = wx.Panel(self,-1, style=wx.SUNKEN_BORDER)
       panel3 = wx.Panel(self,-1, style=wx.SUNKEN_BORDER)

       panel1.SetBackgroundColour("BLUE")
       panel2.SetBackgroundColour("RED")
       panel3.SetBackgroundColour("GREEN")

       vbox = wx.BoxSizer(wx.VERTICAL)
       vbox.Add(panel3,3)
       vbox_inner = wx.BoxSizer(wx.VERTICAL)
       vbox.Add(vbox_inner,1,wx.EXPAND)
       vbox_inner.Add(panel1, 2, wx.EXPAND)
       vbox_inner.Add(panel2, 1, wx.EXPAND)

       # hbox = wx.BoxSizer(wx.HORIZONTAL)
       # hbox.Add(vbox,-1)
       self.SetAutoLayout(True)
       self.SetSizer(vbox)
       self.Layout()


app = wx.PySimpleApp()
frame = MyFrame(None, -1, "Sizer Test")
frame.Show()
app.MainLoop()