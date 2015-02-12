# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Report-Center.ui'
#
# Created: Wed Feb 11 11:27:27 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import pickle
import urllib2
import csv
import xml.etree.ElementTree as ET
from datetime import datetime


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        #Init widget and setup ui that is generated from PyQt
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        ## Instantiate variables ##
        self.settings = None
        self.conn = None
        self.serverParams = None
        self.cur = None
        self.orgChartURL = 'https://labtools.cisco.com/general/orgchart.php?tops=kip&format=csv'
        self.clarityUrl = 'http://ppm-prod-int:8888/ppmws/api/resources/resourceById/'
        self.username = None
        self.password = None

        ## Bind buttons input fields ##
        self.bindEvents()
        ## Get User Settings ##
        self.getUserSettings()
        ## Establish connection to Database ##
        self.setConnection()
        ## 
        self.retrieveTableData()

    def setupUi(self, MainWindow):
    	"""
    	QT Design code to set up ui.
    	used pyqtc4 to convert the .ui file to python
    	"""
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(552, 548)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Main_Tab = QtGui.QTabWidget(self.centralwidget)
        self.Main_Tab.setObjectName(_fromUtf8("Main_Tab"))
        self.Reports = QtGui.QWidget()
        self.Reports.setObjectName(_fromUtf8("Reports"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.Reports)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Reports_TabWidget = QtGui.QTabWidget(self.Reports)
        self.Reports_TabWidget.setEnabled(True)
        self.Reports_TabWidget.setObjectName(_fromUtf8("Reports_TabWidget"))
        self.Clarity = QtGui.QWidget()
        self.Clarity.setObjectName(_fromUtf8("Clarity"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Clarity)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Reports_Clarity_HBox_Top = QtGui.QHBoxLayout()
        self.Reports_Clarity_HBox_Top.setObjectName(_fromUtf8("Reports_Clarity_HBox_Top"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Reports_Clarity_HBox_Top.addItem(spacerItem)
        self.Reports_Clarity_Btn_Excel = QtGui.QPushButton(self.Clarity)
        self.Reports_Clarity_Btn_Excel.setObjectName(_fromUtf8("Reports_Clarity_Btn_Excel"))
        self.Reports_Clarity_HBox_Top.addWidget(self.Reports_Clarity_Btn_Excel)
        self.Reports_Clarity_Btn_Tableau = QtGui.QPushButton(self.Clarity)
        self.Reports_Clarity_Btn_Tableau.setObjectName(_fromUtf8("Reports_Clarity_Btn_Tableau"))
        self.Reports_Clarity_HBox_Top.addWidget(self.Reports_Clarity_Btn_Tableau)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Reports_Clarity_HBox_Top.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.Reports_Clarity_HBox_Top)
        self.Reports_Clarity_Scroll = QtGui.QScrollArea(self.Clarity)
        self.Reports_Clarity_Scroll.setWidgetResizable(True)
        self.Reports_Clarity_Scroll.setObjectName(_fromUtf8("Reports_Clarity_Scroll"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 474, 308))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Reports_Clarity_Text = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.Reports_Clarity_Text.setReadOnly(True)
        self.Reports_Clarity_Text.setObjectName(_fromUtf8("Reports_Clarity_Text"))
        self.horizontalLayout_3.addWidget(self.Reports_Clarity_Text)
        self.Reports_Clarity_Scroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.Reports_Clarity_Scroll)
        self.Reports_Clarity_HBox_Bottom = QtGui.QHBoxLayout()
        self.Reports_Clarity_HBox_Bottom.setObjectName(_fromUtf8("Reports_Clarity_HBox_Bottom"))
        self.Reports_Clarity_Btn_Refresh = QtGui.QPushButton(self.Clarity)
        self.Reports_Clarity_Btn_Refresh.setObjectName(_fromUtf8("Reports_Clarity_Btn_Refresh"))
        self.Reports_Clarity_HBox_Bottom.addWidget(self.Reports_Clarity_Btn_Refresh)
        self.Reports_Clarity_ProgressBar = QtGui.QProgressBar(self.Clarity)
        self.Reports_Clarity_ProgressBar.setProperty("value", 0)
        self.Reports_Clarity_ProgressBar.setObjectName(_fromUtf8("Reports_Clarity_ProgressBar"))
        self.Reports_Clarity_HBox_Bottom.addWidget(self.Reports_Clarity_ProgressBar)
        self.verticalLayout_2.addLayout(self.Reports_Clarity_HBox_Bottom)
        self.Reports_TabWidget.addTab(self.Clarity, _fromUtf8(""))
        self.Bookings = QtGui.QWidget()
        self.Bookings.setObjectName(_fromUtf8("Bookings"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Bookings)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.Reports_Bookings_HBox_Top = QtGui.QHBoxLayout()
        self.Reports_Bookings_HBox_Top.setObjectName(_fromUtf8("Reports_Bookings_HBox_Top"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Reports_Bookings_HBox_Top.addItem(spacerItem2)
        self.Reports_Bookings_Btn_Excel = QtGui.QPushButton(self.Bookings)
        self.Reports_Bookings_Btn_Excel.setObjectName(_fromUtf8("Reports_Bookings_Btn_Excel"))
        self.Reports_Bookings_HBox_Top.addWidget(self.Reports_Bookings_Btn_Excel)
        self.Reports_Bookings_Btn_Tableau = QtGui.QPushButton(self.Bookings)
        self.Reports_Bookings_Btn_Tableau.setObjectName(_fromUtf8("Reports_Bookings_Btn_Tableau"))
        self.Reports_Bookings_HBox_Top.addWidget(self.Reports_Bookings_Btn_Tableau)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Reports_Bookings_HBox_Top.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.Reports_Bookings_HBox_Top)
        self.Reports_Bookings_Scroll = QtGui.QScrollArea(self.Bookings)
        self.Reports_Bookings_Scroll.setWidgetResizable(True)
        self.Reports_Bookings_Scroll.setObjectName(_fromUtf8("Reports_Bookings_Scroll"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 474, 308))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.Reports_Bookings_Text = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Reports_Bookings_Text.setObjectName(_fromUtf8("Reports_Bookings_Text"))
        self.horizontalLayout_4.addWidget(self.Reports_Bookings_Text)
        self.Reports_Bookings_Scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.Reports_Bookings_Scroll)
        self.Reports_Bookings_HBox_Bottom = QtGui.QHBoxLayout()
        self.Reports_Bookings_HBox_Bottom.setObjectName(_fromUtf8("Reports_Bookings_HBox_Bottom"))
        self.Reports_Bookings_Btn_Refresh = QtGui.QPushButton(self.Bookings)
        self.Reports_Bookings_Btn_Refresh.setObjectName(_fromUtf8("Reports_Bookings_Btn_Refresh"))
        self.Reports_Bookings_HBox_Bottom.addWidget(self.Reports_Bookings_Btn_Refresh)
        self.Reports_Bookings_ProgressBar = QtGui.QProgressBar(self.Bookings)
        self.Reports_Bookings_ProgressBar.setProperty("value", 24)
        self.Reports_Bookings_ProgressBar.setObjectName(_fromUtf8("Reports_Bookings_ProgressBar"))
        self.Reports_Bookings_HBox_Bottom.addWidget(self.Reports_Bookings_ProgressBar)
        self.verticalLayout_4.addLayout(self.Reports_Bookings_HBox_Bottom)
        self.Reports_TabWidget.addTab(self.Bookings, _fromUtf8(""))
        self.HeadCount = QtGui.QWidget()
        self.HeadCount.setObjectName(_fromUtf8("HeadCount"))
        self.Reports_TabWidget.addTab(self.HeadCount, _fromUtf8(""))
        self.Bugs = QtGui.QWidget()
        self.Bugs.setObjectName(_fromUtf8("Bugs"))
        self.Reports_TabWidget.addTab(self.Bugs, _fromUtf8(""))
        self.Budget = QtGui.QWidget()
        self.Budget.setObjectName(_fromUtf8("Budget"))
        self.Reports_TabWidget.addTab(self.Budget, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.Reports_TabWidget)
        self.Main_Tab.addTab(self.Reports, _fromUtf8(""))
        self.Mappings = QtGui.QWidget()
        self.Mappings.setObjectName(_fromUtf8("Mappings"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.Mappings)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.Mappings_TabWidget = QtGui.QTabWidget(self.Mappings)
        self.Mappings_TabWidget.setObjectName(_fromUtf8("Mappings_TabWidget"))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_8)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Mappings_Dept_HBox_Top = QtGui.QHBoxLayout()
        self.Mappings_Dept_HBox_Top.setObjectName(_fromUtf8("Mappings_Dept_HBox_Top"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Mappings_Dept_HBox_Top.addItem(spacerItem4)
        self.Mappings_Dept_Btn_New = QtGui.QPushButton(self.tab_8)
        self.Mappings_Dept_Btn_New.setObjectName(_fromUtf8("Mappings_Dept_Btn_New"))
        self.Mappings_Dept_HBox_Top.addWidget(self.Mappings_Dept_Btn_New)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Mappings_Dept_HBox_Top.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.Mappings_Dept_HBox_Top)
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_8)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 474, 308))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.scrollAreaWidgetContents_4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.Mappings_Dept_HBox_Bottom = QtGui.QHBoxLayout()
        self.Mappings_Dept_HBox_Bottom.setObjectName(_fromUtf8("Mappings_Dept_HBox_Bottom"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Mappings_Dept_HBox_Bottom.addItem(spacerItem6)
        self.Mappings_Dept_Btn_Save = QtGui.QPushButton(self.tab_8)
        self.Mappings_Dept_Btn_Save.setObjectName(_fromUtf8("Mappings_Dept_Btn_Save"))
        self.Mappings_Dept_HBox_Bottom.addWidget(self.Mappings_Dept_Btn_Save)
        self.verticalLayout_3.addLayout(self.Mappings_Dept_HBox_Bottom)
        self.Mappings_TabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_9)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.Mappings_Project_HBox_Top = QtGui.QHBoxLayout()
        self.Mappings_Project_HBox_Top.setObjectName(_fromUtf8("Mappings_Project_HBox_Top"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Mappings_Project_HBox_Top.addItem(spacerItem7)
        self.Mappings_Project_Btn_New = QtGui.QPushButton(self.tab_9)
        self.Mappings_Project_Btn_New.setObjectName(_fromUtf8("Mappings_Project_Btn_New"))
        self.Mappings_Project_HBox_Top.addWidget(self.Mappings_Project_Btn_New)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Mappings_Project_HBox_Top.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.Mappings_Project_HBox_Top)
        self.scrollArea = QtGui.QScrollArea(self.tab_9)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 474, 308))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.Mappings_Project_Table = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.Mappings_Project_Table.setObjectName(_fromUtf8("Mappings_Project_Table"))
        self.horizontalLayout_7.addWidget(self.Mappings_Project_Table)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.Mappings_Project_HBox_Bottom = QtGui.QHBoxLayout()
        self.Mappings_Project_HBox_Bottom.setObjectName(_fromUtf8("Mappings_Project_HBox_Bottom"))
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Mappings_Project_HBox_Bottom.addItem(spacerItem9)
        self.Mappings_Project_Btn_Save = QtGui.QPushButton(self.tab_9)
        self.Mappings_Project_Btn_Save.setObjectName(_fromUtf8("Mappings_Project_Btn_Save"))
        self.Mappings_Project_HBox_Bottom.addWidget(self.Mappings_Project_Btn_Save)
        self.verticalLayout_5.addLayout(self.Mappings_Project_HBox_Bottom)
        self.Mappings_TabWidget.addTab(self.tab_9, _fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.Mappings_TabWidget)
        self.Main_Tab.addTab(self.Mappings, _fromUtf8(""))
        self.verticalLayout.addWidget(self.Main_Tab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout_Report_Center = QtGui.QAction(MainWindow)
        self.actionAbout_Report_Center.setObjectName(_fromUtf8("actionAbout_Report_Center"))
        self.actionInput = QtGui.QAction(MainWindow)
        self.actionInput.setObjectName(_fromUtf8("actionInput"))
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionInput)
        self.menuAbout.addAction(self.actionAbout_Report_Center)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.Main_Tab.setCurrentIndex(0)
        self.Reports_TabWidget.setCurrentIndex(4)
        self.Mappings_TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
    	''' More QT compiled code'''
        MainWindow.setWindowTitle(_translate("MainWindow", "IoTSSG Report Center", None))
        self.Reports_Clarity_Btn_Excel.setText(_translate("MainWindow", "Excel Report", None))
        self.Reports_Clarity_Btn_Tableau.setText(_translate("MainWindow", "Tableau", None))
        self.Reports_Clarity_Btn_Refresh.setText(_translate("MainWindow", "Refresh Data", None))
        self.Reports_TabWidget.setTabText(self.Reports_TabWidget.indexOf(self.Clarity), _translate("MainWindow", "Clarity", None))
        self.Reports_Bookings_Btn_Excel.setText(_translate("MainWindow", "Excel Report", None))
        self.Reports_Bookings_Btn_Tableau.setText(_translate("MainWindow", "Tableau", None))
        self.Reports_Bookings_Btn_Refresh.setText(_translate("MainWindow", "Refresh Data", None))
        self.Reports_TabWidget.setTabText(self.Reports_TabWidget.indexOf(self.Bookings), _translate("MainWindow", "Bookings", None))
        self.Reports_TabWidget.setTabText(self.Reports_TabWidget.indexOf(self.HeadCount), _translate("MainWindow", "HeadCount", None))
        self.Reports_TabWidget.setTabText(self.Reports_TabWidget.indexOf(self.Bugs), _translate("MainWindow", "Bugs", None))
        self.Reports_TabWidget.setTabText(self.Reports_TabWidget.indexOf(self.Budget), _translate("MainWindow", "Budget", None))
        self.Main_Tab.setTabText(self.Main_Tab.indexOf(self.Reports), _translate("MainWindow", "Reports", None))
        self.Mappings_Dept_Btn_New.setText(_translate("MainWindow", "New Item", None))
        self.Mappings_Dept_Btn_Save.setText(_translate("MainWindow", "Save", None))
        self.Mappings_TabWidget.setTabText(self.Mappings_TabWidget.indexOf(self.tab_8), _translate("MainWindow", "Department", None))
        self.Mappings_Project_Btn_New.setText(_translate("MainWindow", "New Item", None))
        self.Mappings_Project_Btn_Save.setText(_translate("MainWindow", "Save", None))
        self.Mappings_TabWidget.setTabText(self.Mappings_TabWidget.indexOf(self.tab_9), _translate("MainWindow", "Project", None))
        self.Main_Tab.setTabText(self.Main_Tab.indexOf(self.Mappings), _translate("MainWindow", "Mappings", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout_Report_Center.setText(_translate("MainWindow", "About Report-Center", None))
        self.actionInput.setText(_translate("MainWindow", "Input", None))

    def bindEvents(self):
    	'''
    	After table data loads, Binds buttons and other inputs to functions
    	'''
    	self.Reports_Clarity_Btn_Refresh.clicked.connect(self.refreshClarity)
    	self.Reports_Clarity_Btn_Excel.clicked.connect(self.excelClarityDownload)
    	self.Reports_Clarity_Btn_Tableau.clicked.connect(self.redirectClarityTableau)

    def setConnection(self):
        '''
        Establishes connection to the Database
        '''
        try:
            self.conn = pymysql.connect(
                host=self.serverParams['host'], 
                port=self.serverParams['port'], 
                user=self.serverParams['user'], 
                passwd=self.serverParams['passwd'], 
                db=self.serverParams['db'])
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT VERSION()")
            print "Successfully logged into MySQL server, running version: " + self.cur.fetchone()[0]
        except Exception as e:
            print "trouble connecting to server: " + str(e)
            ## Close cursor and connection
            try:
                self.cur.close()
            except:
                self.cur = None
            try:
                self.conn.close()
            except:
                self.conn = None

    def getUserSettings(self):#TODO: Create window to handle getting settings from user and saving
        try:
            return pickle.load(open('save.p','rb'))
        except:
            print "Settings not found. Please enter CEC Username/password"
            ## new window that asks for username and password ##
            self.settings = "I make a window that gets fields and packages them into self.settings"
            pickle.dump(self.settings,open('save.p','wb'))

    def retrieveTableData(self):
        #what does a return look like? need to get column names items
        '''
        Called right after GUI is made to get items inside the Tables
        Access's MySQL server and gets row for Mappings tab content
        '''
        if not self.conn:
            print "Connection not established."
            return
        return

    	
    def refreshHC(self):
        '''
        Refreshes Employee data. Grabs from CEC Directory
        '''
        if not self.conn:
            print "Connection not established"
            return

    	response = urllib2.urlopen(self.orgChartURL)
        cr = csv.reader(response)
        next(cr)
        count = 0
        ## Wipe the table
        self.cur.execute("DELETE FROM Employees;")
        print "Employee table deleted"

        for row in cr:
            dept = ""

            ## add to username list to pull clarity data
            self.usernames.append(row[0])
            ## upload Employee info to Emp table ##

            ## Step 1: Department Name
            # Identify if the userid is a director
            if row[0] == "kip":
                dept = "IoT Central"
            elif row[0] == "rhouse":
                dept = "Network Engineering - Hardware"
            elif row[0] == "separham":
                dept = "CSS"
            elif row[0] == "jaschen":
                dept = "Network Engineering - Software"
            elif row[0] == "eganesan":
                dept = "Architecture"
            elif row[0] == "vbutaney":
                dept = "Product Management"
            elif row[0] == "sribhaga":
                dept = "IoT Central"
            ## this is kips admin
            elif row[0] == "dihughes":
                dept = "IoT Central"
            else:
                #If not a director, find the director node
                ## Sample string: 'chambers:rlloyd:psp:rosoderb:kip:rhouse:jaschen:adalela'
                ##                  0           1   2    3       4    5      6
                mgrchain = row[8].split(':')
                if len(mgrchain) <= 5:
                    #there's someone under kip that isn't caught above
                    dept = "uncaught kip report"
                else:
                    if len(mgrchain) > 6:
                        if mgrchain[6] == 'jaschen':
                            dept = 'Network Engineering - Software'
                        elif mgrchain[6] == 'skhullar':
                            dept = 'Network Engineering - Software'
                        elif mgrchain[5] == "rhouse":
                            dept = "Network Engineering - Hardware"
                        elif mgrchain[5] == "separham":
                            dept = "CSS"
                        elif mgrchain[5] == "eganesan":
                            dept = "Architecture"
                        elif mgrchain[5] == "vbutaney":
                            dept = "Product Management"
                        elif mgrchain[5] == "sribhaga":
                            dept = "IoT Central"
                        else:
                            dept = "Unknown"
                    else:
                        if mgrchain[5] == "rhouse":
                            dept = "Network Engineering - Hardware"
                        elif mgrchain[5] == "separham":
                            dept = "CSS"
                        # elif mgrchain[5] == "jaschen":
                        #     dept = "Network Engineering - Software"
                        elif mgrchain[5] == "eganesan":
                            dept = "Architecture"
                        elif mgrchain[5] == "vbutaney":
                            dept = "Product Management"
                        elif mgrchain[5] == "sribhaga":
                            dept = "IoT Central"
                        else:
                            dept = "Unknown"

            #Step 2: define other employee definitions
            userID = row[0]
            firstName = row[2]
            lastName = row[1]
            if row[4] == "consvend":
                empType = "Contractor"
            elif row[4] == "mgr" or row[4] == "regular":
                empType = "Employee"
            else:
                empType = row[4]
            managerID = row[7]
            # package data for SQL insert
            data = (userID,firstName,lastName,empType,managerID,dept)

            #Sanity Check
            # print row[0] + " is under " + mgrchain[5] + " and is assigned to " + dept
            # print "the length of mgrchain was " + str(len(mgrchain))

            #execute and commit. update console. This table MUST be present with the field names below
            self.cur.execute("INSERT INTO Employees (User_ID,First_Name,Last_Name,Employee_Type,Manager_ID,Department)VALUES (%s, %s, %s, %s, %s, %s)",data)
            self.conn.commit()
            count += 1
            sys.stdout.write(str(count) + " Employees added to Database\r")
            sys.stdout.flush()

    def refreshClarity(self):
    	'''
    	Updates Employee Table with CEC org chart data
    	Retrieves Clarity information and Loads into MySQL server
    	'''
        print "Refreshing Clarity Data"
    	return

    def excelClarityDownload(self):
    	'''attempts to access Strategic Planning IWE site
    	 to download an Excel Report.
    	 TODO: get Auth information to preauth user?
    	'''
    	return

    def redirectClarityTableau(self):
    	'''
    	Open Browser and direct to Tableau
    	TODO: Add cec authentication to streamline opening report?
    	'''
    	return

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    client = Ui_MainWindow()
    client.show()
    sys.exit(app.exec_())