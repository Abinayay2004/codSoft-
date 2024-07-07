import random

def main():
    print("**ROCK PAPER SCISSORS**")
    print("type 0 -> ROCK")
    print("type 1 -> PAPER")
    print("type 2 -> SCISSORS")

    user_choice = int(input("Enter your choice: "))

    if user_choice < 0 or user_choice > 2:
        print("YOU ENTERED AN INVALID NUMBER, YOU LOSE!!!")
        return

    choices = ["ROCK", "PAPER", "SCISSORS"]
    computer_choice = random.randint(0, 2)
    print(f"Computer's choice: {choices[computer_choice]}")
    print(f"Your choice: {choices[user_choice]}")

    if computer_choice == user_choice:
        print("IT IS A TIE, PLAY NEXT ROUND")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("YOU WIN!!! CONGRATULATIONS")
    else:
        print("YOU LOSE THE MATCH!!! BETTER LUCK NEXT TIME")

main()