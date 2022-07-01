import copy

spam = ['A', 'B', 
        'C', 'D'] #this is an example of line continuation
cheese = copy.deepcopy(spam)
cheese[0] = 100
print(spam)
print(cheese)

print('This is an exampe of line continuation here. ' + \
    'hello okay does this work? it works.') #line continuation example again. This is how you do it not in a list.


#using this function makes it so modifying cheese doesn't modify spam.