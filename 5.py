#B-76-5

n=int(input('enter number'))

for i in range(1,n):
    print ('(',)
    for c in range(1,i+1):
        if c<i:
            print (c,'+' ,)
        else:
            print (c,)
    print (')+',)
        
    
