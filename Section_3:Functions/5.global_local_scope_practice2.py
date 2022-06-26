#This will not work.
def spam(): #spam is defined
    eggs = 99
    bacon()
    print(eggs)

def bacon(): #bacon is defined
    ham = 101
    eggs = 0

spam() 
#spam is called. It's local scope is created. The local variable eggs is created. 
#Bacon is called within the spam function. A new local scope for bacon is also created. The local variable ham is created.
#Then, we assign the local variable eggs to 0. But this eggs local variable is a seperate variable to the eggs local variable in spam.
#Then we return to the spam function, and the local scope of bacon is destroyed. So the ham and eggs variables are now gone.
#So now, within the spam function we print eggs. But it will be printing out spam's eggs variable, which is 99.
#Therefore, local scopes cannot use variables in other local scopes. The eggs in spam can only refer to eggs in spam.
#It makes it more clear though, since when you see the eggs variable in one function, you know it is only in that function, and not some other fucntion.