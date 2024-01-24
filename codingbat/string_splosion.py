
'''
string_splosion:

Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''
def string_splosion(str):
    str1 = ""
    for n in range(0,len(str)+1):
        str1 +=str[:n:]
    return str1

print(string_splosion("code"))

