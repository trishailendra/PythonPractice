'''
cat_dog:

Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
'''
def cat_dog(str):
    str='a'+str
    if str.find("dog"):
       if str.find("cat"):
          if str.count("cat")==str.count("dog"):
             return True
    return False
print(cat_dog('1catcat1cadogdoerdogr'))