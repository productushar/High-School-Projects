#This file contains the functions used when option A: Renting A Vehicle is chosen in the main program

#This function connects to data from the MySQL database to allow the user to choose a vehicle

def renting():
    x=('SNo','Brand','Seats','BCost/D' ,'KmLimit/D','ACost/Km' ,'Year','IDNo','Eco','Trunk')
    import mysql.connector
    conobj=mysql.connector.connect(host="localhost", user="root", passwd="XXXXXXXXX")
    cur=conobj.cursor()
    cur.execute("use car_rental")
    print("\n\tWhich type of car do you want to rent? Select option A-D")
    print("\n\t\tA. Sedan")
    print("\n\t\tB. SUV")
    print("\n\t\tC. Sports Car")
    print("\n\t\tD. Mini Bus")
    typeofcar=input("\n\tSelect option from A-D")

#Sedan

    if typeofcar.upper()=="A":
        print("\n\tSelected: Sedan")
        seats=int(input("\n\tEnter number of seats (4-5)"))
        if seats>5:
            print("\n\tNot Available")
            return
        cur.execute("select * from sedan")
        result=cur.fetchall()
        print("\n\tAvailable Cars Are")
        print("\n\t",x)
        for i in range(len(result)):
            if result[i][2]>=seats:
                print("\n\t",result[i])
        choice=int(input("\n\tEnter choice"))
        print("\n\tCar Details")
        print("\n\t",result[choice-1])
        confirmation=input("\n\tDo you want to confirm? Yes/No")
        if confirmation.upper()=="YES":
            print("\n\tConfirmed - Please fill out your details")
        else:
            return

#SUV
        
    if typeofcar.upper()=='B':
        print("\n\tSelected: SUV")
        seats=int(input("\n\tEnter Number of Seats(7-9)"))
        if seats>9:
            print("\n\tNot Available")
            return
        cur.execute("select * from SUV")
        result=cur.fetchall()
        print("\n\tAvailable Cars Are")
        print("\n\t",x)
        for i in range(len(result)):
            if result[i][2]>=seats:
                print("\n\t",result[i])
        choice=int(input("\n\tEnter choice"))
        print("\n\tCar Details")
        print("\n\t",result[choice-1])
        confirmation=input("\n\tDo you want to confirm? Yes/No")
        if confirmation.upper()=="YES":
            print("\n\tConfirmed - Please fill out your details")
        else:
            return

#Sports Car
        
    if typeofcar.upper()=="C":
        print("\n\tSelected: Sports Car")
        seats=int(input("\n\tEnter number of Seats(2-3)"))
        if seats>3:
            print("\n\tNot Available")
            return
        cur.execute("select * from sports_car")
        result=cur.fetchall()
        print("\n\tAvailable Cars Are")
        print("\n\t",x)
        for i in range(len(result)):
            if result[i][2]>=seats:
                print("\n\t",result[i])
        choice=int(input("\n\tEnter choice"))
        print("\n\tCar Details")
        print("\n\t",result[choice-1])
        confirmation=input("\n\tDo you want to confirm? Yes/No")
        if confirmation.upper()=="YES":
            print("\n\tConfirmed - Please fill out your details")
        else:
            return

#Mini Bus
        
    if typeofcar.upper()=="D":
        print("\n\tSelected: Mini Bus")
        seats=int(input("\n\tEnter number of seats(15-35)"))
        if seats>35:
            print("\n\tNot Available")
            return
        cur.execute("select * from minibus")
        result=cur.fetchall()
        print("\n\tAvailable Cars Are")
        print("\n\t",x)
        for i in range(len(result)):
            if result[i][2]>=seats:
                print("\n\t",result[i])
        choice=int(input("\n\tEnter choice"))
        print("\n\tCar Details")
        print("\n\t",result[choice-1])
        confirmation=input("\n\tDo you want to confirm? Yes/No")
        if confirmation.upper()=="YES":
            print("\n\tConfirmed - Please fill out your details")
    car_details=result[choice-1]
    Cust_details=customer_details(car_details)
    print("\n\tCar Details:",car_details,"\n\tCust Details:",Cust_details)
    car_lease(car_details,Cust_details)

#This function is to update a customer's detail as and when he/she chooses to rent out a vehicle
    
def customer_details(car_details):
    import mysql.connector
    conobj=mysql.connector.connect(host="localhost", user="root", passwd="XXXXXXXXX")
    cur=conobj.cursor()
    cur.execute("use car_rental")
    Name=input("\n\tEnter Your Name")
    Phone=input("\n\tEnter You Phone Number")
    initialdate=input("\n\tEnter initial date in YYYY-MM-DD format")
    No_of_days=int(input("\n\tEnter number of days for renting the car"))
    cur.execute("insert into Customer_Details values(%s,%s,%s,%s,%s,'On lease')",(Name,Phone,initialdate,No_of_days,car_details[7]))
    conobj.commit()
    print("\n\tRecords updated")
    cur.execute("select * from Customer_details where cust_name= %s and car_idno= %s",(Name,car_details[7]))
    return cur.fetchone()

#This function is to update the database with details for the car on lease

def car_lease(car_details,cust_details):
    import mysql.connector
    conobj=mysql.connector.connect(host="localhost", user="root", passwd="XXXXXXXXX")
    cur=conobj.cursor()
    cur.execute("use car_rental")
    cur.execute("insert into cars_lease values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cust_details[0], cust_details[1], cust_details[2], cust_details[3], car_details[1], car_details[2], car_details[3], car_details[4], car_details[5], car_details[6], car_details[7], car_details[8], car_details[9]))
    conobj.commit()
