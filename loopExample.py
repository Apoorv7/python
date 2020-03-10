#while loop example
i =1 # init
while i<10: # condition
     print(i,end='\t')
     i =i+1

#print in reverse order
i =10
while i>0:
     print(i)
     i =i-1

#print all odd numbers between 1 to 30
i =1
while i<=30:
     print(i)
     i =i+2

#print sum of all even no. and odd numbers between two given no.
n1 = int(input('enter first no. :'))
n2 = int(input('enter 2nd  no. :'))

se = 0
so =0

while n1<=n2:
     if n1%2==0:
          se = se+n1
     else:
          so = so+n1
          
     n1 = n1+1


print('sum of all even no. :',se)
print('sum of all odd no. :',so)

#wap to print table of given no.
t = int(input('enter no. :'))
i =1
while i<=10:
     print(t,'*',i,'=',t*i)
     i =i+1
     



### for loop
for i in range(1,10): # from 1 to 9, default incrementer is 1
     print(i)

#reverse
for x in range(10,0,-1):
     print(x)

     
     

     



     


          
     



     
     
