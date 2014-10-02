import wx
import csv
import logging
import _mysql

pth_book = "C:\Users\deryarno\Desktop\Reports\data sources\Bookings.csv"
pth_forecast = "C:\Users\deryarno\Desktop\Reports\data sources\Forecast Bookings.csv"

sqltbl_book = "book"
sqltbl_forecast = "fcp"

OPTIONS_ID = wx.NewId()

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
        self.pnl_Main = wx.Panel(self)
        self.bx_Main = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_bookings = wx.Button(self.pnl_Main,-1,'Bookings')
        self.bx_Main.Add(self.btn_bookings)
        self.Bind(wx.EVT_BUTTON, self.ProcessBookings)
        self.pnl_Main.SetSizer(self.bx_Main)


    def ProcessBookings(self, event):
        logging.error("processing bookings...")
        #try:
        self.ImportCSV(pth_book,sqltbl_book)
        #except Exception as e:
        #    logging.error("Error: " + str(e))

        #try:
        self.ImportCSV(pth_forecast,sqltbl_forecast)
        #except Exception as e:
        #    logging.error("Error: " + str(e))

            

    def ImportCSV(self,pth,table):
        logging.error("Importing CSV at '" + pth + "' to table '" + table + "'")
        with open(pth,'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            columns = next(reader)
            entries = []
            total = 0
    
            for entry in reader:
                row = self.Entry()
                total += 1
                for i in range(len(columns)):
                    setattr(row,columns[i],entry[i])
                entries.append(row)
                if len(entries) == 10:
                    self.LoadSQL(entries,table)
                    entries = []
    
            print "done adding " + str(total) + " entries"
    
    def LoadSQL(self,entries,table):
        #con = _mysql.connect()
#
        ##clean table
        #cmd = "DELETE * FROM " + table
        #con.executescript(cmd)

        #add entries to table
        cmd = "INSERT INTO " + table + "("
        sample = entries[0]
        try:
            attributes = [a for a in dir(sample) if not a.startswith('__') and not callable(getattr(sample,a))]
        except Exception as e:
            logging.error("haha didnt work")
        for col in attributes:
            cmd += col
            if col != attributes[-1]:
                cmd += ","

        cmd += ") VALUES "
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

        logging.error("YOUR SQL COMMAND: ")
        logging.error(cmd)

        #con.query("SELECT VERSION()")
        #result = con.use_result()
#
        #print result

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
    #ImportCSV(pth_book,"book")