myCat = {'size':'fat', 'color':'white', 'texture':'fluffy',} #the keys are size, color and texture. The values are fat, white and fluffy.

print('Ozzie is ' + myCat['size'] + ', ' + myCat['color'] + ', and ' + myCat['texture'] + '!')

for k, v in myCat.items():
    print(k, v)
#I do not fully understand for loops but cool


#get method example.
print('Did we learn ozzies color?')
print('Yeah! Ozzie is ' + myCat.get('color','... Waitttt... we did not learn this information!'))

print('Okay, well did we learn ozzies state?')
print(myCat.get('state','no we did not.'))

#set default practice
print('Well, if we do not know ozzies state, lets assign that')
print('What is ozzies state?')
state = input()
myCat.setdefault('state', state)

print('so, then:')
for k, v in myCat.items():
    print(k, v)