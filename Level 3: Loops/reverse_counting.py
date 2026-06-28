# print Reverse counting
print ("(#PRINT NUMBER IN DESCENDING ORDER THROUGH THE USE OF WHILE / FOR ) ")

print ("___________________________________________________________________")

print ("1. While loop OR 2. For loop")

print ("")

x = int (input ("Enter Selected value:"))

print ("")

if x == 1:

    print ("<----------WHILE LOOP PROGRAM----------->" )

    print ("")

    n= int (input("Enter value:"))
    i = 1
    while n >= i:
        print (n)
        n -= 1

elif x == 2:

    print ("<----------FOR LOOP PROGRAM----------->")

    print ("")

    n= int (input("Enter value:"))

    for i in range (n,0,-1): 

        print (i)
else:

    print ("Invalid Selection")

    print ("_________________")
