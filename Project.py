#1.Create a database called “Inventory_Management” with different tables like “manufacture”, “goods”, “purchase”, “sale” etc.
import mysql.connector
mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password='Sahil*2002')
print(mydb.connection_id)
#create table Inventory_Management;


#3.In the “manufacture” table, one should be able to see all the products that need to be manufactured, and defective items during the manufacture with different entries like manufacture id, number of items required, etc. 
import mysql.connector
mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password='Sahil*2002')
cur=mydb.cursor()
print(mydb.connection_id)
creation = 'create table MANUFACTURE(id INTEGER(10) PRIMARY KEY,product_name VARCHAR(40),color VARCHAR(20),quantity INTEGER(10),manufacturing_date DATE,defective_ITEM VARCHAR(30),company_name varchar(40))'
cur.execute(creation)
print("Table created succesfully")


#4.In the “goods” table, it should include different items that are manufactured by the company along with the goods id, manufactured date, etc.
import mysql.connector
mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password='Sahil*2002')
cur=mydb.cursor()
print(mydb.connection_id)
creation = 'create table GOODS(id INTEGER(10),product_name varchar(40),color varchar(40),quantity INTEGER(10),manufacturing_date date)'
cur.execute(creation)
print("Table created succesfully")


#5.In the “purchase” table, it should include all the purchase details that are purchased in different online and offline stores, along with the purchase id, purchase amount, etc.
import mysql.connector
mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password='Sahil*2002')
cur=mydb.cursor()
print(mydb.connection_id)
creation = 'create table PURCHASE(id INTEGER(10),store_name TEXT,product_name varchar(10),color VARCHAR(20),quantity INTEGER(10),purchase_amount INTEGER(20),purchase_date DATE)'
cur.execute(creation)
print("Table created succesfully")


#6.In the “sale” table, it should include all the items got sold in different stores with the sale date, profit margin, etc
import mysql.connector
mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password='Sahil*2002')
cur=mydb.cursor()
print(mydb.connection_id)
creation = 'create table SALE(id INTEGER(10),store_name VARCHAR(40),product_name VARCHAR(40),color VARCHAR(10),no_of_items INTEGER(10),sale_amount REAL,sale_date DATE,profit_margin real)'
cur.execute(creation)
print("Table created succesfully")


#insertion values into tables 
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Tarak@2002',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
insertion1 = 'insert into MANUFACTURE(id,product_name,color,quantity,manufacturing_date,defective_ITEM,company_name) values(%s,%s,%s,%s,%s,%s,%s)'
values1 = [(1, 'Toy Car', 'Red', 100, '01-05-23', 0,'RR export'),(2, 'Toy Train', 'Green', 50, '01-05-23', 0,'SS Export'),(3, 'Wooden Chair', 'Brown', 200, '01-04-23', 0,'SS Export'),(4, 'Wooden Table', 'Brown', 100, '01-03-23', 0,'RR Export'),(5,'Shirt','Blue',10,'01-05-23',1,SS Export]
cur.executemany(insertion1,values1)
mydb.commit()
print("Data inserted succesfully")


import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Tarak@2002',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
insertion2 = 'insert into GOODS(id,product_name,color,quantity,manufacturing_date) values(%s,%s,%s,%s,%s)'
values2 = [(1, 'Toy Car', 'Red', 100, '01-05-23'),(2, 'Toy Ship', 'Green', 50, '01-05-23'),(3, 'Wooden Chair', 'Brown', 200, '01-04-23'),(4, 'Wooden Table', 'Brown', 100, '01-03-23'),(5,'Shirt','Blue',10,'01-05-23')]
cur.executemany(insertion2,values2)
mydb.commit()
print("Data inserted succesfully")



import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Tarak@2002',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
insertion3 = 'insert into PURCHASE(id,store_name,product_name,color,quantity,purchase_amount,purchase_date) values(%s,%s,%s,%s,%s,%s,%s)'
values3 = [(1, 'MyKids', 'Toy Car', 'Red', 50, 500, '01-05-23'),(2, 'MyKids', 'Toy Ship', 'Green', 25, 250, '01-05-23'),(3, 'ORay', 'Shirt', 'Blue',10,200,'01-05-23')]
cur.executemany(insertion3,values3)
mydb.commit()
print("Data inserted succesfully")



import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Tarak@2002',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
insertion4 = 'insert into SALE(id,store_name,product_name,color,no_of_items,sale_amount,sale_date,profit_margin) values(%s,%s,%s,%s,%s,%s,%s,%s)'
values4 = [(1, 'Offline', 'Toy Car', 'Green', 100, 800, '2023-04-05',10),
(2, 'Online', 'Toy Train', 'Green', 100, 800, '2023-01-05',12.2),
(3, 'Offlin', 'Wooden Chair', 'Green', 100, 800, '2023-04-10',15.6),
(4, 'Online', 'Wooden Table', 'Green', 100, 800, '2023-03-15',13.65),
(5, 'Offline', 'Toy Train', 'Green', 100, 800, '2023-09-25',18.65)]
cur.executemany(insertion4,values4)
mydb.commit()
print("Data inserted succesfully")



#7.Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Yogeshwar@123',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
dlelte_oray ="DELETE FROM purchase WHERE product_name = 'shirt' AND store_name = 'ORay' AND purchase_date = '2001-05-23'"
cur.execute(dlelte_oray)  
show_purchase = "select * from purchase"
cur.execute(show_purchase)  
print("Success")



#8.Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Yogeshwar@123',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
update_manufacure ="UPDATE manufacture SET quantity = '50' WHERE color = 'Red'"
cur.execute(update_manufacure)  
show_manufacture= "select * from manufacture"
cur.execute(show_manufacture)  
print("Success")



#9.Display all the “wooden chair” items that were manufactured before the 1st May 2023.
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Yogeshwar@123',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
display_wooden ="SELECT *FROM goods WHERE product_name = 'wood chair' AND manufacturing_date < '2001-05-23'"
cur.execute(display_wooden)  
print("Success")



#10.Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password='Yogeshwar@123',database = 'INVENTORY_MANAGEMENT')
cur=mydb.cursor()
profit_margin ="SELECT profit_margin FROM sale WHERE product_name = 'wood table' AND store_name = 'Mykids' AND id IN (  SELECT id  FROM manufacture  WHERE company_name = 'SS Export')"
cur.execute(profit_margin)
print("Success")
