password = ''
while True:
    print('What is the password?')
    password = input()
    if password == 'password':
        continue #goes back to the beginning, so the last line in this block is not printed.
    if password == 'blueberry':
        break
    print('Congratulations on not thinking I am stupid enough to put my password as "password"! But it is still wrong, try again!')
print('Correct password entered! Have a great day :)')