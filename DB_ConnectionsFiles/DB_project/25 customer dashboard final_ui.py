# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\bd_final_project\DairyPro\DB_ConnectionsFiles\DB_project\25 customer dashboard final.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 317)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prodView = QtWidgets.QPushButton(parent=self.centralwidget)
        self.prodView.setGeometry(QtCore.QRect(200, 120, 111, 91))
        self.prodView.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.prodView.setObjectName("prodView")
        self.d_orderView = QtWidgets.QPushButton(parent=self.centralwidget)
        self.d_orderView.setGeometry(QtCore.QRect(50, 120, 111, 91))
        self.d_orderView.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.d_orderView.setObjectName("d_orderView")
        self.distributorView = QtWidgets.QPushButton(parent=self.centralwidget)
        self.distributorView.setGeometry(QtCore.QRect(350, 120, 111, 91))
        self.distributorView.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.distributorView.setObjectName("distributorView")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(150, 40, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-20, -10, 831, 681))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("\n"
"\n"
"background-color: rgb(207, 232, 255);\n"
"")
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 170, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c:\\Users\\hp\\Documents\\CS_Undergrad\\Semester_3\\DATABASE\\bd_final_project\\DairyPro\\DB_ConnectionsFiles\\DB_project\\order.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 170, 31, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\hp\\Documents\\CS_Undergrad\\Semester_3\\DATABASE\\bd_final_project\\DairyPro\\DB_ConnectionsFiles\\DB_project\\prod.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 170, 41, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("c:\\Users\\hp\\Documents\\CS_Undergrad\\Semester_3\\DATABASE\\bd_final_project\\DairyPro\\DB_ConnectionsFiles\\DB_project\\cust.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_4.raise_()
        self.prodView.raise_()
        self.d_orderView.raise_()
        self.distributorView.raise_()
        self.label_12.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.prodView.setText(_translate("MainWindow", "Products"))
        self.d_orderView.setText(_translate("MainWindow", "Orders"))
        self.distributorView.setText(_translate("MainWindow", "Customer Info"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Customer Dashboard</span></p></body></html>"))