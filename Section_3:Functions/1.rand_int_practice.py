import random
import sys

Number =  (random.randint(1,10))
print(str(Number))
if Number > 5:
    sys.exit() #You could  just put if number <= 5 print another random number, but for the sake of showing sys.exit i used this.
print(str(random.randint(1,10)) )