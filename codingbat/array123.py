'''
array123:

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

'''

def array123(nums):
    for i in range(1,len(nums)):
        if (nums[i-1:i+2])==[1,2,3]:
            return True
    return False

print (array123([1, 1, 1, 3, 2, 2]))