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


for col in range (5):
    for row in range (col):
        print ("*", end=" ")
    print() 