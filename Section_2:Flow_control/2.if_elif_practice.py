print('Hello, what is your name?')
Name = input()
print('very cool! How old are you?')
Age = int(input())
if Name == 'Emma' and Age == '14':
    print('Oh,hi Emma, creator of this program!')
elif Name == 'Emma':
    print('well, you have the same name as Emma, creator of this program, but you are not her age!')
elif Age == '14':
    print('well, you are the same age as Emma, creator of this program, but do not have her name!')
elif Age <= 10:
    print('You are not Emma, kiddo')
elif Age >= 1000:
    print('Uhhh, hello creepy extremely old being? Please get off of this program that is kinda terrifying.')
elif Age >= 100:
    print('Damn, impressive age! I can only begin to imagine what things you have seen in your life...')
elif Age >= 76:
    print('hello Granny')
elif Age >= 58:
    print('Ok boomer')
elif Age >= 40:
    print('You are many decades too old to be Emma, but hello!')
elif Age >= 20:
    print('How is your life going? i honestly dont know what to write for this age group lol')
elif Age >= 11:
    print('Oh, you are close to Emma (the creator of this programs) age!')
print('Okay goodbye!')