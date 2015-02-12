# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportCenter.ui'
#
# Created: Mon Feb 09 00:26:53 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(537, 316)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolBox = QtGui.QToolBox(Form)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.Refresh = QtGui.QWidget()
        self.Refresh.setGeometry(QtCore.QRect(0, 0, 502, 351))
        self.Refresh.setObjectName(_fromUtf8("Refresh"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.Refresh)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.Refresh)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Clarity = QtGui.QWidget()
        self.Clarity.setObjectName(_fromUtf8("Clarity"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Clarity)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Clarity_HBox = QtGui.QHBoxLayout()
        self.Clarity_HBox.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.Clarity_HBox.setObjectName(_fromUtf8("Clarity_HBox"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.Clarity_HBox.addItem(spacerItem)
        self.Clarity_refresh_btn = QtGui.QPushButton(self.Clarity)
        self.Clarity_refresh_btn.setObjectName(_fromUtf8("Clarity_refresh_btn"))
        self.Clarity_HBox.addWidget(self.Clarity_refresh_btn)
        self.Clarity_download_btn = QtGui.QCommandLinkButton(self.Clarity)
        self.Clarity_download_btn.setObjectName(_fromUtf8("Clarity_download_btn"))
        self.Clarity_HBox.addWidget(self.Clarity_download_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.Clarity_HBox.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.Clarity_HBox)
        self.Clarity_scrollarea = QtGui.QScrollArea(self.Clarity)
        #self.Clarity_scrollarea.setSizeAdjustPolicy(QtGui.QAbstractScrollArea.AdjustToContents)
        self.Clarity_scrollarea.setWidgetResizable(True)
        self.Clarity_scrollarea.setObjectName(_fromUtf8("Clarity_scrollarea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 458, 210))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.Clarity_status = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.Clarity_status.setEnabled(False)
        self.Clarity_status.setObjectName(_fromUtf8("Clarity_status"))
        self.horizontalLayout_6.addWidget(self.Clarity_status)
        self.Clarity_scrollarea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.Clarity_scrollarea, QtCore.Qt.AlignVCenter)
        self.Clarity_progressbar = QtGui.QProgressBar(self.Clarity)
        self.Clarity_progressbar.setProperty("value", 0)
        self.Clarity_progressbar.setObjectName(_fromUtf8("Clarity_progressbar"))
        self.verticalLayout.addWidget(self.Clarity_progressbar)
        self.tabWidget.addTab(self.Clarity, _fromUtf8(""))
        self.Bookings = QtGui.QWidget()
        self.Bookings.setObjectName(_fromUtf8("Bookings"))
        self.tabWidget.addTab(self.Bookings, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.toolBox.addItem(self.Refresh, _fromUtf8(""))
        self.DataManagement = QtGui.QWidget()
        self.DataManagement.setGeometry(QtCore.QRect(0, 0, 519, 244))
        self.DataManagement.setObjectName(_fromUtf8("DataManagement"))
        self.toolBox.addItem(self.DataManagement, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.toolBox)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.tabWidget.setAccessibleName(_translate("Form", "Clarity", None))
        self.Clarity_refresh_btn.setText(_translate("Form", "Refresh Data", None))
        self.Clarity_download_btn.setText(_translate("Form", "Download Excel Report", None))
        self.Clarity_status.setAccessibleName(_translate("Form", "ClarityStatus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Clarity), _translate("Form", "Clarity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bookings), _translate("Form", "Bookings", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Refresh), _translate("Form", "Refresh", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.DataManagement), _translate("Form", "Data Management", None))

        self.Clarity_refresh_btn.clicked.connect(self.RefreshClarity)

    def RefreshClarity(self):
        self.Clarity_status.insertPlainText("Refreshing data...\n")

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Form()
	ex.show()
	sys.exit(app.exec_())