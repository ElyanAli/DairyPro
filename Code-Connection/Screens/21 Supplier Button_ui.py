# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\DB project\DairyPro-main\Code-Connection\Screens\21 Supplier Button.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 569)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searched = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.searched.setGeometry(QtCore.QRect(30, 20, 461, 171))
        self.searched.setObjectName("searched")
        self.searchButton = QtWidgets.QPushButton(parent=self.searched)
        self.searchButton.setGeometry(QtCore.QRect(310, 130, 121, 31))
        self.searchButton.setObjectName("searchButton")
        self.layoutWidget = QtWidgets.QWidget(parent=self.searched)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 30, 281, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.categoryCombo = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.categoryCombo.setObjectName("categoryCombo")
        self.categoryCombo.addItem("")
        self.verticalLayout.addWidget(self.categoryCombo)
        self.titleline = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.titleline.setObjectName("titleline")
        self.verticalLayout.addWidget(self.titleline)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.searched)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 30, 103, 81))
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
        self.booksTableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.booksTableWidget.setGeometry(QtCore.QRect(30, 220, 461, 191))
        self.booksTableWidget.setObjectName("booksTableWidget")
        self.booksTableWidget.setColumnCount(6)
        self.booksTableWidget.setRowCount(0)
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
        self.supp_view = QtWidgets.QPushButton(parent=self.centralwidget)
        self.supp_view.setGeometry(QtCore.QRect(240, 440, 121, 31))
        self.supp_view.setObjectName("supp_view")
        self.closeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(370, 480, 121, 31))
        self.closeButton.setObjectName("closeButton")
        self.deleteButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton_2.setGeometry(QtCore.QRect(370, 440, 121, 31))
        self.deleteButton_2.setObjectName("deleteButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 18))
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
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.categoryCombo.setItemText(0, _translate("MainWindow", "Mr Suppliers"))
        self.titleline.setText(_translate("MainWindow", "11"))
        self.label.setText(_translate("MainWindow", "Supplier Name:"))
        self.label_2.setText(_translate("MainWindow", "Supplier ID:"))
        item = self.booksTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.booksTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.booksTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.booksTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone number"))
        item = self.booksTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.booksTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Activity status"))
        self.supp_view.setText(_translate("MainWindow", "View"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.deleteButton_2.setText(_translate("MainWindow", "Remove"))
