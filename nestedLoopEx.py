'''
4 rows ,and cols

123   R =1 , c 1 2 3
123   r = 2  , c 1 2 3 
123
123

'''
for r in range(1,5):
     for c in range(1,4):
          print(c,end=' ')
     print()
     
          

##pattern # increase 
for r in range(1,5):
     for c in range(1,r+1):
          print(c,end=' ')
     print()

#pattern  # decrease
for r in range(1,5):
     for c in range(5,r,-1):
          print('*',end=' ')
     print()




     
          
