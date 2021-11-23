#Main File - Car Rental 

#Importing essential functions from other modules

from INITIALIZE import *
from ADMIN import *
from RENTING import *
from RETURNING import *

#Execution of Main Program

initialize()
ans="Yes"
while ans.upper()=='YES':
    print("\n\n\t\t\t\tWelcome to OUR CAR RENTAL COMPANY")
    print("\n\n\t\tA. Rent a vehicle")
    print("\n\t\tB. Return vehicle")
    ans2=input("\n\tEnter option")
    if ans2.upper()=="A":
        renting()
    elif ans2.upper()=="B":
        return_car()
    elif ans2.upper()=="ADMIN":
        Admin()
    else:
        print("\n\tInvalid Option")
    ans=input("\n\tEnter Yes to continue or any other key to stop")
