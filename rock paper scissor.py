import random

print("Lets Play")
print(" Type 0 for Rock ")
print("Type 1 for Paper")
print("Type 2 for scissor")

while True:
    choice = input("choose (or Press 'x' to exit)")
    if choice.lower == 'x':
        print("Bye")
        break
    if not choice.isdigit() or int(choice) not in [0,1,2]:
        print("Invalid!")
        continue
    choice = int(choice)
    game =["Rock","Paper","Scissor"]
    computer=(random.randint(0,2))
    user_choice = game[choice]
    print(user_choice)

    computer= random.choice(game)
    print(computer)

    if user_choice == computer:
        print("Tie!")
    elif (user_choice == "Rock" and computer == "Scissor") or\
         (user_choice == "Paper" and computer == "Rock") or \
         (user_choice == "Scissor" and computer == "Paper"):
        print("Yay! You Win.")
    else:
        print("Computer Wins")

    print()
