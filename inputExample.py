#here sid is variable/temp. memory and input is function

sid = input('enter sid : ')

#print(type(sid)) #print data type 
#print('student id is :',sid) #print value of sid

sname = input('enter name :')

hs =  int(input('enter mark in hindi :'))
es = int(input('enter mark in eng. :'))
cs = int(input('enter mark in computer :'))
ms = int(input('enter mark in maths.  :'))


#opertion
total = hs+es+cs+ms
avg = total /4

print('total score is :',total)
print('average score is :',avg)


#print grade
if avg>=80:
     print('Grade A')
elif avg>=60:
     print('Grade B')
elif avg>=40:
     print('Grade C')
else:
     print('Grade D')


     






     






