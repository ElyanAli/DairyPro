INSERT INTO Registrations (password, status) VALUES
('securePass', 'Inactive'),
('secretPwd', 'Active'),
('strongPwd', 'Active'),
('safeguard', 'Active');


INSERT INTO Customers (customer_name, address, phone_number, email, activity_status) VALUES
('Ahmed Khan', '23 ABC Street', 555-9876, 'ahmed@example.com', 'Inactive'),
('Sara Patel', '45 XYZ Road', 555-5432, 'sara@example.com', 'Active'),
('Raj Singh', '12 PQR Lane', 555-1234, 'raj@example.com', 'Active'),
('Priya Das', '21 HIJ Drive', 555-0123, 'priya@example.com', 'Active');

--select * from Customers;

INSERT INTO Distributors (company_name, representative_name, distribution_city, address, phone_number, email, performance_metric, activity_status) VALUES
('Global Distributors', 'Ravi Kumar', 'City A', '123 Maple Street', 555-1122, 'ravi@example.com', 'High', 'Active'),
('Super Distributors', 'Ayesha Singh', 'City B', '456 Oak Street', 555-3344, 'ayesha@example.com', 'Medium', 'Inactive'),
('Mega Distribution', 'Farhan Khan', 'City C', '789 Pine Street', 555-5566, 'farhan@example.com', 'Low', 'Active'),
('Pinnacle Distribution', 'Neha Singh', 'City J', '123 Cedar Street', 555-0011, 'neha@example.com', 'High', 'Inactive');

INSERT INTO Suppliers (supplier_name, address, supplying_city, phone_number, email, activity_status) VALUES
('Metro Suppliers', '78 ABC Street', 'City A', 555-9876, 'metro@example.com', 'Active'),
('Golden Suppliers', '23 XYZ Road', 'City B', 555-5432, 'golden@example.com', 'Active'),
('Best Suppliers', '56 PQR Lane', 'City C', 555-1234, 'best@example.com', 'Inactive'),
('Silver Suppliers', '21 HIJ Drive', 'City J', 555-0123, 'silver@example.com', 'Active');

INSERT INTO Employees (employee_name, address, phone_number, email, date_of_birth, designation, department, led_by, salary) VALUES
('Amit Sharma', '789 Maple Street', 5551122, 'amit@example.com', '1985-05-10', 'Manager', 'Sales', NULL, 60000),
('Sneha Verma', '345 Oak Street', 5553344, 'sneha@example.com', '1990-08-25', 'Supervisor', 'Production', 1, 50000),
('Rajeev Patel', '567 Cedar Street', 5555566, 'rajeev@example.com', '1988-12-15', 'Technician', 'Production', 2, 40000),
('Vikas Patel', '789 Cedar Street', 5551122, 'vikas@example.com', '1991-07-08', 'Supervisor', 'Production', 7, 48000);



INSERT INTO Category (category_name, category_description) VALUES
('Electronics', 'Electronic devices and gadgets'),
('Appliances', 'Home appliances'),
('Home Entertainment', 'TV and audio systems'),
('Small Appliances', 'Small kitchen gadgets');


INSERT INTO Orders (customer_id, employee_id, distributor_id, order_date, required_date, delivery_status, shipped_date, shipped_via, frieght, shipped_name, shipped_address, shipped_city, shipped_postalcode) VALUES
(1, 1, 1, '2023-11-01', '2023-11-10', 'Processing', NULL, 'Train', NULL, NULL, NULL, NULL, NULL),
(2, 2, 2, '2023-11-02', '2023-11-12', 'Shipped', '2023-11-05', 'Courier', 'Standard', 'Sara Patel', '45 XYZ Road', 'City B', '12345'),
(3, 3, 3, '2023-11-03', '2023-11-15', 'Delivered', '2023-11-08', 'Plain', 'Express', 'Raj Singh', '12 PQR Lane', 'City C', '67890'),
(4, 4, 4, '2023-11-04', '2023-11-18', 'Processing', NULL, 'Train', 'Standard', 'Priya Das', '21 HIJ Drive', 'City A', '34565');

INSERT INTO Products (product_name, category_id, price, continuity_status) VALUES
('Infant Formula', 1, 500.00, 'Available'),
('Tea whitener', 1, 1200.00, 'Available'),
('Powdered Milk', 2, 800.00, 'Out of Stock'),
('Nido', 3, 700.00, 'Available');

INSERT INTO Order_Details (order_id, product_id, quantity, price) VALUES
(1,1,2, 1000.00),
(2,2,1,1200.00),
(2, 3, 1, 800.00 ),
(3, 4, 1, 700.00);

