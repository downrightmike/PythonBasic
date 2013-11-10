print("Welcome to the decision maker!")

g = input("How much gas do you have")

fuel = int(g)

h = input("How much cash do you have?")

money = int(h)


if fuel > 3:
        print("It's OK!")

        print("You can Drive downtown!")

else:
    if money > 10:
        print("You should buy some gas!")

    else:
        print ("You had better stay at home!")
print("What's next?!")
        
