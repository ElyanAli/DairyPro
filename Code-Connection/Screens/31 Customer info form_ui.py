# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\DB project\DairyPro-main\Code-Connection\Screens\31 Customer info form.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 441)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 50, 251, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.id = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.id.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.id.setObjectName("id")
        self.verticalLayout.addWidget(self.id)
        self.name = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.name.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.address = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.address.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.address.setObjectName("address")
        self.verticalLayout.addWidget(self.address)
        self.contact = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.contact.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.contact.setObjectName("contact")
        self.verticalLayout.addWidget(self.contact)
        self.email = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.email.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(100, 50, 103, 261))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_2.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_3.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_5.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_6.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.closeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(340, 340, 121, 31))
        self.closeButton.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.closeButton.setObjectName("closeButton")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-30, -40, 851, 741))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("\n"
"\n"
"background-color: rgb(207, 232, 255);\n"
"")
        self.label_7.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.closeButton.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 18))
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
        self.id.setText(_translate("MainWindow", "011245"))
        self.name.setText(_translate("MainWindow", "Ali"))
        self.address.setText(_translate("MainWindow", "Karachi"))
        self.contact.setText(_translate("MainWindow", "03784567302"))
        self.email.setText(_translate("MainWindow", "ali@gmail.com"))
        self.label.setText(_translate("MainWindow", "Customer ID:"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.label_5.setText(_translate("MainWindow", "Phone Number:"))
        self.label_6.setText(_translate("MainWindow", "Email:"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Customer Information</span></p></body></html>"))
