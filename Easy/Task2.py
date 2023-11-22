# Given an array of N integers, and an integer K, 
# the task is to find the number of pairs of integers 
# in the array whose sum is equal to K.

# <---------- Basic Ideaa -------------->
# sort the list - initate 2 pointer - if the sum of right and left is smaller decrease left else decrease right



def count_pairs(arr, K):
    '''Implementation'''
    arr.sort()

    left, right = 0, len(arr) - 1
    count = 0

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == K:
            count += 1
            left += 1
            right -= 1
        elif current_sum < K:
            left += 1
        else:
            right -= 1

    return count

arr = [int(i) for i in input('Enter the array: ')[1:-1].split(',')]
K = int(input('Enter the target: '))

result = count_pairs(arr,K)

print("Number of pairs with sum equal to", K, "is:", result)
