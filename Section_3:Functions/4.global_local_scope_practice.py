#This will not work 
def spam(): #spam function gets defined
    eggs = '99'

spam() #call the spam function. This has created a local scope, and the local variable eggs.
print(eggs) #spam function is returned, local scope and variables are destroyed. Therefore the eggs variable no longer exists, and you cannot print the egg variable.
#Therefore local variables cannot be used in the global scope.