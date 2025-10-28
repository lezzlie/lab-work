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

