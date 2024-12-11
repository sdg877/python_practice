menu = {"cola": 1.75,
        "hot dog": 2.75,
        "malteasers": 2.25,
        "popcorn": 6.99,
        "nachos": 4.50,
        "fries": 2.99,
        "haribo": 3.15,
        "combo": 12.99
        }

cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: £{value:.2f}")
print("--------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Total is £{total:.2f}")
