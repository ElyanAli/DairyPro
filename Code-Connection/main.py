# Importing essential modules
import typing
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

# Replace these with your own database connection details
server = 'DESKTOP-G72O2BA'
database = 'DairyPro2'  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = 'ElyanAli2003'  # Specify a password if not using Windows Authentication

# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# MAIN
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/1 User Type.ui', self)
        self.setWindowTitle("Select Login Type")
        
        self.loginAdmin.clicked.connect(lambda: self.open_Login('Employee'))
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

# LOGIN
class Login(QtWidgets.QMainWindow):
    def __init__(self, typ):
        self.type = typ
        # Call the inherited classes __init__ method
        super(Login, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/3 Login screen.ui', self)

        # Connect Submit Button to Event Handling Code
        self.logInButton.clicked.connect(self.logIn)
        self.createAccount.clicked.connect(self.open_createAccountForm)

    def logIn(self):
        id = self.userId.text()
        password = self.password.text()
        user_type = self.type

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        q = "SELECT * FROM Registrations WHERE id = ? AND Password = ? AND User_Type = ?"
        cursor.execute(q, (id, password, user_type))
        row = cursor.fetchone() 
        if row:
            if user_type == 'Employee':
                self.open_adminDashboard(id)
            elif user_type == 'Distributor':
                self.open_distributorDashboard()
            elif user_type == 'Supplier':
                self.open_supplierDashboard(id)
            elif user_type == 'Customer':
                self.open_customerDashboard(id)
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
        
        connection.close()

    def open_createAccountForm(self):
        self.createDialog = CreateAccount()
        self.createDialog.show()

    def open_adminDashboard(self, current_id):
        self.startAdmin = AdminDashboard(current_id)
        self.startAdmin.show()

    def open_customerDashboard(self, current_id):
        self.startCustomerView = CustomerDashboard(current_id)
        self.startCustomerView.show()

    def open_supplierDashboard(self, current_id):
        # TODO Supplier HERE
        self.startSupplierView = SupplierDashboard(current_id)
        self.startSupplierView.show()

    def open_distributorDashboard(self):
        #TODO Distributor HERE
        pass

    
    

# CREATE ACCOUNT
class CreateAccount(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreateAccount, self).__init__()

        uic.loadUi('Screens/2 Sign up.ui', self)
        self.setWindowTitle("Create Account")

        self.createAccount_button.clicked.connect(self.insertCreate)
        self.cancel.clicked.connect(self.closeCreate)

    def insertCreate(self):
        name = self.name.text()
        phoneNum = self.phoneNum.text()
        address = self.address.toPlainText()
        userType = self.userType.currentText()
        email = self.email.text()
        password = self.password.text()
        reEnterPassword = self.reEnterPassword.text()

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        if password == reEnterPassword:
            #Inserted in Registrations
            sql_query_registrations = """
            INSERT INTO Registrations ([Password], [User_Type]) 
            VALUES (?, ?)
            """

            # Execute the SQL query with parameter values
            cursor.execute(sql_query_registrations, (password, userType))
            connection.commit()

            # Getting Registration
            latest = "SELECT IDENT_CURRENT('Registrations')"
            cursor.execute(latest)
            latest_id_into_registration = cursor.fetchone()[0]
            print(latest_id_into_registration)

            #Insert In Others
            if userType == 'Customer':
                activity_status = 'Active'
                sql_query_customers = "INSERT INTO Customers ([customer_id], [customer_name], [address], [phone_number], [email], [activity_status]) VALUES (?, ?, ?, ?, ?, ?)"
                cursor.execute(sql_query_customers, (int(latest_id_into_registration), name, address, phoneNum, email, activity_status))
                connection.commit()
                QtWidgets.QMessageBox.information(self, "Success", f"The registration was successful. Your {userType} id is {latest_id_into_registration}.")
        else:
            QtWidgets.QMessageBox.warning(self, "Password Error", "The Two password don't Match")

        connection.close()

    def closeCreate(self):
        self.close()

class AdminDashboard (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(AdminDashboard, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/4 Admin dashboard.ui', self)

        # self.productView.clicked.connect(self.open_productView)
        # self.inventoryView.clicked.connect(self.open_inventoryView)
        # self.rawmatView.clicked.connect(self.open_rawmatView)
        # self.orderView.clicked.connect(self.open_orderView)
        # self.distributorView.clicked.connect(self.open_distributorView)
        # self.manufactureView.clicked.connect(self.open_manufactureView)
        # self.supplierView.clicked.connect(self.open_supplierView)
        # self.exitDatabase.clicked.connect(self.open_exitDatabase)
        # print(self.current_id)
        # self.customerView.clicked.connect(lambda: self.open_customerView(current_id))
        self.currentOrders.clicked.connect(lambda: self.open_currentOrders(current_id))
    
    # def open_productView(self):
    #     self.startProductView = AdminProductView()
    #     self.startProductView.show()
    #     pass
    # def open_inventoryView(self):
    #     pass
    # def open_rawmatView(self):
    #     pass
    # def open_distributorView(self):
    #     pass
    # def open_manufactureView(self):
    #     pass
    # def open_supplierView(self):
    #     pass
    # def open_customerView(self):
    #     pass
    # def open_exitDatabase(self):
    #     pass

    def open_currentOrders(self, current_id):
        self.startCurrentOrders = CurrentOrders(current_id)
        self.startCurrentOrders.show()

class CurrentOrders (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CurrentOrders, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/5 Admin Order Approve.ui', self)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        searchOrdersForApproval = "SELECT order_id, customer_id, order_date, required_date from Orders where employee_id is NULL"
        cursor.execute(searchOrdersForApproval)
        # for i in cursor.fetchall():
        #     self.pendingOrderTable.
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.pendingOrderTable.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.pendingOrderTable.setItem(row_index, col_index, item)

        fillEmployeeComboBox = "SELECT employee_name from Employees where department = ?"
        cursor.execute(fillEmployeeComboBox, "Sales")

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.employeeToBeAssigned.addItem(str(cell_data))

        connection.close()

        self.approveOrder.clicked.connect(lambda: self.transact_approveOrder(self.employeeToBeAssigned.currentText()))
        self.closeButton.clicked.connect(self.closeScreen)
        # header = self.pendingOrderTable.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        # header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
    
    def closeScreen(self):
        self.close()

    def transact_approveOrder(self, employee_name):
        selected_items = self.pendingOrderTable.selectedItems()

        if len(selected_items) > 0:
            selected_item = selected_items[0]
            selected_row = selected_item.row()

            # Get all items in the selected row
            row_items = []
            for col in range(self.pendingOrderTable.columnCount()):
                item = self.pendingOrderTable.item(selected_row, col)
                if item is not None:
                    row_items.append(item.text())

            # print(f"Selected Row {selected_row} Items: {row_items}")
            order_id = row_items[0]
            customer_id = row_items[1]
            order_date = row_items[2]
            required_date = row_items[3]

            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()

            selectEmployeeId = "select employee_id from Employees where employee_name = ?"
            cursor.execute(selectEmployeeId, employee_name)
            employee_id = cursor.fetchone()[0]
            # print(employee_id)
            
            getDate = "SELECT CONVERT(DATE, GETDATE(), 103) AS CurrentDate"
            cursor.execute(getDate)
            today = cursor.fetchone()[0]
            updateOrder = "UPDATE Orders SET Employee_id = ?, delivery_status = ?, shipped_date = ? where Order_id = ?"
            cursor.execute(updateOrder, employee_id, 'Delivered', today, order_id)
            cursor.commit()

            fetchOrderProducts = "Select * from Order_Details where order_id = ?"
            cursor.execute(fetchOrderProducts, order_id)
            temp = cursor.fetchall()
            for i in temp:
                product_id = i[1]
                quantity = i[2]
                updateProductInventory = "update Product_Inventory SET product_stock = product_stock - ? where product_id = ?;"
                cursor.execute(updateProductInventory, int(quantity), int(product_id))
                cursor.commit()

            connection.close()
        else:
            print("No item selected.")

class CustomerDashboard (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CustomerDashboard, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/25 Customer Dashboard.ui', self)

        # connection = pyodbc.connect(connection_string)
        # cursor = connection.cursor()

        self.orders.clicked.connect(lambda: self.open_customerOrders(current_id))
    
    def open_customerOrders(self, current_id):
        #To be Editied TODO
        # self.startCustomerOrders = CustomerOrdersView()
        self.startCustomerOrders = CustomerPlaceOrder(current_id)
        self.startCustomerOrders.show()

class CustomerPlaceOrder (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(CustomerPlaceOrder, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/45 Customer Order Placing.ui', self)

        self.customer_id.setText(str(current_id))
        self.customer_id.setEnabled(False)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchCustomerName = "SELECT customer_name from Customers where customer_id = ?"
        cursor.execute(fetchCustomerName, current_id)
        name = cursor.fetchone()[0]
        self.customer_name.setText(str(name))
        self.customer_name.setEnabled(False)

        # print(QDate.currentDate())
        order_date = QDate.currentDate()
        self.order_date.setDate(order_date)
        self.order_date.setEnabled(False)

        self.required_date.setDate(order_date)
        #if statements to be added req date > order date

        fetchAllProducts = "SELECT product_name from Products where continuity_status = 'True'"
        cursor.execute(fetchAllProducts)
        for i in cursor.fetchall():
            self.available_products.addItem(i[0])

        self.add_to_cart.clicked.connect(self.AddProductToCart)
        self.place_order.clicked.connect(self.PlaceOrder)
        self.cancel.clicked.connect(self.cancelPlaceOrder)
        # self.total.setText("{:.2f}".format(0.00))
        self.total.setText(str(0.00))
        self.total.setEnabled(False)
        connection.close()

    def cancelPlaceOrder(self):
        self.close()
    
    def PlaceOrder(self):
        customer_id = self.customer_id.text()
        customer_name = self.customer_name.text()
        order_date = self.order_date.date().toString("yyyy-MM-dd")
        required_date = self.required_date.date().toString("yyyy-MM-dd")
        # print(order_date, required_date)

        products_to_be_ordered = []
        for row in range(self.productTable.rowCount()):
            row_items = []
            for col in range(self.productTable.columnCount()):
                item = self.productTable.item(row, col)
                if item is not None:
                    row_items.append(item.text())
                else:
                    row_items.append(None)

            products_to_be_ordered.append(row_items)
        
        print(products_to_be_ordered)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        if products_to_be_ordered != []:
            insertIntoOrders = "INSERT INTO Orders (customer_id, employee_id, order_date, required_date, delivery_status, shipped_date) VALUES (?, NULL, ?, ?, 'Pending', NULL)"
            cursor.execute(insertIntoOrders, customer_id, order_date, required_date)
            cursor.commit()
            latest_in_order = "SELECT IDENT_CURRENT('Orders')"
            cursor.execute(latest_in_order)
            order_id = cursor.fetchone()[0]
            print(order_id)

            for i in products_to_be_ordered:
                product_id = i[0]
                quantity = i[2]
                total_product_price = i[4]
                #Multiple Inserts here.
                insertIntoOrderDetails = "INSERT INTO Order_Details (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)"
                cursor.execute(insertIntoOrderDetails, order_id, product_id, quantity, total_product_price)
                cursor.commit()
            
            QtWidgets.QMessageBox.information(self, "Success", f"Order successfully generated. Your order ID is: {order_id}.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", f"Order generation failed as there are no products in the cart.")


    def AddProductToCart(self):
        try:
            quantity = int(self.quantity.text())
            product_name = self.available_products.currentText()

            num_rows = self.productTable.rowCount()
            flag = False
            for row in range(num_rows):
                product_name_in_table = self.productTable.item(row, 1).text()
                if product_name_in_table == product_name:
                    flag = True
                    product_id_in_table = self.productTable.item(row, 0).text()
                    quantity_in_table = self.productTable.item(row, 2).text()
                    product_price_in_table = self.productTable.item(row, 3).text()
                    product_total_in_table = self.productTable.item(row, 4).text()

                    total_quantity = int(quantity_in_table) + quantity
                    total_price = float(product_total_in_table) + (quantity * float(product_price_in_table))
                    connection = pyodbc.connect(connection_string)
                    cursor = connection.cursor()

                    checkInventory = "SELECT Product_stock from Product_Inventory where product_id = ?"
                    cursor.execute(checkInventory, product_id_in_table)
                    product_stock_in_table = int(cursor.fetchone()[0])
                    if product_stock_in_table >= total_quantity:
                        #Replace the total quantity and new price
                        total_price = round(total_price, 2)
                        self.productTable.setItem(row, 2, QTableWidgetItem(str(total_quantity)))
                        self.productTable.setItem(row, 4, QTableWidgetItem(str(total_price)))

                        #ERROR: Calculating Fault
                        final_total = float(self.total.text())
                        final_total += float(total_price)
                        final_total = round(final_total, 2)
                        self.total.setText(str(final_total))
                    else:
                        QtWidgets.QMessageBox.warning(self, "Error", f"Failed to add to cart. Only {product_stock_in_table} units of the product named '{product_name}' are available, and {total_quantity} units are requested for addition.")

            if not(flag):
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()

                getId = "SELECT product_id, price from products where product_name = ?"
                cursor.execute(getId, product_name)
                temp = cursor.fetchone()
                # print(temp)
                product_id = int(temp[0])
                product_price = float(temp[1])
                # print(product_id, product_price)

                checkInventory = "SELECT Product_stock from Product_Inventory where product_id = ?"
                cursor.execute(checkInventory, product_id)
                product_stock = int(cursor.fetchone()[0])
                # print(product_stock)

                if product_stock >= quantity:
                    product_total = quantity * product_price
                    product_total = round(product_total, 2)
                    self.productTable.insertRow(self.productTable.rowCount())
                    self.productTable.setItem(self.productTable.rowCount() - 1, 0, QTableWidgetItem(str(product_id)))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 1, QTableWidgetItem(product_name))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 2, QTableWidgetItem(str(quantity)))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 3, QTableWidgetItem(str(product_price)))
                    self.productTable.setItem(self.productTable.rowCount() - 1, 4, QTableWidgetItem(str(product_total)))
                    # self.productTable.add_table_item(str(product_id), product_name, str(product_price), str(product_total))
                    final_total = float(self.total.text())
                    final_total += float(product_total)
                    final_total = round(final_total, 2)
                    self.total.setText(str(final_total))
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", f"Only {product_stock} units of the product named '{product_name}' are remaining.") 

                connection.close()

        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", f"Quantity must be a numeric value.")
        
class SupplierDashboard (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(SupplierDashboard, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/39 supplier dashboard.ui', self)

        self.send_order.clicked.connect(lambda: self.open_generateOrder(self.current_id))
        self.supp_info.clicked.connect(lambda: self.open_supplierInfo(self.current_id))

    def open_generateOrder(self, current_id):
        self.startRawMaterialMaster = SupplierRawMaterials(current_id)
        self.startRawMaterialMaster.show()

    def open_supplierInfo(self, current_id):
        self.startsupplierInfoView = SupplierInformation(current_id)
        self.startsupplierInfoView.show()

class SupplierGenerateOrder (QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        # Call the inherited classes __init__ method
        super(SupplierGenerateOrder, self).__init__()

        # Load the .ui file
        uic.loadUi('Screens/42 Supplier Generate Order Form.ui', self)

        self.supplier_id.setText(current_id)
        self.supplier_id.setEnabled(False)

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fetchMaterials = "SELECT material_name from Raw_Material"
        cursor.execute(fetchMaterials)

        for row_data in cursor.fetchall():
            for cell_data in row_data:
                self.material_name.addItem(str(cell_data))
        
        getDate = "SELECT CONVERT(DATE, GETDATE(), 103) AS CurrentDate"
        cursor.execute(getDate)
        today = cursor.fetchone()[0]

        self.order_date.setDate(today)
        self.order_date.setEnabled(False)

        self.generate_order.clicked.connect(lambda: self.tranactionSupplierGenerateOrder(self.material_name.currentText(), int(self.quantity.text())))

        connection.close()

    def tranactionSupplierGenerateOrder(self, material_name, quantity):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        fetchMaterialId = "SELECT material_id from Raw_Material where material_name = ?"
        cursor.execute(fetchMaterialId, material_name)
        material_id = cursor.fetchone()[0]
        print(material_id)

        updateRawMaterialInventory = "UPDATE Material_Inventory SET material_stock = material_stock + ? where material_id = ?"
        cursor.execute(updateRawMaterialInventory, quantity, material_id)
        cursor.commit()

        connection.close()

class SupplierInformation(QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        super(SupplierInformation, self).__init__()
        uic.loadUi('Screens/43 Supplier info form.ui', self)
        self.setWindowTitle("Supplier Information")

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        #detch data from raw_mat table 
        query = "select * from Suppliers where supplier_id = ?"
        cursor.execute(query, current_id)

        row = cursor.fetchone() 
        self.closeButton.clicked.connect(self.view_close)
        print(row)
        suppID = row[0]
        suppName = row[1]
        suppAdd = row[2]
        suppPhone = row[3]
        suppEmail = row[4]
        suppActStatus = row[5]

        self.supp_id.setText(str(suppID))
        self.supp_name.setText(str(suppName))
        self.supp_addr.setText(str(suppAdd))
        self.supp_phone.setText(str(suppPhone))
        self.supp_email.setText(str(suppEmail))
        self.supp_act_status.setText(str(suppActStatus))

        # Disable QLineEdit widgets
        self.supp_id.setEnabled(False)
        self.supp_name.setEnabled(False)
        self.supp_addr.setEnabled(False)
        self.supp_phone.setEnabled(False)
        self.supp_email.setEnabled(False)
        self.supp_act_status.setEnabled(False)

    def view_close(self):
        self.close()

class SupplierRawMaterials(QtWidgets.QMainWindow):
    def __init__(self, current_id):
        self.current_id = current_id
        super(SupplierRawMaterials, self).__init__()
        
        uic.loadUi('Screens/40 Supplier Order form.ui', self)
        self.setWindowTitle("Materials Supplied")
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        fillSupplierOrders = "select R.material_name, R.cost, MI.material_stock from Raw_Material R INNER JOIN Material_Inventory MI ON R.material_id = MI.material_id where R.supplier_id = ?"
        cursor.execute(fillSupplierOrders, current_id)
        
        for row_index, row_data in enumerate(cursor.fetchall()):
            self.booksTableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.booksTableWidget.setItem(row_index, col_index, item)

        #TODO: Change Material Name Liine edit to ComboBOX
        connection.close()

        self.supp_order_search.clicked.connect(self.suppMaterialSearch)
        self.viewButton.clicked.connect(lambda: self.viewMaterial_clicked(current_id))
        self.closeButton.clicked.connect(self.view_close)
        self.generateOrder.clicked.connect(lambda: self.generate_Order_Clicked(current_id))
    

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

    def viewMaterial_clicked(self, current_id):
        selected_row = self.booksTableWidget.currentRow()
        # material_id = self.booksTableWidget.item(selected_row, 0)
        # material_name = self.booksTableWidget.item(selected_row, 1)
        # supplier_id = self.booksTableWidget.item(selected_row, 2)
        # cost = self.booksTableWidget.item(selected_row, 3)
        # inventory_level = self.booksTableWidget.item(selected_row, 4)
        # quality_metric = self.booksTableWidget.item(selected_row, 5)
        if selected_row >= 0:
            # material_id = self.booksTableWidget.item(selected_row, 0)
            material_name = self.booksTableWidget.item(selected_row, 0)
            # supplier_id = self.booksTableWidget.item(selected_row, 2)
            cost = self.booksTableWidget.item(selected_row, 1)
            inventory_level = self.booksTableWidget.item(selected_row, 2)
            #############
            self.viewMat = viewRawMaterial(material_name, current_id, cost,inventory_level)
            self.viewMat.show()

    def view_close(self):
        self.close()

    #TODO: RESOLVE SEARCH
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
    def generate_Order_Clicked(self, current_id):

        self.startSupplierOrderGen = SupplierGenerateOrder(current_id)
        self.startSupplierOrderGen.show()
        
class viewRawMaterial(QtWidgets.QMainWindow):
    def __init__(self, material_name, supplier_id, cost, inventory_level):
        super(viewRawMaterial, self).__init__()
        
        uic.loadUi('Screens/41 Supplier View Order Form.ui', self)
        self.setWindowTitle("Material Info")

        self.closeButton.clicked.connect(self.view_close)

        self.mat_name.setText(str(material_name.text()))
        self.sup_id.setText(str(supplier_id))
        self.cost_line.setText(str(cost.text()))
        self.inven_levl.setText(str(inventory_level.text()))

        # Disable QLineEdit widgets
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