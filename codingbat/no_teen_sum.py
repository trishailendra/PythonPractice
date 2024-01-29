'''
no_teen_sum:

Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- 
then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper 
"def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, 
you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
'''
def no_teen_sum(a, b, c):
        def fix_teen(n):
             return n==15
        if a>12 and a<20 and a!= fix_teen():
             return b+c
        elif b>12 and b<20:
            return a+c
        elif c>12 and c<20:
            return a+b
        else:
            return a+b+c

print(no_teen_sum(16, 17, 18))
