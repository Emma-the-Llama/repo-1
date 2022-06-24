#This is a short introduction conversation, in which the program says hello and asks for my name

print('Hello!')

print('I am your computer. What is your name?') #asks for name
MyName = input() #new variable called MyName
print('Well, it is very nice to meet you ' + MyName + '!')
print('Want to know something cool? Your name is ' + str(len(MyName)) + ' letters long!') #prints length of letters in variable MyName. Needs to be converted to string.

print('Well, if this is not too rude to ask, how old are you?') #asks for age
MyAge = input() #new variable called MyAge
print('well, I have another piece of cool info to share with you! You will be ' + str(int(MyAge) + 1) + ' in a year!') #prints age you will be in a year. Needs to be converted to an integer to be added to the other integer, and then a string to be added to the other string.