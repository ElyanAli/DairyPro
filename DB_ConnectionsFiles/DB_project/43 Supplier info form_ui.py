# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\bd_final_project\DairyPro\DB_ConnectionsFiles\DB_project\43 Supplier info form.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 431)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 50, 251, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.supp_id = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_id.setObjectName("supp_id")
        self.verticalLayout.addWidget(self.supp_id)
        self.supp_name = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_name.setObjectName("supp_name")
        self.verticalLayout.addWidget(self.supp_name)
        self.city = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.city.setObjectName("city")
        self.verticalLayout.addWidget(self.city)
        self.supp_addr = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_addr.setObjectName("supp_addr")
        self.verticalLayout.addWidget(self.supp_addr)
        self.supp_phone = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_phone.setObjectName("supp_phone")
        self.verticalLayout.addWidget(self.supp_phone)
        self.supp_email = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.supp_email.setObjectName("supp_email")
        self.verticalLayout.addWidget(self.supp_email)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 50, 103, 251))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.closeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(340, 330, 91, 31))
        self.closeButton.setObjectName("closeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 18))
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
        self.supp_id.setText(_translate("MainWindow", "011244"))
        self.supp_name.setText(_translate("MainWindow", "Ahsan"))
        self.city.setText(_translate("MainWindow", "City A"))
        self.supp_addr.setText(_translate("MainWindow", "Karachi"))
        self.supp_phone.setText(_translate("MainWindow", "0378-4567302"))
        self.supp_email.setText(_translate("MainWindow", "ahsan@gmail.com"))
        self.label.setText(_translate("MainWindow", "Supplier ID:"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "City"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.label_5.setText(_translate("MainWindow", "Phone Number:"))
        self.label_6.setText(_translate("MainWindow", "Email:"))
        self.closeButton.setText(_translate("MainWindow", "Close"))