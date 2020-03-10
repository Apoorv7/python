'''
Exception Handling:

Exception: is run time error which may or may not occur
Handling: tackle the error when this will occur
Advantage:
-Prevent the entire code from failure due to single/few error
-Show user friendly/Custom message
-Maintain the error logs/send the notifications

There are following inbuilt keywords:
-try
-except
-finally : is optioal block which will execute always either exception will occur or not
-raise 
'''
'''
#div
try:
     n = int(input('enter data :'))
     d = int(input('enter data :'))

     if d<0:
          err = ZeroDivisionError('divisor cannot be less than 0')
          raise err
     
     o = n/d
     print(o)
     #
except ValueError as e:
     print(e, ' erro ')
     #
except ZeroDivisionError as e:
     print(e)
     #
except:
     print('there is technical issue.')
     #
finally:
     print('enter of block ')
     

###sum
n = int(input('enter data :'))
d = int(input('enter data :'))

o =n+d
print(o)


'''
###
while True:
     try:
          n = int(input('enter data :'))
          d = int(input('enter data :'))

          o = n/d
          print(o)
          break
     except:
            print('something went wrong , try again!!!')
            

