#Sartaj Gill
#Problem1
print("Problem 1")
string = "25"
print(string)
converted = int(string) #converts string to integer value
print(converted + 12)
#Problem 2
print("Problem 2")
string = "13.68"
print(string)
converted1 = float(string) #converts string to float value
print(converted1 + 16.23)
#Problem 3
print("Problem 3")
string1 = "13"
integer1 = 12
print(string1 + str(integer1)) #str converts our int value into a string 
#Problem 4
print("Problem 4")
a = input("Please enter the first number you want multiplied?")
one = int(a) #converts string to integer
b = input("Please enter the second number you want multiplied?")
two = int(b)
c = one * two #multiplies the two integers 
print("The product of ", one, " and ", two, " is ",float(c)) #prints out statement and turns the answer into a float
#Problem 5
print("Problem 5")
string1 = "Hello my name is Sartaj Gill"
print(string1.find("is")) #.find("") allows us to return the index of the first occurance of the substring