# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\bd_final_project\DairyPro\Code-Connection\Screens\5 Admin Order Approve.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pendingOrderTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.pendingOrderTable.setGeometry(QtCore.QRect(160, 80, 541, 192))
        self.pendingOrderTable.setStyleSheet("column-width: 130px")
        self.pendingOrderTable.setObjectName("pendingOrderTable")
        self.pendingOrderTable.setColumnCount(4)
        self.pendingOrderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pendingOrderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pendingOrderTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pendingOrderTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pendingOrderTable.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.approveOrder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.approveOrder.setGeometry(QtCore.QRect(300, 340, 101, 31))
        self.approveOrder.setObjectName("approveOrder")
        self.closeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(420, 340, 101, 31))
        self.closeButton.setObjectName("closeButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 300, 121, 16))
        self.label_2.setObjectName("label_2")
        self.employeeToBeAssigned = QtWidgets.QComboBox(parent=self.centralwidget)
        self.employeeToBeAssigned.setGeometry(QtCore.QRect(350, 300, 171, 22))
        self.employeeToBeAssigned.setObjectName("employeeToBeAssigned")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        item = self.pendingOrderTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.pendingOrderTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Customer ID"))
        item = self.pendingOrderTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Order Date"))
        item = self.pendingOrderTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Required Date"))
        self.label.setText(_translate("MainWindow", "Orders"))
        self.approveOrder.setText(_translate("MainWindow", "Approve Order"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", "To be Assigned to:"))
