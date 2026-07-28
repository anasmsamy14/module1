def game (self)
    print("Welcome to the game!") 
    print("You are in a dark room. There is a door to your left and right. Which one do you take?")

    choice = input("> ")      
    if choice == "left":
        print("You enter a room full of treasure! You win!")
    elif choice == "right":
        print("You enter a room full of monsters! You lose!")
    else:
        print("Invalid choice. You lose!")

if __name__ == "__main__":  game()      
