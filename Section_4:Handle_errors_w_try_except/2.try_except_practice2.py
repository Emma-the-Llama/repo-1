def divby4 (divideby):
    try:
        return 42/divideby #when code in a triclause causes a zero division error, the program execution immediately moves to the code inside the except clause.
    except ZeroDivisionError: #You can also have an except statement without specifying the type of error it catches, and it will catch all types of errors.
        print('Error, you tried to divide by zero') #after running the code in here, the execution continues running as normal, keeping the program from crashing entirely.

print(divby4(2))
print(divby4(12))
print(divby4(0)) #since it returns without a return statement, it returns the none value which gets printed here
print(divby4(1)) #the program continues on.
