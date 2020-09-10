import math
print(" ********************* WELCOME TO PYTHON CALCULATOR ************************************")
print(" ")
print("PlEASE ENTER YOUR SELECTION")
print("** ADDITION --> 1 ** \n** SUBTRACTION --> 2 ** \n** MULTIPLICATION --> 3 ** \n** DIVISION --> 4 ** \n** POWER --> 5 ** \n** ROOT --> 6 ** ")
print(" ")
Select=input("Enter your Selection")
while Select!="Q":
 if Select == "1":
     print("ADDITION")
     first=int(input("Enter the First Number"))
     second = int(input("Enter the Second Number"))
     print("ADDITION OF ",first ,"+",second,":",first+second)
     print(" ")
     Select=input("Please Enter your Next SELECTION")
 if Select == "2":
     print("SUBTRACTION")
     first = int(input("Enter the First Number"))
     second = int(input("Enter the Second Number"))
     print("SUBTRACTION OF ",first ,"-",second,":",first- second)
     print(" ")
     Select = input("Please Enter your Next SELECTION")
 if Select == "3":
     print("DIVISION")
     first = int(input("Enter the First Number"))
     second = int(input("Enter the Second Number"))
     print("DIVISION OF ",first ,"/",second,":",first / second)
     print(" ")
     Select = input("Please Enter your Next SELECTION")
 if Select == "4":
     print("MULTIPLICATION")
     first = int(input("Enter the First Number"))
     second = int(input("Enter the Second Number"))
     print("MULTIPLICATION OF ",first ,"*",second,":",first * second)
     print(" ")
     Select = input("Please Enter your Next SELECTION")
 if Select == "5":
     print("SQAURE")
     first = int(input("Enter the First Number"))
     second = int(input("Enter the Second Number"))
     print(" SQAURE IS ",pow(first,second))
     print(" ")
     Select = input("Please Enter your Next SELECTION")
 if Select == "6":
     print("ROOT")
     first = int(input("Enter the Number for square root"))
     print("SQUARE ROOT OF",first,": ",math.sqrt(first))
     print(" ")
     Select = input("Please Enter your Next SELECTION")
 else:
     print("YOU HAVE GIVEN WRONG CHOICE")
     print(" !!!!!!! Please Try Again !!!!!!!")
     Select = input("Please Enter your Next SELECTION")

