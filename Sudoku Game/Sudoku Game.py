#Importing random so that random values can be generated for the sudoku

import random
print("\n\n                      Welcome to my Sudoku Code")

#Forming a 9x9 matrix with dots only - Values to be filled

l=[[0 for a in range(9)]for b in range(9)]
for a in range(9):
    for b in range(9):
        l[a][b]="."
        
#This list will be further used to ensure that the numbers set by the program cannot be changed
        
lst=[]

#We are inputting 81 values at random first out of which roughly 25-30 should make it to the final sudoku depending on the random values

v=81

#Inputting values randomly

while v!=0:
    a=int(random.randint(0,8))
    b=int(random.randint(0,8))
    c=int(random.randint(1,9))
    l[a][b]=c

#This part of the code ensures that a number is not repeated twice in a row or a column - If so, it is replaced by a dot
    
    for u in range(9):
        if l[a][b]==l[a][u] and u!=b:
            l[a][u]="."
        elif l[a][b]==l[u][b] and u!=a:
            l[u][b]="."
            
#This part ensures that none of the 9 numbers are repeated in any of the 9 3x3 matrix's in the 9x9 matrix
            
        elif a+b<=4 and a<=2 and b<=2:
            for o in range(3):
                for p in range(3):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=7 and a<=2 and 2<b<=5:
            for o in range(3):
                for p in range(3,6):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=10 and a<=2 and 5<b<=8:
            for o in range(3):
                for p in range(6,9):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=7 and 2<a<=5 and b<=2:
            for o in range(3,6):
                for p in range(3):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=10 and 2<a<=5 and 2<b<=5:
            for o in range(3,6):
                for p in range(3,6):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=13 and 2<a<=5 and 5<b<=8:
            for o in range(3,6):
                for p in range(6,9):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=10 and 5<a<=8 and b<=2:
            for o in range(6,9):
                for p in range(3):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=13 and 5<a<=8 and 2<b<=5:
            for o in range(6,9):
                for p in range(3,6):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
        elif a+b<=16 and 5<a<=8 and 5<b<=8:
            for o in range(6,9):
                for p in range(6,9):
                    if l[a][b]==l[o][p] and (a!=o or b!=p):
                        l[o][p]="."
    v-=1
    
#Now the indexes of the final values of the sudoku are being inputted into a list so that later on it can be used to make sure that system generated numbers cannot be replaced

for a in range(9):
    for b in range(9):
        if l[a][b]!=".":
            lst.append((10*a)+b)
            
#Now the sudoku will be printed
            
for a in range(9):
    print(" ")
    print("------------------------------------------------------------------------")
    for b in range(9):
        if b==0:
            print("  ",l[a][b],end="   ")
        else:
            print(" | ",l[a][b],end="   ")
print("\n------------------------------------------------------------------------")
print("\n\n")

#Now the user will replace the dots with numbers for an unlimited amount of times until the code is perfect

print("Now put in your values for the dots!")
z="Y"
while z!="N":
    w=int(input("\n\nEnter row number"))
    x=int(input("Enter column number"))
    y=int(input("Enter value to be entered"))
    if (10*(w-1))+(x-1) in lst:
        print("False input - You cant change this value")
        z=input("Enter N to stop or any other key to continue")
    elif y>9 or y==0 or w==0 or w>9 or x==0 or x>9:
        print("One of the values entered cannot be inputted - False input")
        z=input("Enter N to stop or any other key to continue")
    else:
        l[w-1][x-1]=y
        for a in range(9):
            print(" ")
            print("------------------------------------------------------------------------")
            for b in range(9):
                if b==0:
                    print("  ",l[a][b],end="   ")
                else:
                    print(" | ",l[a][b],end="   ")
        print("\n------------------------------------------------------------------------")
        z=input("\n\nEnter N to stop or any other key to continue")
print("\n")

#This part of the code is to check for victory

g=0
h=1
for a in range(9):
    for b in range(9):
        if l[a][b]==".":
            h=0
            break
        break
    break
if h==1:
    for u in range(9):
        if a+b<=4 and a<=2 and b<=2:
            for o in range(3):
                for p in range(3):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=1
        elif a+b<=7 and a<=2 and 2<b<=5:
            for o in range(3):
                for p in range(3,6):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=2
        elif a+b<=10 and a<=2 and 5<b<=8:
            for o in range(3):
                for p in range(6,9):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=3
        elif a+b<=7 and 2<a<=5 and b<=2:
            for o in range(3,6):
                for p in range(3):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=4
        elif a+b<=10 and 2<a<=5 and 2<b<=5:
            for o in range(3,6):
                for p in range(3,6):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=5
        elif a+b<=13 and 2<a<=5 and 5<b<=8:
            for o in range(3,6):
                for p in range(6,9):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=6
        elif a+b<=10 and 5<a<=8 and b<=2:
            for o in range(6,9):
                for p in range(3):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=7
        elif a+b<=13 and 5<a<=8 and 2<b<=5:
            for o in range(6,9):
                for p in range(3,6):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=8
        elif a+b<=16 and 5<a<=8 and 5<b<=8:
            for o in range(6,9):
                for p in range(6,9):
                    if l[a][b]!=l[o][p] and (a!=o or b!=p):
                        g=9
if g==9:
    print("Congrats - You've got it right!")
else:
    print("Ehem failed..")
            
