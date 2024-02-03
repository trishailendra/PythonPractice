'''
count_code:

Return the number of times that the string "code" appears anywhere in the given string,
 except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''
def count_code(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i:i + 2] == 'co' and s[i + 3] == 'e':
            count += 1
    return count
print(count_code('aaacodebbbcofeco'))