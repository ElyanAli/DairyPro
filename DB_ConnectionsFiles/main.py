# Importing essential modules
import typing
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

# Replace these with your own database connection details
server = 'SARAH'
database = 'DairyPro'  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = 'dbfall2023'  # Specify a password if not using Windows Authentication

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
        
        uic.loadUi('DB_ConnectionsFiles/DB_project/1 User Type.ui', self)
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

        uic.loadUi('DB_ConnectionsFiles/DB_project/2 Sign up.ui', self)
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
        uic.loadUi('DB_ConnectionsFiles/DB_Project/3 Login screen.ui', self)

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
                self.open_supplierDashboard(id)
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

    def open_supplierDashboard(self, id):
        #TODO Supplier HERE
        self.suplierDashDialog = supplierDashboard(id)
        self.suplierDashDialog.show()
        # pass
    
    def open_customerDashboard(self):
        #TODO Customer HERE
        pass


class supplierDashboard(QtWidgets.QMainWindow):
    def __init__(self, id):
        super(supplierDashboard, self ).__init__()

        uic.loadUi('DB_ConnectionsFiles/DB_project/39 supplier dashboard.ui', self)
        self.setWindowTitle("Suplier Dahboard")
        
        #supplier order clicked
        self.sup_dash_rawMat.clicked.connect(self.open_supplier_rawMat)
        self.supp_info.clicked.connect(lambda: self.open_supplier_info(id))
    def open_supplier_rawMat(self):
        self.suppOrderview = SupplierRawMaterials()
        self.suppOrderview.show()
        self.suppOrderview.populate_supp_rawMat()
        

    def open_supplier_info(self, id):
        self.suppInfoView = SupplierInformation(id)
        self.suppInfoView.show()



class SupplierInformation(QtWidgets.QMainWindow):
    def __init__(self, id):
        super(SupplierInformation, self).__init__()
        uic.loadUi('DB_ConnectionsFiles/DB_project/43 Supplier info form.ui', self)
        self.setWindowTitle("Supplier Information")

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #detch data from raw_mat table 
        query = "select * from Suppliers where supplier_id = ?"

        cursor.execute(query, (id))

        row = cursor.fetchone() 
        self.closeButton.clicked.connect(self.view_close)
        # print(row)
        suppID = row[0]
        suppName = row[1]
        suppCity = row[3]
        suppAdd = row[2]
        suppPhone = row[4]
        suppEmail = row[5]

        self.supp_id.setText(str(suppID))
        self.supp_name.setText(str(suppName))
        self.city.setText(str(suppCity))
        self.supp_addr.setText(str(suppAdd))
        self.supp_phone.setText(str(suppPhone))
        self.supp_email.setText(str(suppEmail))

        # Disable QLineEdit widgets
        self.supp_id.setEnabled(False)
        self.supp_name.setEnabled(False)
        self.city.setEnabled(False)
        self.supp_addr.setEnabled(False)
        self.supp_phone.setEnabled(False)
        self.supp_email.setEnabled(False)

    def view_close(self):
        self.close()














# suppRawMatSearch
class SupplierRawMaterials(QtWidgets.QMainWindow):
    def __init__(self):
        super(SupplierRawMaterials, self).__init__()
        
        uic.loadUi('DB_ConnectionsFiles/DB_project/40 Supplier Order form.ui', self)
        self.setWindowTitle("Materials Supplied")

        self.supp_order_search.clicked.connect(self.suppMaterialSearch)
        self.viewButton.clicked.connect(self.viewMaterial_clicked)
        self.closeButton.clicked.connect(self.view_close)

        

    def populate_supp_rawMat(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Clear existing rows in the table
        self.booksTableWidget.setRowCount(0)

        #detch data from raw_mat table 
        cursor.execute("select * from Raw_Material")

        # Fetch all rows and populate the table
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        #close database connection
        connection.close()

    def viewMaterial_clicked(self):
        selected_row = self.booksTableWidget.currentRow()
        material_id = self.booksTableWidget.item(selected_row, 0)
        material_name = self.booksTableWidget.item(selected_row, 1)
        supplier_id = self.booksTableWidget.item(selected_row, 2)
        cost = self.booksTableWidget.item(selected_row, 3)
        inventory_level = self.booksTableWidget.item(selected_row, 4)
        # quality_metric = self.booksTableWidget.item(selected_row, 5)
        self.viewMat = viewRawMaterial(material_id, material_name, supplier_id, cost,inventory_level)
        self.viewMat.show()

    def view_close(self):
        self.close()

    def suppMaterialSearch(self):
        material_id = self.supp_mat_id.text()
        supp_id = self.supp_id.text()
        material_name = self.mat_name.text()

        for row in range(self.booksTableWidget.rowCount()):
            m_id = self.booksTableWidget.item(row, 0).text() if self.booksTableWidget.item(row, 0) is not None else ""
            s_id = self.booksTableWidget.item(row, 2).text() if self.booksTableWidget.item(row, 1) is not None else ""
            m_name = self.booksTableWidget.item(row, 1).text() if self.booksTableWidget.item(row, 2) is not None else ""
            
            if not material_id and not supp_id and not material_name:
                self.booksTableWidget.setRowHidden(row, False)
            else:
                # Show the row if at least one criterion matches
                if m_id == material_id or s_id == supp_id or m_name == material_name:
                    self.booksTableWidget.setRowHidden(row, False)
                else:
                    self.booksTableWidget.setRowHidden(row, True)

class viewRawMaterial(QtWidgets.QMainWindow):
    def __init__(self, material_id, material_name, supplier_id, cost, inventory_level):
        super(viewRawMaterial, self).__init__()
        
        uic.loadUi('DB_ConnectionsFiles/DB_project/41 Supplier View Order Form.ui', self)
        self.setWindowTitle("Material Info")

        self.closeButton.clicked.connect(self.view_close)

        # self.matID = material_id
        # self.matName = material_name
        # self.suppID = supplier_id
        # self.cost = cost
        # self.inveLevl = inventory_level
        

        self.mat_id.setText(str(material_id.text()))
        self.mat_name.setText(str(material_name.text()))
        self.sup_id.setText(str(supplier_id.text()))
        self.cost_line.setText(str(cost.text()))
        self.inven_levl.setText(str(inventory_level.text()))

        # Disable QLineEdit widgets
        self.mat_id.setEnabled(False)
        self.mat_name.setEnabled(False)
        self.sup_id.setEnabled(False)
        self.cost_line.setEnabled(False)
        self.inven_levl.setEnabled(False)

    def view_close(self):
        self.close()
        




def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
