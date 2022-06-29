# This is a guess the number game (my version)
import random
again = True
correct = False
guesses = 0
yesno = ''
number = random.randint(0, 101)

print('Hello! What is your name?')
name = input()
print('Okay ' + name + ', I am thinking of a number between 1 and 100. You have 6 guesses to find it!')

while correct == False:
    print('Take a guess!')
    guess = int(input())
    guesses = guesses + 1
    if int(guess) == number:
        print('Congrats, you guessed the right number!')
        correct = True
        print('That was fun, right? Do you want to play again? Y for yes and N for no.')
        yesno = input()
        if yesno == 'Y':
            number = random.randint(0, 101)
            print('okay!')
            guesses = 0
            correct = False
            continue
        else:
            print('okay')
            break
    if guesses == 6:
        correct = True
        print('the number was ' + str(number))
        print('Sorry, you ran out of guesses! Do you want to try again? Y for yes and N for no.')
        number = random.randint(0, 101)
        yesno = input()
        if yesno == 'Y':
            print('okay!')
            guesses = 0
            correct = False
            continue
        else:
            print('okay')
            break
    elif guess > number:
        print('The number I am thinking of is lower.')
        correct = False
    elif guess < number:
        print('The number I am thinking of is higher.')
        correct = False
print('Goodbye and thank you for playing!')
