#Vending Machine
#Jace Kim
#UCC
x = True
print("Options: ")
print("1. Cookies - $1.75")
print("2. Coke - $2.00")
print("3. Sprite - $2.00")
print("4. Ginger Ale - $2.00")
print("5. Cheetos - $1.50")
print("6. Fruit by the Foot - $1.25")

payment = int(input("How much money are you inputting? \n"))

change = (payment)
while x == True:

	choice = int(input("What do you want to purchase? \n"))

	if choice == 1:
		change = change - 1.75
		print("You have got cookies and $" + str(change) + " of change.")
	elif choice == 2:
		change = change - 2
		print ("You have got a Coke and $" + str(change) + " of change.")
	elif choice == 3:
		change = change - 2
		print ("You have got a Sprite and $" + str(change) + " of change.")
	elif choice == 4:
		change = change - 2
		print("You have got a Ginger Ale and $" + str(change) + " of change.")
	elif choice == 5:
		change = change - 1.5
		print ("You have got a bag of Cheetos and $" + str(change) + " of change.")
	elif choice == 6:
		change = change - 1.25
		print ("You have got a Fruit by the Foot and $" + str(change) + " of change.")
	else:
		print ("This is not a valid choice")

	if change < 2.5: 
		print("You do not have sufficient funds anymore. Please come back with more money.")
		x = False
