print('Enter a name.')
name = input()
if name: #it would be better to put something like: if name != '0':, but for the sake of showing truthy and falsey it is this.
    print('Thank you for entering something!')
else:
    print('You did not enter a name :(')