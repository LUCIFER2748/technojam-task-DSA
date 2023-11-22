# Given a non-negative integer n. The problem is to reverse the bits of n 
# and print the number obtained after reversing the bits. 
# Note that the actual binary representation of the number is being considered for reversing the bits, 
# no leadings 0’s are being considered.

# <------------------- Basic Idea --------------------->
# Convert a number in a binary representationa and reverse it using string manipulation then handle zeros

def reverse_bits(num):
    '''Implementation'''
    bin_num = str(bin(num))[2:]
    rev_bin = bin_num[::-1]
    dec_num = int(rev_bin,2)
    return dec_num

n = input('Enter the number: ')
print('The output is:',reverse_bits(n))
