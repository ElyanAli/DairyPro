CREATE TABLE Registrations (
    id INT PRIMARY KEY IDENTITY(0001,1) NOT NULL,
    password NVARCHAR(255),
    user_type VARCHAR(255) NOT NULL
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    address NVARCHAR(MAX),
    phone_number NVARCHAR(11),
    email NVARCHAR(255),
    activity_status VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Registrations(id)
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY NOT NULL,
    employee_name VARCHAR(255) NOT NULL,
    address VARCHAR(MAX),
    phone_number NVARCHAR(11),
    email NVARCHAR(255),
    date_of_birth DATE,
    designation VARCHAR(255),
    department VARCHAR(255),
    led_by INT NULL,
    salary MONEY,
    FOREIGN KEY (employee_id) REFERENCES Registrations(id)
);

CREATE TABLE Category (
    category_id INT PRIMARY KEY IDENTITY(01,1) NOT NULL,
    category_name VARCHAR(255),
    category_description VARCHAR(255)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY IDENTITY(001,1) NOT NULL,
    product_name VARCHAR(255),
    category_id INT,
    price MONEY,
    continuity_status VARCHAR(255),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY IDENTITY(00001,1) NOT NULL,
    customer_id INT,
    employee_id INT NULL,
    distributor_id INT NULL,
    order_date DATE,
    required_date DATE,
    delivery_status VARCHAR(255),
    shipped_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);

CREATE TABLE Order_Details (
    order_id INT,
    product_id INT,
    quantity INT,
    price MONEY,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Warehouse (
    warehouse_id INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    warehouse_address NVARCHAR(255),
    warehouse_city VARCHAR(255),
    warehouse_phone_number NVARCHAR(11),
    warehouse_lead INT,
    FOREIGN KEY (warehouse_lead) REFERENCES Employees(employee_id)
);

CREATE TABLE Product_Inventory (
    product_id INT,
    warehouse_id INT,
    product_stock INT,
    PRIMARY KEY (product_id, warehouse_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id)
);

/*
DROP TABLE Product_Inventory;
DROP TABLE Warehouse;
DROP TABLE Order_Details;
DROP TABLE Orders;
DROP TABLE Products;
DROP TABLE Category;
DROP TABLE Employees;
DROP TABLE Customers;
DROP TABLE Registrations;
*/