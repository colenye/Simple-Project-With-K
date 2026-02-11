import random

while True:
    user_action = input('Enter your choice (rock, paper, or scissors):')
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possible_actions)

    print("You chose " + user_action + ", computer chose " + computer_action)

    if user_action == computer_action:
        print("Both players selected " + user_action + ". It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("You lose.")
        else:
            print("You win!")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("You lose.")
        else:
            print("You win!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
        else:
            print("You lose.")

    play_again = input("Do you want to play again (yes/no): ")
    if play_again == "no":
        break

