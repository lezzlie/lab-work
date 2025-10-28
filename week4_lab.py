def celsius_to_farenheit(celsius): #function to convert celsius to fahrenheit
    fahrenheit = (celsius * 9/5) + 32 #calculate fahrenheit using the celsius value
    return fahrenheit



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
