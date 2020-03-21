import os

from random import randint

just_price = randint(1, 1000)

user_price = 0

while user_price != just_price:

    user_price = int(input("Entrez un nombre : "))

    if user_price < just_price:
        print("C'est plus grand!")

    elif user_price > just_price:
        print("C'est plus petit!")

    else:
        print("C'est gagné!")

        break

print("Fin du jeu, merci d'avoir joué!")

os.system("PAUSE")

