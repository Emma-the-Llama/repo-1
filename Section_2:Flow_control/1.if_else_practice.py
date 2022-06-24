print('What the password? Be careful, you only have one try!')
Password = input()
if Password == 'blueberry':
    print('Access granted!')
    print('Would you like to know the secret? Put y for yes, and n for no.')
    secret = input()
    if secret == 'y':
        print('The secret is: Emma is awesome!!')
        print('Now logging out of computer, thank you for visiting!')
    else:
        print('bruh ok, but wasnt the whole point of getting into this computer to hear the secret? K, well you do you dude.')
else:
    print('Access denied poopy face')