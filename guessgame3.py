print("Welcome Hobbits!")

guess = 0

while guess != 3:

    g = input("How many Breakfasts do you need?")

    guess = int(g)

    if guess == 3:

        print("You win! Now eat this Bacon!")

    else:
        if guess > 3:

            print("Too many Breakfasts! Save some room for Lunch!")

        else:

            print("Too few! You can stomach more than that!")

print("Game over!")
