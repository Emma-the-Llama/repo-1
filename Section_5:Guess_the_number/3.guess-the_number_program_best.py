#this is a guess the number game (his version improved to be more like my version.)
#This is the best version out of all 3.
import random

print('Hello! What is your name?')
name = input()

while True:
    print('Well, ' + name + ' I am thinking of a number between 1 and 100. Try to guess it in 6 or less.')
    secretNumber = random.randint(1, 100)

    for guessesTaken in range (1,7):
        print('Take a guess.')
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high')
        else:
            break
    if guess == secretNumber:
        print('Good job ' + name + '! You guessed the number in ' + str(guessesTaken) + ' guesses!')
        print('Would you like to play again? Y for yes, N for no.')
        again = input()
        if again == 'Y':
            continue
        else:
            break
    else:
        print('The number I was thinking of was ' + str(secretNumber) + '!')
        print('Would you like to play again? Y for yes, N for no.')
        again = input()
        if again == 'Y':
            continue
        else:
            break
print('Okay, thank you for playing ' + name + '!')