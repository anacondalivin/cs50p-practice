import random

def main():
    number = random.randint(1, 100)
    guess = 0
    attempt = 0
    while guess != number:
        guess = int(input("Pick a number between 1 and 100 "))
        attempt += 1
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
    print(f"You got it in {attempt} attempts!")
main()
