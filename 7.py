#B-76-7

n=int(input('enter number'))

for i in range(1,n):
    if i%2!=0:
        print ('(',end='')
    for c in range(1,i+2):
         if c%2!=0 and i%2!=0:
            print (c,end='+')
    if i%2!=0:
        print (')+',end='')    
