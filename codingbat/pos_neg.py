
'''
pos_neg:

Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''
def pos_neg(a, b, negative):
    if (a<0 and b <0) and negative is False:
        return False
    elif (a<0 or b <0) and negative is False:
        return True
    elif (a<0 and b <0) and negative is True:
        return True
    else:
        return False
print(pos_neg(-1,-1,False))
