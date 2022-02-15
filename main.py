from ast import Expression
import numbers
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random.number:
        guess = int(input('Odgadnij liczbę od 1 do: {x}'))
        print(guess)
        if guess < random_number:
            print('Pudło, zgadnij jeszcze raz. Za nisko.')
        elif guess > random_number:
            print('Pudło, zgadnij jeszcze raz. Za wysoko.')
    
    print(f'Gratulacje. Odgadłeś numer {random_number} prawidłowo!')

guess(10)