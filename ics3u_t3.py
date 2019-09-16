# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...


print("1. Weather")
print("2. Time")
print("3. Schedule \n")
print(" Choose one \n")


mood = int(input("What do you want to know? \n"))

if mood == 1:
    print("Cloudy")
elif mood == 2:
    print ("9:23:46 AM")
elif mood == 3:
    print ("CODING, PHYSICS, PHYS ED, ENGLISH")
else:
    print ("This is not a valid choice")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")
