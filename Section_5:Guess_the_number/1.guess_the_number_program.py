#This is a guess the number game (my version)
import random

print('Hello! What is your name?')
name = input()
print('Okay ' + name + ', I am thinking of a number between 1 and 100. You have 10 guesses to find it!')
number = random.randint(0,101)

correct = False

while correct == False:
    print('Take a guess!')
    guess = int(input())
    if guess == number:
        print('Congrats, you guessed the right number!')
        correct = True
    elif guess > number:
        print('The number I am thinking of is lower.')
        correct = False
    elif guess < number:
        print('The number I am thinking of is higher.')
        correct = False

