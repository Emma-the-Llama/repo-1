cnt = 0
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            if  n > 9950:
                 print(n, 'equals', x, '*', n // x )
            break
    else:
         print(n, "\tis a prime number")
         cnt += 1

print("\n\n\t\t Total number of primes is", cnt, "\n\n")
