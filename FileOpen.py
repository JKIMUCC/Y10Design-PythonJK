print ("This program will open a file and read information from it")

# When we open the file we can read one character at a time
# including the newline character "\n"

f = open("textfile.txt", "r")

print(f.read(7))
print ("")

# Another way is to simply read the whole file...
f = open("textfile.txt", "r")
print(f.read())

# This is a way to gracefully exit the program
input("Press ENTER to quit the program")