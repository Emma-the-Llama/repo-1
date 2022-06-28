#This program will cause an error.
def divby4 (divideby):
    return 42/divideby

print(divby4(2))
print(divby4(12))
print(divby4(0)) #everything before this is good, but the error happened here. Computers can't handle dividing a number by 0.
print(divby4(1)) #this function call never gets made because the crashed before it.

#You can handle an error with try and except statements.