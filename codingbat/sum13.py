'''
sum13:

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''
def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2  # Skip the number 13 and the number immediately following it
            continue
        total += nums[i]
        i += 1
    return total
print(sum13([13, 1, 2, 13, 2, 1, 13]))