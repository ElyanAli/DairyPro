# Importing essential modules
import typing
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

# Replace these with your own database connection details
server = ''
database = 'DairyPro'  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = ''  # Specify a username if not using Windows Authentication
password = ''  # Specify a password if not using Windows Authentication

# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Main Window Class
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi('DB_Project/1 User Type.ui', self)
        self.setWindowTitle("Select Login Type")
        
        self.loginAdmin.clicked.connect(lambda: self.open_Login('Admin'))
        self.loginDistributor.clicked.connect(lambda: self.open_Login('Distributor'))
        self.loginSupplier.clicked.connect(lambda: self.open_Login('Supplier'))
        self.loginCustomer.clicked.connect(lambda: self.open_Login('Customer'))
        self.createAccount.clicked.connect(self.open_createAccountForm)
        # self.openLogin(self.type)
    def open_Login(self, type):
        self.loginDialog = Login(type)
        self.loginDialog.show()

    def open_createAccountForm(self):
        self.createDialog = CreateAccount()
        self.createDialog.show()


class CreateAccount(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreateAccount, self).__init__()

        uic.loadUi('DB_project/2 Sign up.ui', self)
        self.setWindowTitle("Create Account")

        self.createAccount_button.clicked.connect(self.insertCreate)
        self.cancel.clicked.connect(self.closeCreate)

    def insertCreate(self):
        # name = self.name.text()
        # phoneNum = self.phoneNum.text()
        # address = self.address.text()
        # userType = self.userType.currentText()
        # email = self.email.text()
        # password = self.password.text()
        # reEnterPassword = self.reEnterPassword.text()

        # # TODO: Provide the  connection string to connect to the Northwind database
        # connection = pyodbc.connect(connection_string)
        # cursor = connection.cursor()

        # if password == reEnterPassword:
        #     #Inserted in Registrations
        #     sql_query_registrations = """
        #     INSERT INTO Registrations ([Password], [Status]) 
        #     VALUES (?, ?)
        #     """

        #     # Execute the SQL query with parameter values
        #     cursor.execute(sql_query_registrations, (password, userType))
        #     connection.commit()

        #     #Insert In Others
        #     if userType == 'Customer':
        #         sql_query_customers = "INSERT INTO Customers ()"
        # else:
        #     QtWidgets.QMessageBox.warning(self, "Password Error", "The Two password don't Match")

        # # TODO: Write SQL query with parameters to insert order
        

        # # Retrieve the newly inserted order ID
        # cursor.execute("SELECT max(orderid) AS OrderID from orders")
        # result = cursor.fetchone()
        # order_id = result[0]

        # # Show a message box with the order ID
        # QtWidgets.QMessageBox.information(
        #     self, "Order Inserted", f"Order ID: {order_id} has been inserted successfully.")

        # # Close the database connection
        # connection.close()
        pass

    def closeCreate(self):
        self.close()



class Login(QtWidgets.QMainWindow):
    def __init__(self, typ):
        self.type = typ
        # Call the inherited classes __init__ method
        super(Login, self).__init__()

        # Load the .ui file
        uic.loadUi('DB_Project/3 Login screen.ui', self)

        # Connect Submit Button to Event Handling Code
        self.logInButton.clicked.connect(self.logIn)
        # if type == 'Admin':
        #     self.logInButton.clicked.connect(self.open_adminDashboard)
        # elif type == 'Distributor':
        #     self.logInButton.clicked.connect(self.open_distributorDashboard)
        # elif type == 'Supplier':
        #     self.logInButton.cliked.connect(self.open_supplierDashboard)
        # elif type == 'Customer':
        #     self.logInButton.clicked.connect(self.open_customerDashboard)
        self.createAccount.clicked.connect(self.open_createAccountForm)

    def logIn(self):
        id = self.userId.text()
        password = self.password.text()
        status = self.type

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        q = "SELECT * FROM Registrations WHERE id = ? AND Password = ? AND Status = ?"
        cursor.execute(q, (id, password, status))
        row = cursor.fetchone() 
        if row:
            if status == 'Admin':
                self.open_adminDashboard()
            elif status == 'Distributor':
                self.open_distributorDashboard()
            elif status == 'Supplier':
                self.open_supplierDashboard()
            elif status == 'Customer':
                self.open_customerDashboard()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")

    def open_createAccountForm(self):
        self.createDialog = CreateAccount()
        self.createDialog.show()

    def open_adminDashboard(self):
        #TODO Admin HERE
        pass

    def open_distributorDashboard(self):
        #TODO Distributor HERE
        pass

    def open_supplierDashboard(self):
        #TODO Supplier HERE
        pass
    
    def open_customerDashboard(self):
        #TODO Customer HERE
        pass


def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
