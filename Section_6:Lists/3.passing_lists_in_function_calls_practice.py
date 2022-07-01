def eggs(cheese):
    cheese.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

#Based on the global and local scope rules, this should not print out 'hello' at the end of this list, because after eggs is called the 'hello' function is deleted.
#This works because of the use of references. 
#even though the cheese variable does get destroyed after this function returns, because it was making a change to the same list that spam was referring to, the changes in spam are reflected outside of the function.
#you are actually storing a reference to that list through a variable, and when you call a function or do an assignment, you are actually copying the reference to it, so it is actually refering to the same list.
#so any method calls or anything that you do that modify that list in place,are going to be operating on that particular list.
