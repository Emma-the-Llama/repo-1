def spam():
    print(eggs)

eggs = 42 #this is a global eggs variable

spam()
#since there is no local variable named eggs, python checks to see if there is a global eggs variable. Since there is, it prints that.
#If you see a variable inside of a function, is it a local variable, or is it a global variable that's just being read from the local scope?
#The way python distinguishes between these two possibilities, is that if there is an assignment statement, for a variable anywhere in that function, it is considered a local variable. 
#ONLY if there isn't an assignment statement like in this example, python checks if there is a global variable by that name.
# Therefore, code in a local scope can access a global variable

def spam():
    eggs = 99
    print(eggs) #in this program, python treats this as a local variable now since there is an assignment statement.

eggs = 42 

spam() #therefore when it runs spam it prints out the local variable eggs which is 99

print(eggs) #but now in the global scope, the eggs variable that it will print is the global variable which is 42.