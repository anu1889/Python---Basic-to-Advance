import random


def guess_number():
    random_number = random.randint(1,100)
    print("Welcome to Number Guessing Game.")
    print("I am thinking of number between 1 to 100. Can you guess it?")

    attempts = 0

    while True:
        guess = int(input("\n Enter your guess: "))

        attempts += 1
        
        if guess < random_number:
            print("Too Low! Try Again.")
        elif guess > random_number:
            print("Too High! Try Again.")
        else:
            print(f"Congrats! You guessed the number {random_number} correctly!")
            break


if __name__ == "__main__":
    guess_number()            
