# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\bd_final_project\DairyPro\DB_ConnectionsFiles\DB_project\17 Distributors Button.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 622)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searched = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.searched.setGeometry(QtCore.QRect(30, 20, 691, 251))
        self.searched.setObjectName("searched")
        self.type = QtWidgets.QGroupBox(parent=self.searched)
        self.type.setGeometry(QtCore.QRect(480, 20, 171, 171))
        self.type.setObjectName("type")
        self.layoutWidget = QtWidgets.QWidget(parent=self.type)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 121, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rdb1 = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.rdb1.setObjectName("rdb1")
        self.verticalLayout_3.addWidget(self.rdb1)
        self.rdb2 = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.rdb2.setObjectName("rdb2")
        self.verticalLayout_3.addWidget(self.rdb2)
        self.rdb3 = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.rdb3.setObjectName("rdb3")
        self.verticalLayout_3.addWidget(self.rdb3)
        self.rdb3_2 = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.rdb3_2.setObjectName("rdb3_2")
        self.verticalLayout_3.addWidget(self.rdb3_2)
        self.searchButton = QtWidgets.QPushButton(parent=self.searched)
        self.searchButton.setGeometry(QtCore.QRect(510, 200, 121, 31))
        self.searchButton.setObjectName("searchButton")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.searched)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 30, 281, 82))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.categoryCombo = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.categoryCombo.setObjectName("categoryCombo")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.verticalLayout.addWidget(self.categoryCombo)
        self.titleline = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.titleline.setObjectName("titleline")
        self.verticalLayout.addWidget(self.titleline)
        self.titleline_2 = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.titleline_2.setObjectName("titleline_2")
        self.verticalLayout.addWidget(self.titleline_2)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.searched)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 30, 129, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.booksTableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.booksTableWidget.setGeometry(QtCore.QRect(30, 290, 691, 191))
        self.booksTableWidget.setObjectName("booksTableWidget")
        self.booksTableWidget.setColumnCount(9)
        self.booksTableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setItem(0, 8, item)
        self.viewButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.viewButton_4.setGeometry(QtCore.QRect(470, 510, 121, 31))
        self.viewButton_4.setObjectName("viewButton_4")
        self.closeButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton_2.setGeometry(QtCore.QRect(600, 550, 121, 31))
        self.closeButton_2.setObjectName("closeButton_2")
        self.deleteButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton_2.setGeometry(QtCore.QRect(600, 510, 121, 31))
        self.deleteButton_2.setObjectName("deleteButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 26))
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
        self.searched.setTitle(_translate("MainWindow", "Search"))
        self.type.setTitle(_translate("MainWindow", "City"))
        self.rdb1.setText(_translate("MainWindow", "Karachi"))
        self.rdb2.setText(_translate("MainWindow", "Peshawer"))
        self.rdb3.setText(_translate("MainWindow", "Islamabad"))
        self.rdb3_2.setText(_translate("MainWindow", "Lahore"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.categoryCombo.setItemText(0, _translate("MainWindow", "Ali"))
        self.categoryCombo.setItemText(1, _translate("MainWindow", "Hamza"))
        self.categoryCombo.setItemText(2, _translate("MainWindow", "Yasir"))
        self.categoryCombo.setItemText(3, _translate("MainWindow", "Majeed"))
        self.titleline.setText(_translate("MainWindow", "011222"))
        self.titleline_2.setText(_translate("MainWindow", "Rehman Dairy"))
        self.label.setText(_translate("MainWindow", "Representative Name:"))
        self.label_2.setText(_translate("MainWindow", "Distributor ID:"))
        self.label_3.setText(_translate("MainWindow", "Company Name:"))
        item = self.booksTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.booksTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Distributor ID"))
        item = self.booksTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Company Name"))
        item = self.booksTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Representative Name"))
        item = self.booksTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address"))
        item = self.booksTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "City"))
        item = self.booksTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phone Number"))
        item = self.booksTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.booksTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Performance Metric"))
        item = self.booksTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Activity Status"))
        __sortingEnabled = self.booksTableWidget.isSortingEnabled()
        self.booksTableWidget.setSortingEnabled(False)
        item = self.booksTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "011222"))
        item = self.booksTableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Rehman Dairy"))
        item = self.booksTableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Ali"))
        item = self.booksTableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "222A, Gulistan-e-Johar"))
        item = self.booksTableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Karachi"))
        item = self.booksTableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "333-123455"))
        item = self.booksTableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "xyz@abc.com"))
        item = self.booksTableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "A+"))
        item = self.booksTableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "Active"))
        self.booksTableWidget.setSortingEnabled(__sortingEnabled)
        self.viewButton_4.setText(_translate("MainWindow", "View"))
        self.closeButton_2.setText(_translate("MainWindow", "Close"))
        self.deleteButton_2.setText(_translate("MainWindow", "Remove"))
