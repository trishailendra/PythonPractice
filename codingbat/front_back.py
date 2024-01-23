
'''
front_back:

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''

def front_back(str):
    if len(str)==1:
        return str
    else:
        return str[-1:]+ str[1:-1] +str[:1]

print(front_back("C"))
