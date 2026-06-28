# Print numbers from 1 to the user input value using a loop

print ("(PRINT VALUE THROUGH THE USE OF WHILE / FOR ) ")

print ("____________________________________________")

print ("1. While loop OR 2. For loop")

print ("")

x = int (input ("Enter Selected value:"))

if x == 1:

    print ("<----------WHILE LOOP PROGRAM----------->" )

    print ("")

    n= int (input("Enter value:"))
    i = 1
    while i <= n:
        print (i)
        i += 1
        
elif x == 2:

    print ("<----------FOR LOOP PROGRAM----------->")

    print ("")

    n= int (input("Enter value:"))

    for i in range (1,n): 

        print (i)
else:

    print ("Invalid Selection")

    print ("_________________")
