def make_smoothie():
    juice = input("What juice would you like? ")
    fruit = input("What fruit would you like? ")
    print("Thanks!")
    print("Crushing it!")
    print("blending the  " + fruit)
    print("now adding the " + juice + " juice")
    print("Finished! Here's your " + fruit + " and " + juice + " smoothie!")
    
print("Welcome to the Smoothie-matic!")
another = "Y"
while another == "Y":
    make_smoothie()
    another = input("Would you like another? (Y/N)")