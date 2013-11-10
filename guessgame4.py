from random import randint

secret = randint(1,10)

print("Welcome my precious.....")

guess = 0
while guess != secret:
    g = input("Give us a number love: ")

    guess = int(g)
    if guess == secret:
        print("the precious is yours...")

    else:
        if guess > secret:
            print("Too high! My precious...")

        else:
            print("Too low, My precious is priceless")

print("Game over!")
