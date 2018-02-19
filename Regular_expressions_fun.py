def isPhoneNumber(text):
    try:
        if len(text) != 12 and text[3] != '-' and text[7] != '-': #check length/hiphen
            return False
        elif not (text[0:3].isdecimal() and text[4:7].isdecimal() and \
             text[8:12].isdecimal()): #check digits
            return False
        else:
            return 'number'
    except IndexError:
        return 'Index out of range'

message = 'Call me 415-555-1011 tomorrow or at 415-555-9999..'



print('There are %s numbers in this list' % (len('12')))

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(phoneNumRegex.findall(message))







    
