
'''
string_splosion:

Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''
def string_splosion(str):
    for x in len(str)<0:
        return str[x]
print(string_splosion("code"))

