import mysql.connector as mysql

#------Creating database project----------
createdb = mysql.connect(
  host="localhost",
  user="root",
  password="root"
)

mycursor = createdb.cursor()

mycursor.execute("CREATE DATABASE project")
createdb.close()

#-----------connecting to the created database-----------------

db=mysql.connect(host = 'localhost',user='root',passwd="root",database='project')
c=db.cursor()
s = '''
create table Types_of_Appliances (
SrNo int PRIMARY KEY,
Type varchar(255),
No_of_Models int,
Price_Range varchar(255));
insert into Types_of_Appliances values
('1.', 'Washing Machines', '5', '7290-15990'), 
('2.', 'Microwave Ovens', '7', '5890-14490'), 
('3.', 'Air Conditioners', '7', '24790-39990'), 
('4.', 'Chimneys', '4', '4599-11999'), 
('5.', 'Refigerators', '5', '20800-32690');
create table washing_machines (
SrNo int PRIMARY KEY,
Model varchar(255),
Sale_Price int,
MRP varchar(255),
Warranty varchar(255));
insert into washing_machines values
('1.', 'Thomson 7kg Semi Automatic Top Load', '7290', '10499 - 30% off', '2 Years Warranty on Product and 4 Years on Motor'),
('2.', 'SAMSUNG 7.2 kg with Double Storm Technology Semi Automatic Top Load', '9690', '13100 - 26% off', '2 Years Warranty on Product and 5 Years on Motor'),
('3.', 'LG 8 kg 5 Star Rating Semi Automatic Top Load', '16990', '13500 - 20% off','2 Years Warranty on Product and 5 Years on Motor'),
('4.', 'SAMSUNG 6.5 kg Diamond Drum feature Fully Automatic Top Load', '14190', '16800 - 15% off', '2 Years Warranty on Product and 2 Years on Motor'),
('5.', 'LG 6.5 kg 5 Star Inverter Fully Automatic Top Load', '15990', '18490 - 13% off', '2 Years Warranty on Product and 10 Years on Motor');
create table microwave_ovens (
SrNo int PRIMARY KEY,
Model varchar(255),
Sale_Price int,
MRP varchar(255),
Warranty varchar(255));
insert into microwave_ovens values
('1.', 'SAMSUNG 23 L Solo Microwave Oven', '5890', '7590 - 22% off', '1 Year Standard Warranty'),
('2.', 'Whirlpool 20 L Solo Microwave Oven', '6099', '7000 - 12% off', '1 Year Warranty on Product and 2 Years on Magnetron'),
('3.', 'SAMSUNG 23 L Grill Microwave Oven', '7400', '11050 - 33% off','1 Years Warranty on Product and 3 Years on Magnetron'),
('4.', 'Whirlpool 30 L Convection Microwave Oven', '9299', '19500 - 52% off', '2 Years Warranty on Product and 3 Years on Magnetron'),
('5.', 'SAMSUNG 28 L Slim Fry Convection Microwave Oven', '11590', '14990 - 22% off', '1 Years Warranty on Product and 4 Years on Magnetron'),
('6.', 'IFB 30 L Convection Microwave Oven', '13749', '17990 - 23% off', '1 Years Warranty on Product and 3 Years on Magnetron'),
('7.', 'SAMSUNG 28 L Convection Microwave Oven', '14490', '17690 - 18% off', '1 Years Warranty on Product and 4 Years on Magnetron');
create table air_conditioners (
SrNo int PRIMARY KEY,
Model varchar(255),
Sale_Price int,
MRP varchar(255),
Warranty varchar(255),
Star_Rating varchar(255));
insert into air_conditioners values
('1.', 'Blue Star 1 Ton Window AC', '24790', '29500 - 16% off', '1 Year Warranty on Product and 5 years on Compressor', '3 Star'),
('2.', 'CARRIER 1.5 Ton Window AC', '26990', '35990 - 25% off', '1 Year Warranty on Product and 5 years on Compressor', '3 Star'),
('3.', 'Voltas 1.5 Ton Window AC', '28490', '34690 - 17% off','1 Year Warranty on Product and 5 years on Compressor', '5 Star'),
('4.', 'SAMSUNG 1 Ton Split Inverter AC', '26990', '42990 - 37% off', '1 Year Warranty on Product and 10 years on Compressor', '3 Star'),
('5.', 'Blue Star 1.2 Ton Split Inverter AC', '29490', '50000 - 41% off', '1 Year Warranty on Product and 10 years on Compressor', '3 Star'),
('6.', 'Whirlpool 1.5 Ton Split Inverter AC', '33990', '64400 - 47% off', '1 Year Warranty on Product and 10 years on Compressor', '5 Star'),
('7.', 'CARRIER 4 in 1 Convertible Cooling 1.5 Ton Split Inverter AC', '39990', '61990 - 35% off', '1 Year Warranty on Product and 10 years on Compressor', '5 Star');
create table chimneys (
SrNo int PRIMARY KEY,
Model varchar(255),
Sale_Price int,
MRP varchar(255),
Warranty varchar(255),
Suction_Capacity varchar(255));
insert into chimneys values
('1.', 'Greenchef Akeno 60cm Wall Mounted Chimney', '4599', '11990 - 61% off', '1 Year Warranty on Product and 5 Years Warranty on Motor', '650 CMH'),
('2.', 'Hindware Clarissa 60cm Wall Mounted Chimney', '5899', '11990 - 50% off', '1 Year Warranty on Product and 5 Years Warranty on Motor', '700 CMH'),
('3.', 'Faber Hood Mercury 60cm Auto Clean Wall Mounted Chimney', '9990', '22990 - 56% off','1 Year Warranty on Product and 5 Years Warranty on Motor', '1200 CMH'),
('4.', 'Elica WDFL NERO 90cm Auto Clean Wall Mounted Chimney', '11999', '26990 - 55% off', '1 Year Warranty on Product and 5 Years Warranty on Motor', '1200 CMH');
create table refrigerators (
SrNo int PRIMARY KEY,
Model varchar(255),
Sale_Price int,
MRP varchar(255),
Warranty varchar(255),
Star_Rating varchar(255));
insert into refrigerators values
('1.', 'SAMSUNG 192 L Direct Cool Single Door Refrigerator', '12790', '14990 - 14% off', '1 Year Warranty on Product and 10 years on Compressor', '2 Star'),
('2.', 'Whirlpool 190 L Direct Cool Single Door Refrigerator', '14490', '19500 - 25% off', '1 Year Warranty on Product and 10 years on Compressor', '3 Star'),
('3.', 'SAMSUNG 198 L Direct Cool Single Door Refrigerator', '16350', '19990 - 18% off','1 Year Warranty on Product and 10 years on Compressor', '4 Star'),
('4.', 'SAMSUNG 225 L Direct Cool Single Door Refrigerator', '19690', '22990 - 14% off', '1 Year Warranty on Product and 10 years on Compressor', '4 Star'),
('5.', 'SAMSUNG 253 L Frost Free Double Door Convertible Refrigerator', '25590', '31990 - 20% off', '1 Year Warranty on Product and 10 years on Compressor', '3 Star');
'''
s=s.replace('\n','')
l= s.split(';')
l.pop()
for i in l:
    c.execute(i)
db.commit()
print("Database Created Successfully!!")
