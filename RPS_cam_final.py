keep_going = ""
while keep_going == "":
    print("welcome to paper scissors rock, where you put in paper, scissors or rock to see if you win")

    choice = input("your choice:")
    print("scissors is my choice")

    print(f" {choice} is your choice\n")
    print("rock beats scissors, rock loses to paper rock, ties against rock ")
    print("scissors beats paper, scissors loses to rock, scissors ties against scissors ")
    print("paper beats rock, paper loses to scissors, paper ties against paper ")
    print()
    print(
        f"you might have won, or lost, or tied, or you might have put in something completely random. in that case, "
        f"i dont know if you won or not\n")
    keep_going = input("Press enter to play again or any key to quit")
    print()
    print("thank you for playing")

    # add that thing that makes you only able to put paper scissors or rock or not I don't care