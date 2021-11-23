#Initial function run before the execution of the main program to verify the existence of the desired SQL database (which is also established incase the database doesn't exist)

def initialize():

    #Importing and connecting MySQL
    
    import mysql.connector
    conobj=mysql.connector.connect(host="localhost", user="root", passwd="XXXXXXXXX")
    cur=conobj.cursor()

    #Checking for the desired database's existence
    
    cur.execute("show databases")
    x=cur.fetchall()
    if ('car_rental',) in x:
        print("\n\t\t\t\t\t\t\t\t\tDATABASE EXISTS ALREADY")

    #Establishing the database incase it does not exist prior to running the main program
        
    elif ('car_rental',) not in x:
        cur.execute("create database car_rental")
        cur.execute("use car_rental")
        cur.execute("create table BOOK_A_CAR(SNo integer,Type_Of_Vehicle varchar(15))")
        cur.execute("insert into BOOK_A_CAR values(1,'Sedan')")
        cur.execute("insert into BOOK_A_CAR values(2,'SUV')")
        cur.execute("insert into BOOK_A_CAR values(3,'Sports Car')")
        cur.execute("insert into BOOK_A_CAR values(4,'Minibus')")
        cur.execute("use car_rental")
        cur.execute("create table SEDAN(SNo integer,Brand varchar(20),No_Of_Seats integer,Base_Cost_Per_Day integer,Km_Limit_Per_Day integer,Surplus_Cost_Per_Km integer,Model_Year integer,Car_IDNo char(8) primary key,Fuel_Economy varchar(15),Trunk_Space_Litres integer)")
        cur.execute("insert into SEDAN values(1,'Honda',5,75,100,2,2018,'RCS00001',18,450)")
        cur.execute("insert into SEDAN values(2,'BMW',4,150,60,4,2013,'RCS00002',7,400)")
        cur.execute("insert into SEDAN values(3,'Nissan',5,60,150,1,2009,'RCS00003',23,500)")
        cur.execute("insert into SEDAN values(4,'Mitsubishi',5,35,175,1,2007,'RCS00004',15,420)")
        cur.execute("insert into SEDAN values(5,'Toyota',4,50,120,3,2020,'RCS00005',20,600)")
        cur.execute("insert into SEDAN values(6,'Mercedes',4,250,25,5,2019,'RCS00006',6,300)")
        cur.execute("insert into SEDAN values(7,'Hyundai',5,80,250,1,2006,'RCS00007',25,250)")
        cur.execute("insert into SEDAN values(8,'Kia',4,65,300,3,2015,'RCS00008',20,150)")
        cur.execute("create table SUV(SNo integer,Brand varchar(20),No_Of_Seats integer,Base_Cost_Per_Day integer,Km_Limit_Per_Day integer,Surplus_Cost_Per_Km integer,Model_Year integer,Car_IDNo char(8) primary key,Fuel_Economy integer,Trunk_Space_Litres integer)")
        cur.execute("insert into SUV values(1,'Honda',7,200,300,4,2014,'RCSUV001',8,750)")
        cur.execute("insert into SUV values(2,'Ford',8,350,150,5,2016,'RCSUV002',12,600)")
        cur.execute("insert into SUV values(3,'Hummer',9,100,50,5,2012,'RCSUV003',6,900)")
        cur.execute("insert into SUV values(4,'Cadillac',8,250,60,4,2020,'RCSUV004',5,800)")
        cur.execute("insert into SUV values(5,'Toyota',8,175,40,2,2009,'RCSUV005',10,875)")
        cur.execute("insert into SUV values(6,'Nissan',9,400,75,3,2013,'RCSUV006',11,570)")
        cur.execute("insert into SUV values(7,'Lexus',9,275,80,2,2016,'RCSUV007',8,450)")
        cur.execute("insert into SUV values(8,'BMW',8,450,300,6,2020,'RCSUV008',9,325)")
        cur.execute("create table Sports_Car(SNo integer,Brand varchar(20),No_Of_Seats integer,Base_Cost_Per_Day integer,Km_Limit_Per_Day integer,Surplus_Cost_Per_Km integer,Model_Year integer,Car_IDNo char(8) primary key,Fuel_Economy integer,Trunk_Space_Litres integer)")
        cur.execute("insert into Sports_Car values(1,'Ferrari',2,1500,25,10,2012,'RCSUP001',3,100)")
        cur.execute("insert into Sports_Car values(2,'McLaren',3,2500,45,15,2014,'RCSUP002',2,75)")
        cur.execute("insert into Sports_Car values(3,'Koenigsegg',2,3000,30,12,2017,'RCSUP003',5,25)")
        cur.execute("insert into Sports_Car values(4,'Bugatti',2,4500,50,8,2009,'RCSUP004',6,40)")
        cur.execute("create table Minibus(SNo integer,Brand varchar(20),No_Of_Seats integer,Base_Cost_Per_Day integer,Km_Limit_Per_Day integer,Surplus_Cost_Per_Km integer,Model_Year integer,Car_IDNo char(8) primary key,Fuel_Economy integer,Trunk_Space_Litres integer)")
        cur.execute("insert into Minibus values(1,'Mitsubishi',20,100,300,1,2012,'RCBUS001',1,3000)")
        cur.execute("insert into Minibus values(2,'Ashok Leyland',35,150,400,2,2016,'RCBUS002',3,2500)")
        cur.execute("insert into Minibus values(3,'Volvo',15,250,500,3,2017,'RCBUS003',2,4250)")
        cur.execute("insert into Minibus values(4,'Toyota',18,120,375,1,2010,'RCBUS004',1,4000)")
        cur.execute("create table Contact_Us(SNo integer,Type_of_Service varchar(20))")
        cur.execute("insert into Contact_Us values(1,'Feedback')")
        cur.execute("insert into Contact_Us values(2,'Enquiry')")
        cur.execute("insert into Contact_Us values(3,'Complaint')")
        cur.execute("insert into Contact_Us values(4,'+971568022811')")
        cur.execute("create table Cars_Lease(Cust_Name varchar(25),Cust_No varchar(15),Initial_Date_of_Rent date,No_of_days integer,Brand varchar(20),No_Of_Seats integer,Base_Cost_Per_Day integer,Km_Limit_Per_Day integer,Surplus_Cost_Per_Km integer,Model_Year integer,Car_IDNo varchar(8),Fuel_Economy integer,Trunk_Space_Litres integer)")
        cur.execute("create table Customer_Details(Cust_Name varchar(25),Cust_PhoneNo varchar(15),Initial_Date_Of_Rent date,No_of_days integer,Car_IDNo char(8),Status varchar(10))")
        conobj.commit()
        print("\n\t\t\t\t\t\t\t\t\t\tDATABASE CREATED")

