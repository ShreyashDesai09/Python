from random import *

name = input("ENTER NAME:")
print(f"HELLO {name} WELCOME TO GUESS THE NUMBER GAME")

secrete_num = randint(1,10)
print("I HAVE GUESSED A NAME \nNOW YOU TRY TO GUESS IT CORRECT........")

for guess_num in range (1,6):
    print("Take A Guess:")
    guess = int(input())
    if guess < secrete_num:
        print("Too Low")
        print(f"{guess_num}'s Guesses")
    elif guess == secrete_num:
        print("Too High")
        print(f"{guess_num}'s Guesses")
    # elif guess == secrete_num - 1 or guess == secrete_num + 1:
    #     print("TOOOOOOO CLOSE")
    #     print(f"{guess_num}'s Guesses")
    else:
        break
if guess == secrete_num:
    print("GAME OVER")
else:
    print("HOORAYYYY!!!!! \n VICTORY")

