# Given an array arr[] of size N-1 with integers in the range of [1, N], 
# the task is to find the missing number from the first N integers.


# <----------- Basic Idea ----------------->
# Brute force approch or Sum of Natural numbers approch

from numpy import array


def missing_num(arr):
    n = len(arr) + 1
    formula = n * (n+1) //2
    actual_sum = sum(arr)
    diff = formula - actual_sum
    return diff

arr = [int(i) for i in input('Enter the array: ')[1:-1].split(',')]
res = missing_num(arr)
print('The missing number is ',res)
