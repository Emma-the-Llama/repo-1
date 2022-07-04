print('type a message!')
message = input()
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] +1

while True:
    print('Print a letter and I can tell you how many times it shows up in your message!')
    letter = input()
    print(count.get(letter,'that letter does not show up.'))
    print('do you want to ask about another letter? Y for yes, N for no.')
    again = input()
    if again == 'Y':
        continue
    else:
        print('ok bye')
        break
