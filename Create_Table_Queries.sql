CREATE TABLE Registrations (
    id INT PRIMARY KEY IDENTITY(1,1),
    password NVARCHAR(255),
    status VARCHAR(255)
);


CREATE TABLE Customers (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    customer_name VARCHAR(255),
    address NVARCHAR(255),
    phone_number BIGINT,
    email NVARCHAR(255),
    activity_status VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Registrations(id)
);
--ALTER TABLE Customers
--ALTER COLUMN phone_number BIGINT;

CREATE TABLE Distributors (
    distributor_id INT PRIMARY KEY IDENTITY(1,1),
    company_name VARCHAR(255),
    representative_name VARCHAR(255),
    distribution_city VARCHAR(255),
    address NVARCHAR(255),
    phone_number BIGINT,
    email NVARCHAR(255),
    performance_metric VARCHAR(255),
    activity_status VARCHAR(255),
    FOREIGN KEY (distributor_id) REFERENCES Registrations(id)
);

--ALTER TABLE Distributors
--ALTER COLUMN phone_number BIGINT;

CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY IDENTITY(1,1),
    supplier_name VARCHAR(255),
    address VARCHAR(255),
    supplying_city VARCHAR(255),
    phone_number BIGINT,
    email NVARCHAR(255),
    activity_status VARCHAR(255),
    FOREIGN KEY (supplier_id) REFERENCES Registrations(id)
);
--ALTER TABLE Suppliers
--ALTER COLUMN phone_number BIGINT;

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY IDENTITY(1,1),
    employee_name VARCHAR(255),
    address VARCHAR(255),
    phone_number BIGINT,
    email NVARCHAR(255),
    date_of_birth DATE,
    designation VARCHAR(255),
    department VARCHAR(255),
    led_by INT,
    salary MONEY,
    FOREIGN KEY (employee_id) REFERENCES Registrations(id)
);

CREATE TABLE Category (
    category_id INT PRIMARY KEY IDENTITY(1,1),
    category_name VARCHAR(255),
    category_description VARCHAR(255)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY IDENTITY(1,1),
    product_name VARCHAR(255),
    category_id INT,
    price MONEY,
    continuity_status VARCHAR(255),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY IDENTITY(1,1),
    customer_id INT,
    employee_id INT,
    distributor_id INT,
    order_date DATE,
    required_date DATE,
    delivery_status VARCHAR(255),
    shipped_date DATE,
    shipped_via VARCHAR(255),
    frieght VARCHAR(255),
    shipped_name VARCHAR(255),
    shipped_address NVARCHAR(255),
    shipped_city VARCHAR(255),
    shipped_postalcode VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (distributor_id) REFERENCES Distributors(distributor_id)
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


CREATE TABLE Raw_Material (
    material_id INT PRIMARY KEY IDENTITY(1,1),
    material_name VARCHAR(255),
    supplier_id INT,
    cost MONEY,
    inventory_level INT,
    quality_metric VARCHAR(255),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Products_RawMaterial (
    product_id INT,
    material_id INT,
    PRIMARY KEY (product_id, material_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (material_id) REFERENCES Raw_Material(material_id)
);



CREATE TABLE Warehouse (
    warehouse_id INT PRIMARY KEY IDENTITY(1,1),
    warehouse_address NVARCHAR(255),
    warehouse_city VARCHAR(255),
    warehouse_phone_number INT,
    warehouse_lead VARCHAR(255)
);



CREATE TABLE Section_Types (
    section_id INT PRIMARY KEY IDENTITY(1,1),
    section_type VARCHAR(255),
    description NVARCHAR(255)
);


CREATE TABLE Warehouse_Section (
    warehouse_id INT,
    section_id INT,
    PRIMARY KEY (warehouse_id, section_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id),
    FOREIGN KEY (section_id) REFERENCES Section_Types(section_id)
);


CREATE TABLE Inventory_Warehouse (
    product_or_material_id INT PRIMARY KEY IDENTITY(1,1),
    warehouse_id INT,
    FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id)
);

ALTER TABLE Inventory_Warehouse
	ADD CONSTRAINT FK_product_or_material_id
	FOREIGN KEY (product_or_material_id) REFERENCES Products(product_id);

ALTER TABLE Inventory_Warehouse
	ADD CONSTRAINT FK_material
	FOREIGN KEY (product_or_material_id) REFERENCES Raw_Material(material_id);

CREATE TABLE Manufacturing (
    batch_id INT PRIMARY KEY IDENTITY(1,1),
    product_id INT,
    production_date DATE,
    expiry_date DATE,
    quality_control VARCHAR(255),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


CREATE TABLE Regulatory_Compliance (
    compliance_id INT PRIMARY KEY IDENTITY(1,1),
    batch_id INT,
    managed_by INT,
    compliance_status VARCHAR(255),
    FOREIGN KEY (batch_id) REFERENCES Manufacturing(batch_id),
    FOREIGN KEY (managed_by) REFERENCES Employees(employee_id)
);


CREATE TABLE Certifications (
    certification_id VARCHAR(255) PRIMARY KEY,
    certification_name VARCHAR(255),
    issued_by VARCHAR(255),
    issued_on DATE
);


CREATE TABLE Checkpoint_Types (
    checkpoint_type VARCHAR(255) PRIMARY KEY,
    description NVARCHAR(255)
);



CREATE TABLE Quality_Control (
    checkpoint_id INT PRIMARY KEY IDENTITY(1,1),
    batch_id INT,
    compliance_id INT,
    managed_by INT,
    checkpoint_type VARCHAR(255),
    inspection_result NVARCHAR(255),
    corrective_actions NVARCHAR(255),
    FOREIGN KEY (batch_id) REFERENCES Manufacturing(batch_id),
    FOREIGN KEY (compliance_id) REFERENCES Regulatory_Compliance(compliance_id),
    FOREIGN KEY (managed_by) REFERENCES Employees(employee_id),
    FOREIGN KEY (checkpoint_type) REFERENCES Checkpoint_Types(checkpoint_type)
);


CREATE TABLE RegulatoryCompliance_Certifications (
    Compliance_id INT,
    Certification_id VARCHAR(255),
    PRIMARY KEY (Compliance_id, Certification_id),
    FOREIGN KEY (Compliance_id) REFERENCES Regulatory_Compliance(compliance_id),
    FOREIGN KEY (Certification_id) REFERENCES Certifications(certification_id)
);
