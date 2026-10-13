# Q3: Guessing game

LUCKY_NUMBER = 7
MAX_ATTEMPTS = 3
WINNERS_FILE = r"C:\Users\ngiog\Desktop\Moringa School\Lab Works\Python_Functions\winners.txt"

name = input("Enter your name: ")
won = False

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input("Guess the lucky number: "))

    if guess == LUCKY_NUMBER:
        print(f"Congrats {name}! You won the game")
        won = True
        break
    else:
        if attempt < MAX_ATTEMPTS:
            print(f"Attempt {attempt}: No luck, try again")
        else:
            print(f"Attempt {attempt}: No luck, try again")
            print("Oops! You're out of luck")

# Record the winner (only if not already recorded)
if won:
    try:
        with open(WINNERS_FILE, "r") as file:
            winners = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        winners = []

    if name not in winners:
        with open(WINNERS_FILE, "a") as file:
            file.write(name + "\n")