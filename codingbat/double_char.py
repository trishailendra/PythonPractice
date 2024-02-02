'''
double_char:


Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''
def double_char(str):
    chr=''
    for i in list(str):
        chr+= i*2
    return chr
        
print(double_char('The'))
    