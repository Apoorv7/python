'''
Regular Expression: re
import re

match()
search()
group()

pattern:
----------
/d    : digit 0-9
[0-9]
/D     : non digit
/w     : alphabets
/W     : non alphabets
[a-z]
[A-Z]
[0-9a-m./]
(.*)   : . any char , * : any no. of times 


'''

import re

email = input('enter email id:')
m = re.match('(.*)@gmail.com',email)
if m:
     print('correct format ')
else:
     print('incorrect format')
     
##
st = input('enter sentence id:')
m = re.match('(.*) is (.*)',st)
if m:
     print('is is present ')
else:
     print('is not exist')
     

























