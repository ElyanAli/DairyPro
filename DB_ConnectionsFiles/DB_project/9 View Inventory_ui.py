# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\bd_final_project\DairyPro\DB_ConnectionsFiles\DB_project\9 View Inventory.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 374)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 30, 281, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLineedit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.titleLineedit.setObjectName("titleLineedit")
        self.verticalLayout.addWidget(self.titleLineedit)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.categoryLine = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.categoryLine.setObjectName("categoryLine")
        self.verticalLayout.addWidget(self.categoryLine)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 30, 109, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.viewButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.viewButton_5.setGeometry(QtCore.QRect(340, 190, 121, 31))
        self.viewButton_5.setObjectName("viewButton_5")
        self.type = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.type.setGeometry(QtCore.QRect(50, 180, 141, 141))
        self.type.setObjectName("type")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.type)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 121, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rdb1 = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        self.rdb1.setObjectName("rdb1")
        self.verticalLayout_3.addWidget(self.rdb1)
        self.rdb2 = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        self.rdb2.setObjectName("rdb2")
        self.verticalLayout_3.addWidget(self.rdb2)
        self.rdb3 = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        self.rdb3.setObjectName("rdb3")
        self.verticalLayout_3.addWidget(self.rdb3)
        self.rdb3_2 = QtWidgets.QRadioButton(parent=self.layoutWidget_2)
        self.rdb3_2.setObjectName("rdb3_2")
        self.verticalLayout_3.addWidget(self.rdb3_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 26))
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
        self.titleLineedit.setText(_translate("MainWindow", "56"))
        self.lineEdit.setText(_translate("MainWindow", "1001"))
        self.categoryLine.setText(_translate("MainWindow", "20001"))
        self.lineEdit_3.setText(_translate("MainWindow", "2000"))
        self.lineEdit_2.setText(_translate("MainWindow", "Cool"))
        self.label.setText(_translate("MainWindow", "Warehouse ID:"))
        self.label_2.setText(_translate("MainWindow", "Product ID:"))
        self.label_3.setText(_translate("MainWindow", "Managed  By:"))
        self.label_5.setText(_translate("MainWindow", "Stock_level"))
        self.label_4.setText(_translate("MainWindow", "Storage Condition:"))
        self.viewButton_5.setText(_translate("MainWindow", "Cancel"))
        self.type.setTitle(_translate("MainWindow", "WareHouse City"))
        self.rdb1.setText(_translate("MainWindow", "Karachi"))
        self.rdb2.setText(_translate("MainWindow", "Peshawer"))
        self.rdb3.setText(_translate("MainWindow", "Islamabad"))
        self.rdb3_2.setText(_translate("MainWindow", "Lahore"))