INSERT INTO Raw_Material (material_name, supplier_id, cost, inventory_level, quality_metric)
VALUES
('Milk Base', 1, 3.99, 1000, 'High Quality Protein Source'),
('Tea Extract', 2, 1.49, 500, 'Natural Flavoring'),
('Sugar', 3, 2.99, 800, 'Refined Sweetener'),
('Vitamins and Minerals Mix', 4, 5.99, 300, 'Fortification for Nutrition');


INSERT INTO Products_RawMaterial (product_id, material_id)
VALUES
(1, 1), -- Fresh Milk is made from Milk Base
(2, 2), -- Tea is made from Tea Extract
(3, 3), -- Milk Whitener is made from Sugar
(4, 4);-- Infant Formula is made from Vitamins and Minerals Mix


INSERT INTO Warehouse (warehouse_address, warehouse_city, warehouse_phone_number, warehouse_lead)
VALUES
('123 Dairy Street', 'Lahore', 4567890, 'Ahmed Khan'),
('456 Milk Lane', 'Karachi', 6543210, 'Sara Ahmed'),
('789 Dairy Avenue', 'Islamabad', 5432109, 'Rizwan Malik'),
('234 Milk Boulevard', 'Faisalabad', 7382910, 'Aisha Ali');

select * from Warehouse;

INSERT INTO Section_Types (section_type, description)
VALUES
('Milk Storage', 'Section for storing various types of milk products'),
('Tea Storage', 'Section for storing tea-related products'),
('Whitener Storage', 'Section for storing milk whitener products'),
('Infant Formula Storage', 'Section for storing infant formula products');

INSERT INTO Warehouse_Section (warehouse_id, section_id)
VALUES
(1, 1), 
(2, 2), 
(3, 2), 
(4, 4); 

INSERT INTO Inventory_Warehouse (warehouse_id)
VALUES
(3),
(1),
(4),
(2);



INSERT INTO Manufacturing (product_id, production_date, expiry_date, quality_control)
VALUES
(1, '2023-01-05', '2023-02-05', 'High Quality Control'), -- Fresh Milk
(2, '2023-02-10', '2023-04-10', 'Premium Quality Control'), -- Tea
(3, '2023-03-15', '2023-06-15', 'Top Quality Control'), -- Milk Whitener
(4, '2023-04-20', '2023-09-20', 'Pediatric Quality Control'); -- Infant Formula

INSERT INTO Regulatory_Compliance (batch_id, managed_by, compliance_status)
VALUES
(1, 1, 'Compliant'), -- Batch 1 of Fresh Milk
(2, 2, 'Pending Approval'), -- Batch 2 of Tea
(3, 3, 'Approved'), -- Batch 3 of Milk Whitener
(4, 4, 'Under Review'); -- Batch 4 of Infant Formula

INSERT INTO Certifications (certification_id, certification_name, issued_by, issued_on)
VALUES
('CERT001', 'Quality Assurance', 'International Standards Organization', '2023-01-15'),
('CERT002', 'Organic Certification', 'Organic Certification Authority', '2023-02-20'),
('CERT003', 'Pediatric Safety', 'Health and Safety Authority', '2023-03-25'),
('CERT004', 'Product Excellence', 'Quality Control Certification Board', '2023-04-30');

INSERT INTO Checkpoint_Types (checkpoint_type, description)
VALUES
('Raw Material Inspection', 'Inspection of raw materials for quality and safety'),
('Production Quality Check', 'Quality check during the production process'),
('Final Product Inspection', 'Final inspection of the finished product'),
('Packaging Integrity Check', 'Verification of packaging for quality and safety');

INSERT INTO Quality_Control (batch_id, compliance_id, managed_by, checkpoint_type, inspection_result, corrective_actions)
VALUES
(1, 1, 1, 'Raw Material Inspection', 'Pass', 'None'), -- Fresh Milk
(2, 2, 2, 'Production Quality Check', 'Fail', 'Adjust Tea Extract quantity'), -- Tea
(3, 3, 3, 'Final Product Inspection', 'Pass', 'None'), -- Milk Whitener
(4, 4, 4, 'Packaging Integrity Check', 'Pending', 'Recheck packaging seals'); -- Infant Formula

select * from Certifications;


INSERT INTO RegulatoryCompliance_Certifications (Compliance_id, Certification_id)
VALUES
(1, 'CERT001'), -- Fresh Milk is compliant with Quality Assurance
(2, 'CERT002'), -- Tea is pending approval for Organic Certification
(3, 'CERT003'), -- Milk Whitener is compliant with Pediatric Safety
(4, 'CERT004'); -- Infant Formula is under review for Product Excellence