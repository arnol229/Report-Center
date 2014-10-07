import wx
import csv
import logging
import _mysql

pth_book = "C:\Users\deryarno\Desktop\Reports\data sources\Bookings.csv"
pth_forecast = "C:\Users\deryarno\Desktop\Reports\data sources\Forecast Bookings.csv"

sqltbl_book = "book"
sqltbl_forecast = "fcp"

OPTIONS_ID = wx.NewId()

class SubFrame(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,parent=None,title=title,size=(200,300))
        self.pnl_Msg = wx.Panel(self)
        self.hbx_Msg = wx.BoxSizer(wx.HORIZONTAL)
        self.size = wx.StaticText(self.pnl_Msg,-1,"0")
        self.update = wx.StaticText(self.pnl_Msg,-1,"0")
        self.hbx_Msg.Add(self.size)
        self.hbx_Msg.Add(self.update)

        self.vbx_Msg = wx.BoxSizer(wx.VERTICAL)
        self.vbx_Msg.Add(self.hbx_Msg,0,flag=wx.CENTER)
        self.pnl_Msg.SetSizer(self.vbx_Msg)
        #self.vbx_Msg.Fit(self)

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
        self.ProgressFrame = SubFrame(title="Bookings Refresh")
        self.ProgressFrame.Show()
        logging.error("processing bookings...")
        try:
            self.ImportCSV(pth_book,sqltbl_book)
        except Exception as e:
            logging.error("Error: " + str(e))

        try:
            self.ImportCSV(pth_forecast,sqltbl_forecast)
        except Exception as e:
            logging.error("Error: " + str(e))
        self.ProgressFrame.Destroy()

            

    def ImportCSV(self,pth,table):
        logging.error("Importing CSV at '" + pth + "' to table '" + table + "'")
        with open(pth,'rb') as csvfile:
            data = csv.reader(csvfile,delimiter=',')
            columns = data.next()
            print type(data)
            # columns = ["ha","yo","what","no","hur dur"]
            # total = data
            # total = str(len(list(total)))
            # self.ProgressFrame.size.SetValue(total)
            entries = []
            i = 0

            for entry in data:
                row = self.Entry()
                for i in range(len(columns)):
                    setattr(row,columns[i],entry[i])
                # logging.error('appending row')
                entries.append(row)
                i += 1
                # self.ProgressFrame.update.SetValue(str(i))
                if len(entries) == 10000:
                    logging.error('loading SQL with 10000 entries')
                    print vars(entries[0])
                    self.LoadSQL(entries,table)
                    entries = []
            print columns
            print data
            print i
            # print "done adding " + total + " entries"
        csvfile.close()

    def LoadSQL(self,entries,table):
        con = _mysql.connect('localhost')
        cursor = con.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        logging.error(data)
        con.close()
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