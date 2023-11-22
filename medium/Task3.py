# Find the factorial of a large number.


# <----------- Basic idea -------------->
# recurssion or a loop

def factorial(val):
    if val == 0:
        return 0

    factor = 1

    for i in range(1,val+1):
        factor *= i

    return factor

num = int(input("Enter the number: "))
res = factorial(num)
print(f'The factorial of {num} is: {res}')
