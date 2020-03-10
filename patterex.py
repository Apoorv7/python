i =1
while i<40:

    if i% 2 == 0:
        print ('-',i)

    else:
        print (i)
        
    i =i+3


##pattern
for i in range(1,10):
    print ('(',)
    for c in range(1,i+1):
        if c<i:
            print (c,'+' ,)
        else:
            print (c,)
    print (')+',)
        
    
