cost =[15.00, 12.50 , 3.75, 40.25, 6.99]
total_cost = 0
for counter in range(0, 21, 2): # this is a for loop that will loop from 1 to 10
    print(counter)   
for price in cost :
    print (price)
    total_cost= total_cost + price
print(f"Total cost is: {total_cost}")

for col in range(3): # this is a loop createing column by column
    for row in range (5): # this is a nested loop creating each row
        print("*", end=" ")
    print()


for col in range (5): # creates each column
    for row in range (col): # creates each row depending on which column it is intrated into
        print ("*", end=" ")
    print()

choice = None   #creates an epty variable
while choice != "q":  #creates a while loop that will continue until the user enters q
    print(" 1. Add")
    print(" 2. Subtract")
    print("q. Quit")
    choice = input("Choose an option: ") #asks the user to enter a choice
    if choice == "1":
        number1 = int(input("Enter first number: ")) 
        number2 = int(input("Enter second number: "))
        print(f"The sum is: {number1 + number2}") #prints the sum of the two numbers
    elif choice == "2":
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print(f"The difference is: {number1 - number2}")
    elif choice == "q": #if the user enters q, the loop will end
        print("Goodbye!") #prints goodbye message


