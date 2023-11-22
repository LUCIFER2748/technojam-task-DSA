# 1.Write a program to reverse an array or string.


# <--------- Basic Idea --------------->
# use simple list comprehension


def reverse_array(array):
    '''Function to Reverse a array'''
    return array[::-1]

arr = [int(i) for i in input('Enter the array: ')[1:-1].split(',')]

print('The reverse of',arr,' is', reverse_array(arr))
