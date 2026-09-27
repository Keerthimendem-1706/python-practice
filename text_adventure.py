print("==== TEXT ADVENTURE ====")
health =100
inventory = []
print("\nYou are inside a mysterious house.")
choice = input("Choose left or right: ").lower()
if choice == "left":
    print("\nYou found a key!")
    inventory.append("key")
    choice = input("Go left or right? ").lower()
    if choice == "right":
        print("\nYou found the locked door.")
        if "key" in inventory:
            print("You used the key and escaped!")
        else:
            print("\nThe door is locked.")
    else:
        print("\nYou found a treasure chest!")
        print("You win")
elif choice =="right":
    print("\nA trap was triggered!")
    health -= 30
    print("Health:",health)
    if health > 0:
        print("You escaped the trap!")
    else:
        print("Game Over!")
else:
    print("\nInvalid choice. Game Over!")
print("\nFinal Health:",health)
print("Inventory:",inventory)
