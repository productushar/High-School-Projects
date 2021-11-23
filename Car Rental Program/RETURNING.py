#This file contains functions for when Option B: Return a Vehicle is chosen in the main program

def return_car():

#Connecting to Database
    
    import mysql.connector
    conobj=mysql.connector.connect(host="localhost", user="root", passwd="XXXXXXXXX")
    cur=conobj.cursor()

#Searching for the record with the specific vehicle to be returned
    
    cur.execute("use car_rental")
    cust_name=input("\n\tEnter Your Name")
    cust_phone=input("\n\tEnter Phone Number")
    initial_date=input("\n\tEnter Initial lease date in YYYY-MM-DD format")
    km=int(input("\n\tEnter total number of Kilometers driven"))
    add_days=int(input("\n\tEnter number of Additional days"))
    cur.execute("select * from cars_lease")
    result=cur.fetchall()
    bcost=0
    acost=0

#Procedure for when the record is found (Finances)

    for i in result:
        if (cust_name==i[0] and cust_phone==i[1] and initial_date==str(i[2])):
            print("\n\tRecords Found")
            days=i[3]+add_days
            kmday=km/days
            ekms=0
            if kmday>i[7]:
                ekms=days*(kmday-i[7])
                acost+=ekms*(i[8])
            acost+=add_days*(i[6])
            bcost+=(i[3])*(i[6])
            print("\n\tNo. of Days=",i[3])
            print("\n\tExtra Days=",add_days)
            print("\n\tKm Limit/Day=",i[7])
            print("\n\tNet Kms/Day=",kmday)
            print("\n\tExtra kms=",ekms)
            print("\n\tRate for Extra KMs=",i[8])
            print("\n\tYour base cost is AED",bcost)
            print("\n\tYour additional cost is AED",acost)
            print("\n\tYour total cost is AED",acost+bcost)
            confirm=input("\n\tDo you want to confirm return of car")
            if confirm.upper()=="YES":
                print("\n\tPlease pay AED",acost+bcost,"at the counter")
                cur.execute("delete from cars_lease where cust_name= %s and cust_no= %s ",(cust_name, cust_phone))
                cur.execute("update customer_details set Status='Returned'")
                print("\n\tCar Returned")
                conobj.commit()
                break
        else:
            print("\n\tNot Found")
            
        
