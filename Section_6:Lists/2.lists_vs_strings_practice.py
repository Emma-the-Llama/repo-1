#strings
spam = 42
cheese = spam
spam = 100
print(cheese)
print(spam)
#cheese is 42, because when it was assigned to the value of spam, spam was 42. And when spam is updated, cheese is not, because it was assigned to spam before that.

#lists
spam = [0, 1, 2, 3, 4, 5]
print(spam)
cheese = spam
cheese[1] = 'hello'
print(cheese)
print(spam)
#we only modified the cheese variable, so why does spam also change?
#this is because, when you assign that list value to spam, python created that list in the computer's memory, but it assigned a reference to this list spam.
#so when cheese=spam, the reference from spam gets copied to cheese. Even though we have 2 seperate references, they are referencing the same list.
#What is really in a variable with a list inside of it is a reference, not the list itself.
#This also applies to any mutable value.
#Immutable values don't have this problem because they can't be modified 'in place'. They can only be replaced by new values.


