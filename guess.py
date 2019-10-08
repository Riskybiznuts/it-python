import random

print("================")
print("GUESS MY NUMBER")
print("================")
print("")
name = input("What is your name?")
the_number = random.randint(0,100)

print("")
print("I'm thinking of an integer between 0 and 100. Can you guess it?")

guess = 101

while guess != the_number:
    guess_text = input("What is your guess?")
    guess = int(guess_text)

    if guess < the_number:
        print(f"sorry, {name}, but your guess is too LOW")
    elif guess > the_number:
        print(f"sorry, {name}, but your guess is too HIGH")
    else:
        print(f"You guessed it! Congatulations, {name}!")



print("Thanks for playing!")