import random
while True :
    user_action = input ("your choice rock, paper, scissors ?")
    possible_actions = ["rock", "paper", "scissors"]
    robot = random.choice(possible_actions)
    print (f"\n you chose {user_action}, robot chose {robot}.\n")
    if user_action == robot :
        print (f"both players selected {user_action}. it's a tie!")
    elif user_action == "rock" :
        if robot == 'paper' :
            print ("paper covers rock! you lose.")
        else :
                print ("rock smashes scissors! you win!")
    elif user_action == "paper" :
        if robot == 'scissors' :
            print ("scissors cuts paper! you lose.")
        else :
            print ("paper covers rock! you win!")
    elif user_action == "scissors" :
        if robot == 'rock' :
            print ("rock smashes scissors! you lose.")
        else :
            print ("scissors cuts paper! you win!")
    play_again = input ("play again ? (y/n) : ")
    if play_again == "no" or play_again == "n" :
        break
