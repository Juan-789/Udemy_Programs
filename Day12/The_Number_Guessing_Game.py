import random as r
def numberToBeGuessed():
    return r.randint(1,100)
actualNum = numberToBeGuessed()
def start_difficulty():
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
    if difficulty =="easy":
        return 10
    elif difficulty =="hard":
        return 5
guessesLeft = start_difficulty()
while guessesLeft>0:
    print(f"You have {guessesLeft} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > actualNum:
        print("Too high.")
    elif guess < actualNum:
        print("Too low.")
    elif guess == actualNum:
        print(f"You got it! The answer was {actualNum}.")
        break
    guessesLeft-=1

if guessesLeft<0:
    print("You've ran out of guesses, you lose.")
