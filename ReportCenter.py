import wx
import csv
import logging
import _mysql

pth_book = "C:\Users\deryarno\Desktop\Reports\data sources\Bookings.csv"
pth_forecast = "C:\Users\deryarno\Desktop\Reports\data sources\Forecast Bookings.csv"

sqltbl_book = "book"
sqltbl_forecast = "fcp"

OPTIONS_ID = wx.NewId()

class ProgressFrame(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,parent=None,title=title,size=(400,400))
        #self.pnl_main = wx.Panel(self)
        self.pnl_current = wx.Panel(self)
        self.pnl_size = wx.Panel(self)
        self.pnl_msg = wx.Panel(self)

        self.pnl_current.SetBackgroundColour("RED")
        self.pnl_msg.SetBackgroundColour("BLUE")
        self.pnl_size.SetBackgroundColour("GREEN")

        self.vbx_main = wx.BoxSizer(wx.VERTICAL)
        self.hbx_progress = wx.BoxSizer(wx.HORIZONTAL)
        self.hbx_msg = wx.BoxSizer(wx.HORIZONTAL)

        self.current = wx.StaticText(self.pnl_current,-1,"0")
        self.size = wx.StaticText(self.pnl_size,-1,"1")
        self.msg = wx.StaticText(self.pnl_msg,-1,label="Working...")

        self.vbx_main.Add(self.hbx_progress)
        self.vbx_main.Add(self.hbx_msg)
        self.hbx_progress.Add(self.pnl_current)
        self.hbx_progress.Add(self.pnl_size)
        self.hbx_msg.Add(self.pnl_msg)

        self.SetSizer(self.vbx_main,wx.EXPAND)
        self.SetAutoLayout(True)
        self.vbx_main.Fit(self)

    def ErrorExit(self):
        self.Destroy()
    
    def ShowError(self,error):
        self.msg.SetLabel(str(error))
        # self.Layout()
        
        # self.pnl_error = wx.Panel(self)
        # self.btn_error = wx.Button(self.pnl_error,-1,"Ok")
        # self.hbx_error = wx.BoxSizer(wx.HORIZONTAL)
        # self.hbx_error.Add(self.btn_error)
        # self.error = wx.StaticText(self.pnl_error,-1,str(error))
        # self.Bind(wx.EVT_BUTTON, self.Destroy(), self.btn_error)
    def complete(self):
        self.Destroy()

class Frame(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,parent=None,title=title, id=-1,size=(300,300))
    
        ## Create Menu
        self.menubar = wx.MenuBar()
        self.menu = wx.Menu()
        self.m_Fexit = self.menu.Append(wx.ID_EXIT, 'Exit', "Exit")
        self.m_Foptions = self.menu.Append(OPTIONS_ID, 'Options','Edit Options')
        self.menubar.Append(self.menu, '&File')
        self.SetMenuBar(self.menubar)
        self.Bind(wx.EVT_MENU, self.OnOptions, self.m_Foptions)
        self.Bind(wx.EVT_MENU, self.OnExit, self.m_Fexit)
    
        ## Create Main Panel
        self.pnl_main = wx.Panel(self)
        self.bx_main = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_bookings = wx.Button(self.pnl_main,-1,'Bookings')
        self.bx_main.Add(self.btn_bookings)
        self.Bind(wx.EVT_BUTTON, self.ProcessBookings, self.btn_bookings)
        self.btn_clarity = wx.Button(self.pnl_main,-1,'Clarity')
        self.Bind(wx.EVT_BUTTON, self.ProcessClarity, self.btn_clarity)
        self.bx_main.Add(self.btn_clarity)
        self.pnl_main.SetSizer(self.bx_main)

    def ProcessClarity(self, event):
        pass

    def ProcessBookings(self, event):
        self.StatusFrame = ProgressFrame(title="Bookings Refresh")
        self.StatusFrame.Show()
        logging.error("processing bookings...")
        try:
            self.ImportCSV(pth_book,sqltbl_book)
        except Exception as e:
            self.StatusFrame.ShowError(e)

        try:
            self.ImportCSV(pth_forecast,sqltbl_forecast)
        except Exception as e:
            logging.error("Error: " + str(e))
        self.StatusFrame.complete()

            

    def ImportCSV(self,pth,table):
        logging.error("Importing CSV at '" + pth + "' to table '" + table + "'")
        #Get the total number of rows to show progress.
        with open(pth,'rb') as csvfile:
            data = csv.reader(csvfile,delimiter=',')
            rows = list(data)
            total = len(rows)
            self.StatusFrame.size.SetLabel(str(total))
            print str(total)

        with open(pth,'rb') as csvfile:
            data = csv.reader(csvfile,delimiter=',')
            columns = data.next()

            ### why does getting the total rows below cause data to become empty?
            ### is it iterating through and 'using up' the csv?
            # rows = list(data)
            # total = len(rows)
            # self.StatusFrame.size.SetLabel(str(total))
            # print str(total)

            entries = []
            i = 0

            for entry in data:
                row = self.Entry()
                for pos in range(len(columns)):
                    setattr(row,columns[pos],entry[pos])
                # logging.error('appending row')
                entries.append(row)
                i += 1
                self.StatusFrame.current.SetLabel(str(i))
                if len(entries) == 10000:
                    logging.error('loading SQL with 10000 entries')
                    # print vars(entries[0])
                    self.LoadSQL(entries,table)
                    entries = []
            logging.error('loading SQL with the remaining ' + str(len(entries)) + ' entries.')
            self.LoadSQL(entries,table)
            print columns
            print data
            print i
            # print "done adding " + total + " entries"

    def LoadSQL(self,entries,table):
        # con = _mysql.connect('localhost')
        # cursor = con.cursor()
        # cursor.execute("SELECT VERSION()")
        # data = cursor.fetchone()
        # logging.error(data)
        # con.close()
#
        ##clean table
        #cmd = "DELETE * FROM " + table
        #con.executescript(cmd)

        #add entries to table
        cmd = "INSERT INTO " + table + "("
        sample = entries[0]
        attributes = [a for a in dir(sample) if not a.startswith('__') and not callable(getattr(sample,a))]

        #extract individual attributes to put in sql statement
        for col in attributes:
            cmd += col
            if col != attributes[-1]:
                cmd += ","
        cmd += ") VALUES "

        #create SQL row statement for each object
        for entry in entries:
            cmd += "("
            for col in attributes:
                cmd += str(getattr(entry,str(col)))
                if col != attributes[-1]:
                    cmd += ","
                else:
                    cmd += ")"
                    if entry != entries[-1]:
                        cmd += ','

        #logging.error("YOUR SQL COMMAND: ")
        #logging.error(cmd)

        #execute SQL cmd and close connection
        #con.execute(cmd)
        #con.close()

    def OnExit(self, event):
        self.Destroy()

    def OnOptions(self, event):
        pass

    class Entry(object):
        pass

logging.error(__name__)
if __name__ == '__main__':
    logging.error("welcome to Report Center")
    app = wx.App()
    app.main = Frame("Report Center")
    app.main.Show()
    app.MainLoop()