## Clarity XML ETL ##
## This assumes there are tables already in place for Employee and Allocations ##
## Will Delete all entries in Employee table, create new list based on current CEC org chart ##
## uses org chart usernames to look up clarity info via XML web services ##
## Deletes all from Allocations table and inserts new data ##
import sys
import xml.etree.ElementTree as ET
import urllib2
import csv
import pymysql
from datetime import datetime
import pprint

class ClarityAllocations:
    def __init__(self):
        self.pp = pprint.PrettyPrinter(indent=4)
        self.running_count = 0
        ## SQL server ##
        self.serverParams = {'host':'sjc-dbdl-mysql3',
                        'port':3306,
                        'user':'iotssg',
                        'passwd':'iotssg',
                        'db':'iotssg'}
        self.conn = None
        self.cur = None

        ## Org Chart ##
        self.usernames = []
        self.Org_Chart_url = 'https://labtools.cisco.com/general/orgchart.php?tops=kip&format=csv'

        ## Clarity XML ##
        self.Clarity_url = 'http://ppm-prod-int:8888/ppmws/api/resources/resourceById/'
        self.user = 'morahman'
        self.password = 'Nasreen12-'
        try:
            print "running refresh routine..."
            print "Establishing Connection to DB..."
            self.setConnection()
            print "Success!"
        except Exception as e:
            print "error! " + str(e)

    def setConnection(self):
        """
        establishes connection to MySQL server
        """
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

    def cleanTables(self):
        self.cur.execute("DELETE FROM Allocations;")
        self.cur.execute("DELETE FROM Employees;")
        print "Tables cleaned."

    def closeConnection(self):
        self.cur.close()
        self.conn.close()

    def getOrgChart(self):
        """
        Accesses CEC org chart and inserts usernames into SQL
        """
        response = urllib2.urlopen(self.Org_Chart_url)
        cr = csv.reader(response)
        next(cr)
        count = 0
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

    def getClarityInfo(self):
        """
        Uses the usernames from CEC orgchart and retrieves allocation data
        """
        count = 0
        for username in self.usernames:
            count += 1
            ## data var will contain SQL rows to insert into table ##
            data = []
            ## for each username, build connection to clarity web services url ##
            url = self.Clarity_url + username
            p = urllib2.HTTPPasswordMgrWithDefaultRealm()
            p.add_password(None, url, self.user, self.password)
            handler = urllib2.HTTPBasicAuthHandler(p)
            opener = urllib2.build_opener(handler)
            urllib2.install_opener(opener)

            ## create xml data and establish parent tree ##
            xmldata = urllib2.urlopen(url)
            tree = ET.parse(xmldata)
            xmldata.close()
        
            root = tree.getroot()
            FTE_count = 0.0
            try:
                for month in root[0].find('monthlySums'):
                    if float(month.get('fte')) == 0:
                        data.append((username,
                                    datetime.strptime(month.get('start').split('T')[0],"%Y-%m-%d"),
                                    "Unallocated",
                                    "Unallocated",
                                    0))
                        self.running_count += 1
                for project in root[0].find('allocations'):
                    for month in project.find('monthlySegments'):
                        if float(month.get('fte')) > 0:
                            ## append a tuple as a row to use as insert statement ##
                            data.append(
                                (username,
                                ## Month - DATETIME ##
                                datetime.strptime(month.get('start').split('T')[0],"%Y-%m-%d"),
                                ## Project Name - STRING##
                                project.get('investmentName')[0:-9],
                                ## Project ID - STRING##
                                project.get('investmentId'),
                                ## FTE amount - FLOAT##
                                float(month.get('fte')))
                            )
                            self.running_count += 1

            except Exception as e:
                print "No projects found for " + username
                data.append(
                    (username, datetime.strftime(datetime.today(),"%Y-%m-01"),"Unallocated", "No Projects", 0))
                self.running_count += 1
            ## add rows to SQL Server ##
            try:
                self.cur.executemany("INSERT INTO Allocations VALUES (%s, %s, %s, %s, %s)",data)
                self.conn.commit()
                sys.stdout.write(str(count) + "/" +str(len(self.usernames)) + "\r" )
                sys.stdout.flush()
            except Exception as e:
                print str(e)
if __name__ == "__main__":
    try:
        clarityProgram = ClarityAllocations()
        print "Cleaning tables"
        clarityProgram.cleanTables()
        print "Starting Data Extraction process"
        clarityProgram.getOrgChart()
        clarityProgram.getClarityInfo()
        print "Closing Connection"
        clarityProgram.closeConnection()
        print "Done"
    except KeyboardInterrupt:
        clarityProgram.closeConnection()