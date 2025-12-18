def shutdown(user_input):
    if user_input == "yes":
        print("Shutting down")
    elif user_input == "no":
        print("Abort shut down")
    else:
        print("Sorry.")


choice = input("Do you want to shut down the system? (Yes/No): ")
shutdown(choice)
