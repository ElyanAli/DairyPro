# Form implementation generated from reading ui file 'c:\Users\hp\Documents\CS_Undergrad\Semester_3\DATABASE\DB project\DairyPro-main\Code-Connection\Screens\30 Customer View Products.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 399)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.issueCheck2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.issueCheck2.setGeometry(QtCore.QRect(70, 190, 71, 21))
        self.issueCheck2.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.issueCheck2.setObjectName("issueCheck2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 60, 281, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLineedit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.titleLineedit.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.titleLineedit.setObjectName("titleLineedit")
        self.verticalLayout.addWidget(self.titleLineedit)
        self.comboBox = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBox.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.categoryLine = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.categoryLine.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.categoryLine.setObjectName("categoryLine")
        self.verticalLayout.addWidget(self.categoryLine)
        self.listWidget = QtWidgets.QListWidget(parent=self.layoutWidget)
        self.listWidget.setStyleSheet("background-color: rgb(169, 192, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(69, 60, 66, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_2.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_3.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_4.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color:rgb(0, 0, 127)\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.closeButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton_2.setGeometry(QtCore.QRect(310, 310, 121, 31))
        self.closeButton_2.setStyleSheet("background-color: rgb(174, 209, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: #00007f;\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-radius: 5px;\n"
"border-color: #00007f;\n"
"")
        self.closeButton_2.setObjectName("closeButton_2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-30, -30, 821, 691))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("\n"
"\n"
"background-color: rgb(207, 232, 255);\n"
"")
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(170, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_5.raise_()
        self.issueCheck2.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.closeButton_2.raise_()
        self.label_12.raise_()
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
        self.issueCheck2.setText(_translate("MainWindow", "In Stock"))
        self.titleLineedit.setText(_translate("MainWindow", "Nido"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Infant Formula"))
        self.categoryLine.setText(_translate("MainWindow", "400"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Wheat"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Sugar"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Milk"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Type:"))
        self.label_3.setText(_translate("MainWindow", "Price:"))
        self.label_4.setText(_translate("MainWindow", "Ingredients"))
        self.closeButton_2.setText(_translate("MainWindow", "Close"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00007f;\">Product Details</span></p></body></html>"))
