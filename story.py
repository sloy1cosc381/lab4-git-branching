def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You try to pull the sword out, but instead take the whole thing out of the ground.")
    print("This sword-in-stone is more like a hammer now, but you wield it valiently none the less.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    
def center_path():
    print("You walk down the center and into a clearing with a pond. Something glitters at the bottom.")

if __name__ == "__main__":
    intro()
