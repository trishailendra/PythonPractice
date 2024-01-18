
'''

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True

'''

def sleep_in(weekday, vacation):
    a= weekday
    b=vacation
    if a==False and b==False:
        return True
    elif a== True and b== False:
        return False
    elif a== False and b== True:
        return True
    elif a== True and b== True:
      return True
    else: 
        return False
print(sleep_in(False, True))

