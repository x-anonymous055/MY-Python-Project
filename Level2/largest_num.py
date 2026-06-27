# Compare two numbers and display the larger one

print ("<--------Largest Number Finder-------->")

print ("___________________")

print ("")

num1 = int (input ("Enter 1st Number:"))

num2 = int (input("Enter 2nd Number:"))

print ("___________________")

print ("Comparing", "(",num1,")", "and", "(",num2,")")

print ("")

if num1 == num2:

    print ("Number is Equal")

elif num1 >= num2:

    print (num1, "is the largest")

else:

    print (num2," is the Largest")

print ("")

print ("(Thanks For Using)")
