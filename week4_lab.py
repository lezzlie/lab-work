def celsius_to_farenheit(celsius): #function to convert celsius to fahrenheit
    fahrenheit = (celsius * 9/5) + 32 #calculate fahrenheit using the celsius value
    return fahrenheit

def  test_scope():
    my_variable = "I am local"
    print(my_variable)
    

secret_number = 245
while True:
    Guess = int(input("guess the number"))
    if Guess == secret_number:
        print("congratulations! you guessed it")
        break
    elif Guess < secret_number:
        print("too low, try again")
    else:
        print("too high, try again")
c_temp =25
f_temp = celsius_to_farenheit(c_temp)
print(f"{c_temp}C is equal to {f_temp}F ")

my_variable = "I am global"
test_scope() # calles the function and demonstraits that the variable being printed is comming from inside the function
print(my_variable) # prints the global variable outside the function

