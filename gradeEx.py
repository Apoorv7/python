
hs = input('enter mark in hindi :')
es = input('enter mark in eng. :')
cs = input('enter mark in comp. :')

#print(type(hs))
#print(type(es))
#print(type(cs))

total = int( hs) + int( es ) + int(cs)
avg = total / 3


print('total score is :',total)
print('average score is :',avg)

if avg>80:
     print('A')
elif avg>60:
     print('B')
elif avg>40:
     print('C')
else:
     print('D')
     
          
     
