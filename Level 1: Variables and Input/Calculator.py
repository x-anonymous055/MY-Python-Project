# Basic Calculator 
print ("What do you want to calculate?")
print ("1.Addition")
print ("2.subtraction")
print ("3.Multiplication")
print ("4.Division")
n = int(input ("Select value:"))
if 1 == n:
    print ("Addition" )
    a = int (input ("Enter 1st value:"))
    b = int (input ("Enter 2nd value:"))
    sum= a + b
    print ("Final Answer", sum)
    print ("Thanks for using")
elif 2 == n:
    print ("Subtraction")
    a = int (input ("Enter 1st value:"))
    b = int (input ("Enter 2nd value:"))
    sub = a - b
    print ("Final Answer", sub)
    print ("Thanks for using")
elif 3 == n:
    print ("Multiplication")
    a = int (input ("Enter 1st value:"))
    b = int (input ("Enter 2nd value:"))
    mul= a * b
    print ("Final Answer",mul)
    print ("Thanks for using")
elif 4 == n:
    print ("Division")
    a = int (input ("Enter 1st value:"))
    b = int (input ("Enter 2nd value:"))
    div= a + b
    print ("Final Answer", div)
    print ("Thanks for using")
else: 
    print ("Invalid Selection")
