animals = ['cats', 'dogs', 'guinea pigs', 'rats', 'pigs']

for i in range(len(animals)):
    print('Index ' + str(i) + ' in supplies is: ' + animals[i])

print('Lets hear more about index 0, cat.')

#multiple assignment
cat = ['fat','white','hungry']
weight, color, state = cat
print('Ozzie the cat is ' + weight + ' in weight, ' + color + ' in color, and always very ' + state) 
