#B-76-6

n=int(input('enter number'))

for i in range(2,n):
    print ('(',)
    for c in range(2,i+2):
         if c%2==0 and i%2==0:
            print (c,'+' ,)
            
    print (')+',)    
