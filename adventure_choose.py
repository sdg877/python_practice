name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer=input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type swim or cross: ")
    if answer == "swim":
        print("You swam across and were eaten by a crocodile. You lose.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You lose.")
    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross is or head back? Type cross or back: " )
    if answer == "cross":
        print("You cross the bridge and it breaks. You were eaten by a crocodile. You lose.")
    elif answer == "back":
        print("You go back to the main road and find some gold. You win.")

else:
    print("Not a valid option. You lose.")

