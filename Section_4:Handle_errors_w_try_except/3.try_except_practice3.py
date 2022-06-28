correct = False
while correct == False:
    print('How many cats do you have?')
    numCats = input()
    try:
        if int(numCats) >= 10:
            correct = True
            print('that may be a bit too many cats but you do you dude')
        elif int(numCats) >= 3:
            correct = True
            print('That is a lot of cats.')
        elif int(numCats) == 2:
            correct = True
            print('That is a good amount of cats.')
        elif int(numCats) == 1:
            correct = True
            print('That is the number of cats that I, the designer of this program owns!')
        elif int(numCats) == 0:
            correct = True
            print('You should get a cat!')
        elif int(numCats) < 0:
            correct = False
            print('It is impossible to have a negative number of cats. Please type a positive number!')
    except ValueError: #if you get a value error during the thing you try, it prints the below.
        correct = False
        print('Please enter a number!')
        