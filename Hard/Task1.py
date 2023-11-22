# Given two numbers a and b as interval range, the task is to find the prime numbers in between this interval.

# <----------------- Basic Idea ------------------------>
# Run a loop uto half the number and check the prime number

def check_prime(num):
    '''Prime num check'''
    if num < 2:
        return False

    for i in range(2, num//2+1):
        if num % i == 0:
            return False

    return True

def interval_prime(a,b):
    '''Checks for prime number in range a and b'''
    prime = []

    for i in range(a,b+1):
        flag = check_prime(i)
        if flag is True:
            prime.append(i)

    return prime

a = int(input("Enter the starting Point: "))
b = int(input("Enter the ending Point: "))
res = interval_prime(a,b)

print(f'The prime numbers between {a} and {b} are: {res}')
