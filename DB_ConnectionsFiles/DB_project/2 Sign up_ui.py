# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\bd_final_project\DairyPro\DB_ConnectionsFiles\DB_project\2 Sign up.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 699)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(90, 500, 201, 21))
        self.password.setObjectName("password")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 480, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 120, 55, 16))
        self.label_6.setObjectName("label_6")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(90, 140, 201, 21))
        self.name.setInputMask("")
        self.name.setObjectName("name")
        self.reEnterPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.reEnterPassword.setGeometry(QtCore.QRect(90, 560, 201, 21))
        self.reEnterPassword.setObjectName("reEnterPassword")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 540, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 180, 131, 16))
        self.label_8.setObjectName("label_8")
        self.phoneNum = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.phoneNum.setGeometry(QtCore.QRect(90, 200, 201, 21))
        self.phoneNum.setInputMask("")
        self.phoneNum.setCursorPosition(11)
        self.phoneNum.setObjectName("phoneNum")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 240, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 420, 131, 16))
        self.label_10.setObjectName("label_10")
        self.email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.email.setGeometry(QtCore.QRect(90, 440, 201, 21))
        self.email.setObjectName("email")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 360, 131, 16))
        self.label_11.setObjectName("label_11")
        self.userType = QtWidgets.QComboBox(parent=self.centralwidget)
        self.userType.setGeometry(QtCore.QRect(90, 380, 201, 22))
        self.userType.setObjectName("userType")
        self.userType.addItem("")
        self.userType.addItem("")
        self.userType.addItem("")
        self.cancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(200, 610, 121, 31))
        self.cancel.setObjectName("cancel")
        self.createAccount_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createAccount_button.setGeometry(QtCore.QRect(60, 610, 121, 31))
        self.createAccount_button.setObjectName("createAccount_button")
        self.address = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.address.setGeometry(QtCore.QRect(90, 260, 201, 87))
        self.address.setObjectName("address")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 26))
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
        self.label_4.setText(_translate("MainWindow", "Sign Up"))
        self.password.setText(_translate("MainWindow", "************"))
        self.label_5.setText(_translate("MainWindow", "Password:"))
        self.label_6.setText(_translate("MainWindow", "Name:"))
        self.name.setText(_translate("MainWindow", "Sami Ali"))
        self.reEnterPassword.setText(_translate("MainWindow", "************"))
        self.label_7.setText(_translate("MainWindow", "Re-Enter Password:"))
        self.label_8.setText(_translate("MainWindow", "Phone Number:"))
        self.phoneNum.setText(_translate("MainWindow", "313-1234455"))
        self.label_9.setText(_translate("MainWindow", "Address:"))
        self.label_10.setText(_translate("MainWindow", "Email:"))
        self.email.setText(_translate("MainWindow", "0313-1234455"))
        self.label_11.setText(_translate("MainWindow", "User Type:"))
        self.userType.setItemText(0, _translate("MainWindow", "Customer"))
        self.userType.setItemText(1, _translate("MainWindow", "Distributor"))
        self.userType.setItemText(2, _translate("MainWindow", "Supplier"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.createAccount_button.setText(_translate("MainWindow", "Create Account"))
        self.address.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">222-A, XYZ Street, Gulshan-e-Iqbal</p></body></html>"))
