print("Welcome!")

g  = input("take a guess: ")

guess = int(g)

if guess == 5:

    print("yay you got it!")

else:

    if guess <= 4:
        
        print("Ouch! Too low!")

    else:
        if guess > 5:
        
            print("Too high, Sorry!")
        
    print("You lost!")

print("Game over!")
