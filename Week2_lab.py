"""
This program calculates the area of a rectangle and prints the results
"""
temp_celsius = int(input(f"please enter teperature in celseus: ")) #this represents the temporature in degrees celsius
temp_Fahrenheit = ((temp_celsius * 9/5)+32) # this line converts the temperature from celsius to fahrenheit
print(f"{temp_celsius} degrees celsius is equal to {temp_Fahrenheit} degrees fahrenheit")




string =  "hello" #initialising different data types
integer = 5
float=3.5
boolean = True
print(f"{string} is a data type called a string, ") #prints the data type of the variable and tells you what it is
print(f"{integer} is a data type called an integer, ")
print(f"{float} is a data type called a float, ")
print(f"{boolean} is a data type called a boolean. ")
print(type(string)) #uses the type function to print the data type of each variable
print(type(integer))
print(type(float))
print(type(boolean))

