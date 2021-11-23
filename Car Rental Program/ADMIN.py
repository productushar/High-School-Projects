#This is a secret menu option for the ADMIN to check out cars on lease, customer details, and also for updating records manually

def Admin():

#Connecting to database
    
    import mysql.connector
    conobj=mysql.connector.connect(host="localhost", user="root", passwd="XXXXXXXXX")
    cur=conobj.cursor()
    cur.execute("use car_rental")

#Options-Menu for ADMIN
    
    print("\n\tA. Show Cars on lease")
    print("\n\tB. Show Customer Details")
    print("\n\tC. Update Records *Custom*\n")
    opt=input("Enter Option")
    if opt.upper()=="A":
        cur.execute("select * from cars_lease")
        result=cur.fetchall()
        if result==[]:
            print("\n\tNo Cars on Lease")
        else:
            for i in result:
                print("\n\t",i)
    elif opt.upper()=="B":
        cur.execute("select * from customer_details")
        for i in cur.fetchall():
            print("\n\t",i)
    elif opt.upper()=="C":
        print("\n\tTo discontinue type No")
        sql="Yes"
        while sql.upper()!="NO":
            sql=input("\n\tInput Sql Statement")
            if sql.upper()=="NO":
                break
            cur.execute(sql)
            for i in cur.fetchall():
                print("\n\t",i)
