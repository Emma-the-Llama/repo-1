#This will add up number 1+2+3+4 etc. until 100 (including 100)
total = 0
for num in range(101): #it dones't include 101, only 0-100
    total = total + num
print(total)

#while loop equivalent
Total = 0
Num = 1
while Num <= 100:
    Total = Total + Num
    Num = Num + 1
print(Total)